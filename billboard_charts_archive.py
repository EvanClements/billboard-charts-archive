#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "billboard.py>=7.0.0",
#     "duckdb>=1.0.0",
# ]
# ///
"""Archive Billboard charts into a local DuckDB database.

Usage:
    uv run billboard_charts_archive.py --list-charts
    uv run billboard_charts_archive.py --chart hot-100 --chart alternative-airplay
    uv run billboard_charts_archive.py --chart hot-100 --start-date 1970-01-01 --end-date 1979-12-31
    uv run billboard_charts_archive.py --export-parquet data/              # dump db as-is, no fetching
    uv run billboard_charts_archive.py --chart hot-100 --start-date 2026-07-01 --export-parquet data/
"""

import argparse
import os
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta

import billboard
import duckdb

# billboard.py 7.1.0's per-entry parser calls _pageHasAwardColumn(soup) once for
# EVERY chart entry, and each call re-scans the entire page with a CSS selector.
# For a 100-entry chart that's ~100 full-document scans, ~25-30s per chart-week.
# The result only depends on the page, so cache it per soup object (by identity,
# not content-hash: BeautifulSoup's __hash__ serializes the whole tree, which is
# just as slow). This turns ~28s/week into ~2.5s/week.
_award_column_cache: dict[int, bool] = {}
_orig_page_has_award_column = billboard.ChartData._pageHasAwardColumn


def _cached_page_has_award_column(self, soup):
    key = id(soup)
    if key not in _award_column_cache:
        _award_column_cache.clear()  # only ever parsing one page at a time
        _award_column_cache[key] = _orig_page_has_award_column(self, soup)
    return _award_column_cache[key]


billboard.ChartData._pageHasAwardColumn = _cached_page_has_award_column

DEFAULT_DB_PATH = "billboard_charts.db"
DEFAULT_DELAY_SECONDS = 0.5
PROGRESS_EVERY = 25  # print an ETA line every N fetches


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


@dataclass(frozen=True)
class ChartInfo:
    slug: str
    label: str
    start_date: date  # approximate chart launch date; used as default backfill start


# A curated set of commonly-archived Billboard charts. Any other chart slug
# from https://www.billboard.com/charts/ can still be passed via --chart,
# it just won't have a known default start date (pass --start-date too).
CURATED_CHARTS: dict[str, ChartInfo] = {
    "hot-100": ChartInfo("hot-100", "Billboard Hot 100", date(1958, 8, 4)),
    "billboard-200": ChartInfo("billboard-200", "Billboard 200 (Albums)", date(1963, 1, 5)),
    "artist-100": ChartInfo("artist-100", "Artist 100", date(2014, 7, 19)),
    "alternative-airplay": ChartInfo("alternative-airplay", "Alternative Airplay", date(1988, 9, 10)),
    "pop-songs": ChartInfo("pop-songs", "Pop Airplay", date(1992, 3, 21)),
    "country-airplay": ChartInfo("country-airplay", "Country Airplay", date(2012, 1, 21)),
    "r-b-hip-hop-songs": ChartInfo("r-b-hip-hop-songs", "Hot R&B/Hip-Hop Songs", date(1958, 10, 20)),
    "rock-songs": ChartInfo("rock-songs", "Hot Rock & Alternative Songs", date(2009, 7, 18)),
    "dance-electronic-songs": ChartInfo("dance-electronic-songs", "Hot Dance/Electronic Songs", date(2013, 8, 10)),
    "hot-mainstream-rock-tracks": ChartInfo("hot-mainstream-rock-tracks", "Mainstream Rock Airplay", date(1981, 3, 21)),
    "adult-contemporary": ChartInfo("adult-contemporary", "Adult Contemporary", date(1961, 7, 17)),
}


def list_charts() -> None:
    print(f"{'slug':<24} {'label':<32} approx. start date")
    print("-" * 72)
    for info in CURATED_CHARTS.values():
        print(f"{info.slug:<24} {info.label:<32} {info.start_date.isoformat()}")
    print()
    print("Any other chart slug from https://www.billboard.com/charts/ also works")
    print("via --chart <slug>, just pass --start-date explicitly too.")


def format_duration(seconds: float) -> str:
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}h{minutes:02d}m"
    if minutes:
        return f"{minutes}m{secs:02d}s"
    return f"{secs}s"


def week_saturdays(start: date, end: date):
    """Billboard chart dates always fall on a Saturday."""
    days_ahead = (5 - start.weekday()) % 7  # Monday=0 ... Saturday=5
    current = start + timedelta(days=days_ahead)
    while current <= end:
        yield current
        current += timedelta(weeks=1)


def ensure_schema(con: duckdb.DuckDBPyConnection) -> None:
    con.execute("""
        CREATE TABLE IF NOT EXISTS chart_entries (
            chart_slug VARCHAR NOT NULL,
            chart_title VARCHAR,
            chart_date DATE NOT NULL,
            rank INTEGER NOT NULL,
            title VARCHAR,
            artist VARCHAR,
            peak_pos INTEGER,
            last_pos INTEGER,
            weeks_on_chart INTEGER,
            is_new BOOLEAN,
            image_url VARCHAR,
            fetched_at TIMESTAMP DEFAULT current_timestamp
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS fetch_progress (
            chart_slug VARCHAR NOT NULL,
            chart_date DATE NOT NULL,
            status VARCHAR NOT NULL,
            fetched_at TIMESTAMP DEFAULT current_timestamp,
            PRIMARY KEY (chart_slug, chart_date)
        )
    """)


def already_fetched(con: duckdb.DuckDBPyConnection, slug: str) -> set:
    rows = con.execute(
        "SELECT chart_date FROM fetch_progress WHERE chart_slug = ?", [slug]
    ).fetchall()
    return {r[0] for r in rows}


def fetch_and_store(
    con: duckdb.DuckDBPyConnection,
    slug: str,
    chart_date: date,
    delay_seconds: float,
) -> str:
    """Fetch one chart-week and store it. Returns status: ok | empty | error."""
    try:
        chart = billboard.ChartData(slug, date=chart_date.isoformat())
    except Exception as exc:  # billboard.py raises plain Exceptions on failure
        log(f"  {chart_date}: ERROR {exc}")
        con.execute(
            "INSERT INTO fetch_progress VALUES (?, ?, 'error', current_timestamp)",
            [slug, chart_date],
        )
        time.sleep(delay_seconds)
        return "error"

    if not chart.entries:
        log(f"  {chart_date}: empty (chart not yet published)")
        con.execute(
            "INSERT INTO fetch_progress VALUES (?, ?, 'empty', current_timestamp)",
            [slug, chart_date],
        )
        time.sleep(delay_seconds)
        return "empty"

    rows = [
        (
            slug,
            chart.title,
            chart_date,
            e.rank,
            e.title,
            e.artist,
            e.peakPos,
            e.lastPos,
            e.weeks,
            e.isNew,
            getattr(e, "image", None),
        )
        for e in chart.entries
    ]
    con.executemany(
        """INSERT INTO chart_entries
           (chart_slug, chart_title, chart_date, rank, title, artist,
            peak_pos, last_pos, weeks_on_chart, is_new, image_url)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        rows,
    )
    con.execute(
        "INSERT INTO fetch_progress VALUES (?, ?, 'ok', current_timestamp)",
        [slug, chart_date],
    )
    log(f"  {chart_date}: {len(rows)} entries")
    time.sleep(delay_seconds)
    return "ok"


def export_parquet(con: duckdb.DuckDBPyConnection, out_dir: str, slugs: list[str]) -> None:
    """Write one parquet file per chart. If a file already exists, its rows are
    merged with the current db content instead of being overwritten, keeping the
    newest fetch for any (chart, date, rank) that appears in both -- this lets the
    same flag serve as a one-off historical export and a weekly incremental update."""
    os.makedirs(out_dir, exist_ok=True)
    for slug in slugs:
        path = os.path.join(out_dir, f"{slug}.parquet")
        con.execute(
            "CREATE OR REPLACE TEMP TABLE _export AS SELECT * FROM chart_entries WHERE chart_slug = ?",
            [slug],
        )
        if os.path.exists(path):
            # Billboard charts can have genuine ties (two titles sharing one rank
            # in the same week), so the dedup key must include title/artist --
            # (chart_slug, chart_date, rank) alone would silently collapse ties.
            con.execute(
                """
                CREATE OR REPLACE TEMP TABLE _export AS
                SELECT * EXCLUDE (_rn) FROM (
                    SELECT *, row_number() OVER (
                        PARTITION BY chart_slug, chart_date, rank, title, artist
                        ORDER BY fetched_at DESC
                    ) AS _rn
                    FROM (
                        SELECT * FROM read_parquet(?)
                        UNION ALL BY NAME
                        SELECT * FROM _export
                    )
                )
                WHERE _rn = 1
                """,
                [path],
            )
        row_count = con.execute("SELECT count(*) FROM _export").fetchone()[0]
        con.execute(f"COPY (SELECT * FROM _export ORDER BY chart_date, rank) TO '{path}' (FORMAT parquet)")
        log(f"  exported {slug}: {row_count} rows -> {path}")


def resolve_chart(slug: str, start_date_arg: str | None) -> tuple[str, date]:
    info = CURATED_CHARTS.get(slug)
    if start_date_arg:
        start = datetime.strptime(start_date_arg, "%Y-%m-%d").date()
    elif info:
        start = info.start_date
    else:
        raise SystemExit(
            f"Unknown chart '{slug}' has no default start date; pass --start-date YYYY-MM-DD"
        )
    return slug, start


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-charts", action="store_true", help="print curated chart slugs and exit")
    parser.add_argument(
        "--chart",
        action="append",
        default=[],
        help="chart slug, repeatable (see --list-charts); pass 'all' for every curated chart",
    )
    parser.add_argument("--start-date", help="YYYY-MM-DD, defaults to the chart's known launch date if curated")
    parser.add_argument("--end-date", help="YYYY-MM-DD, defaults to today")
    parser.add_argument("--db", default=DEFAULT_DB_PATH, help=f"DuckDB file path (default: {DEFAULT_DB_PATH})")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS, help="seconds to sleep between requests")
    parser.add_argument("--limit", type=int, default=None, help="max new weeks to fetch this run, across all charts")
    parser.add_argument("--force", action="store_true", help="re-fetch weeks already recorded in fetch_progress")
    parser.add_argument(
        "--export-parquet",
        metavar="DIR",
        help="after fetching, write one <slug>.parquet per chart into DIR "
        "(merged with any existing file there); with no --chart, exports "
        "every chart already in the db without fetching anything new",
    )
    args = parser.parse_args()

    if args.list_charts:
        list_charts()
        return

    if not args.chart and not args.export_parquet:
        parser.error("pass at least one --chart (see --list-charts) or --export-parquet")

    if "all" in args.chart:
        args.chart = list(CURATED_CHARTS.keys())

    end = datetime.strptime(args.end_date, "%Y-%m-%d").date() if args.end_date else date.today()

    con = duckdb.connect(args.db)
    ensure_schema(con)

    fetched_total = 0
    try:
        for slug in args.chart:
            slug, start = resolve_chart(slug, args.start_date)
            done = set() if args.force else already_fetched(con, slug)
            all_weeks = list(week_saturdays(start, end))
            todo = [wk for wk in all_weeks if wk not in done]
            log(
                f"== {slug} : {start} -> {end} | "
                f"{len(done)}/{len(all_weeks)} already done, {len(todo)} to fetch =="
            )

            chart_start_time = time.monotonic()
            for i, wk in enumerate(todo, start=1):
                if args.limit is not None and fetched_total >= args.limit:
                    log(f"Reached --limit {args.limit}, stopping.")
                    return
                fetch_and_store(con, slug, wk, args.delay)
                fetched_total += 1

                if i % PROGRESS_EVERY == 0:
                    elapsed = time.monotonic() - chart_start_time
                    rate = i / elapsed  # weeks/sec, includes delay+request time
                    remaining = len(todo) - i
                    eta = remaining / rate if rate > 0 else 0
                    log(
                        f"  -- progress: {i}/{len(todo)} this run "
                        f"({rate * 60:.1f} weeks/min, elapsed {format_duration(elapsed)}, "
                        f"ETA {format_duration(eta)}) --"
                    )

        if args.export_parquet:
            slugs = args.chart or [
                r[0] for r in con.execute("SELECT DISTINCT chart_slug FROM chart_entries").fetchall()
            ]
            log(f"== exporting {len(slugs)} chart(s) to {args.export_parquet} ==")
            export_parquet(con, args.export_parquet, slugs)
    finally:
        con.close()

    log(f"Done. Fetched {fetched_total} new chart-week(s) into {args.db}")


if __name__ == "__main__":
    main()
