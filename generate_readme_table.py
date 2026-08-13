#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb>=1.0.0",
# ]
# ///
"""Generate the chart inventory table in README.md from the exported parquet files.

For every ``data/*.parquet`` file this records the chart, its file path, the
date range it covers (from -> to), the number of rows, and the SHA-256 hash of
the file. The table is written between the marker comments in README.md so the
surrounding prose is preserved. README.md is created from a small template if it
does not exist yet.

Usage:
    uv run generate_readme_table.py                 # data/ -> README.md
    uv run generate_readme_table.py --data-dir data --readme README.md
"""

import argparse
import glob
import hashlib
import os

import duckdb

TABLE_START = "<!-- CHART-INVENTORY:START -->"
TABLE_END = "<!-- CHART-INVENTORY:END -->"

README_TEMPLATE = """# Billboard Charts Archive

A weekly-updated archive of historical Billboard chart data, exported as one
[Apache Parquet](https://parquet.apache.org/) file per chart under `data/`.

The data is collected by `billboard_charts_archive.py` and refreshed every
Sunday by the [`weekly-update`](.github/workflows/weekly-update.yml) GitHub
Actions workflow.

## Chart inventory

The table below is generated automatically from the parquet files on every
update -- do not edit it by hand.

{table}
"""


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def human_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def build_table(data_dir: str) -> str:
    con = duckdb.connect()
    rows = []
    for path in sorted(glob.glob(os.path.join(data_dir, "*.parquet"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        title, first, last, count = con.execute(
            """
            SELECT any_value(chart_title), min(chart_date), max(chart_date), count(*)
            FROM read_parquet(?)
            """,
            [path],
        ).fetchone()
        rows.append(
            {
                "chart": title or slug,
                "path": path.replace(os.sep, "/"),
                "from": first.isoformat() if first else "",
                "to": last.isoformat() if last else "",
                "rows": count or 0,
                "size": human_size(os.path.getsize(path)),
                "sha256": sha256_of(path),
            }
        )
    con.close()

    header = (
        "| Chart | File | From | To | Rows | Size | SHA-256 |\n"
        "| ----- | ---- | ---- | -- | ----:| ----:| ------- |"
    )
    lines = [header]
    for r in rows:
        lines.append(
            f"| {r['chart']} | [`{r['path']}`]({r['path']}) | {r['from']} | {r['to']} "
            f"| {r['rows']:,} | {r['size']} | `{r['sha256']}` |"
        )
    return "\n".join(lines)


def render_readme(existing: str | None, table: str) -> str:
    block = f"{TABLE_START}\n{table}\n{TABLE_END}"
    if existing is None:
        return README_TEMPLATE.format(table=block)

    if TABLE_START in existing and TABLE_END in existing:
        before = existing.split(TABLE_START)[0]
        after = existing.split(TABLE_END, 1)[1]
        return f"{before}{block}{after}"

    # README exists but has no marker block yet -- append the section.
    sep = "" if existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
    return f"{existing}{sep}## Chart inventory\n\n{block}\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default="data", help="directory of <slug>.parquet files")
    parser.add_argument("--readme", default="README.md", help="README file to update")
    args = parser.parse_args()

    table = build_table(args.data_dir)
    existing = None
    if os.path.exists(args.readme):
        with open(args.readme, encoding="utf-8") as fh:
            existing = fh.read()

    new_content = render_readme(existing, table)
    with open(args.readme, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    print(f"Updated {args.readme} with inventory for {len(glob.glob(os.path.join(args.data_dir, '*.parquet')))} chart(s)")


if __name__ == "__main__":
    main()
