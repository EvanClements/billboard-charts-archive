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

# The generator owns the section under this heading: on each run it replaces
# everything from this heading up to the next level-2 (## ) heading, or the end
# of the file. This keeps the rendered README free of visible marker comments
# while still letting the table be regenerated in place.
SECTION_HEADING = "## Chart inventory"
SECTION_INTRO = (
    "This section is generated from the parquet files on every update; "
    "the table lists each chart, its file, the date range it covers, and the "
    "SHA-256 of the file."
)

README_TEMPLATE = """# Billboard Charts Archive

A weekly-updated archive of historical Billboard chart data, exported as one
[Apache Parquet](https://parquet.apache.org/) file per chart under `data/`.

The data is collected by `billboard_charts_archive.py` and refreshed every
Sunday by the [`weekly-update`](.github/workflows/weekly-update.yml) GitHub
Actions workflow.

{section}
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


def render_section(table: str) -> str:
    return "\n".join([SECTION_HEADING, "", SECTION_INTRO, "", table])


def render_readme(existing: str | None, table: str) -> str:
    section = render_section(table)
    if existing is None:
        return README_TEMPLATE.format(section=section)

    lines = existing.splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.strip() == SECTION_HEADING), None
    )

    if start is None:
        # README exists but has no inventory section yet -- append one.
        body = existing.rstrip("\n")
        return f"{body}\n\n{section}\n"

    # Replace from the heading up to the next level-2 heading (or end of file),
    # so any sections following the inventory are preserved untouched.
    end = next(
        (j for j in range(start + 1, len(lines)) if lines[j].startswith("## ")),
        len(lines),
    )
    before = "\n".join(lines[:start]).rstrip("\n")
    after = "\n".join(lines[end:]).strip("\n")

    result = f"{before}\n\n{section}" if before else section
    if after:
        result = f"{result}\n\n{after}"
    return result + "\n"


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
