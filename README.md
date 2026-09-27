# Billboard Charts Archive

A weekly-updated archive of historical Billboard chart data, exported as one
[Apache Parquet](https://parquet.apache.org/) file per chart under `data/`.

The data is collected by `billboard_charts_archive.py` and refreshed every
Sunday by the [`weekly-update`](.github/workflows/weekly-update.yml) GitHub
Actions workflow.

## Chart inventory

This section is generated from the parquet files on every update; the table lists each chart, its file, the date range it covers, and the SHA-256 of the file.

| Chart | File | From | To | Rows | Size | SHA-256 |
| ----- | ---- | ---- | -- | ----:| ----:| ------- |
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-09-19 | 124,388 | 1.7 MB | `189b47354a743bbc969f3657b0b34bc159845d92f94909de5c364ecde0c26524` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-09-19 | 76,270 | 1.0 MB | `8b45c84f05b39c95fc3a2f04a57663e5903822abb8909a4d89ecbd16d7a262c2` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-09-19 | 63,600 | 865.8 KB | `9e5328b06ab23af49f0d7c3c7dc6a07292ce07a9f3e2abe038eafa6d5ca1e27d` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-09-19 | 649,530 | 9.2 MB | `0782a205e3d8695cd6dfb52c630ed22f09be8e7ffc1b0da85063d22ea3eda399` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-09-19 | 45,900 | 577.6 KB | `9307b1f8e297190bf096f4b1a7554525f006e915ba15d359927259cb9795d815` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-09-19 | 32,051 | 523.2 KB | `c1c03d38d0bb408398e2efe2a487830b091be3ffb0a605341056cfbc644e3207` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-09-19 | 355,491 | 5.0 MB | `3cfb3bf69c21b0ef66c8334a08ec4ef5486d7185c917d05760f935e92003fbbb` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-09-19 | 94,960 | 1.2 MB | `0c7dfa67599ed9b68b495b1dbb5f049f7695a75817365cb3400d6f50e3ebb7f9` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-09-19 | 72,040 | 1009.7 KB | `dc8411c487320a94ca6bcb36a999278c5038329594dce234b5e6e2f82dcaa52f` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-09-19 | 254,426 | 3.5 MB | `2c86d6865ed3e137724d8c631dd57d1c6098263a2f27c1995f59e379ffdbdfe1` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-09-19 | 44,852 | 671.1 KB | `6ac3fec27d1149ca2579aee97a38eb2b996c8102ae2d8b1f59b95de0f7f76d5c` |
