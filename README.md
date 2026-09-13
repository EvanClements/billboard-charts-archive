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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-09-12 | 124,358 | 1.7 MB | `5718ce9b146bc7ea9bd848b055414ac7b466cd46fab728a46bf2d06953f4b05d` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-09-12 | 76,230 | 1.0 MB | `e93fcff2351647b665914ca2473370de6ff6a9ed53e5a8bcda4285a6cbdd12e9` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-09-12 | 63,500 | 864.8 KB | `379067c4a902a2730eb32bf98f8017ff6582d685764a8c71f5fc3854da838fcc` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-09-12 | 649,330 | 9.2 MB | `1283367979216004925e5d94d41147c5270bac4b07282b3212a0188385efcca0` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-09-12 | 45,840 | 577.3 KB | `080737869bf87d82099afc02207f2ae7f9502d9ba6245c8dd7661efd7e8d2643` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-09-12 | 32,025 | 522.9 KB | `57de3a7e31db417d2957791b44f668f80f984c1c8fe726fb6626844828198a99` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-09-12 | 355,391 | 5.0 MB | `780e80137c042fb5abb09af4bbacd9aa4c278605ecd0070e6e761c945078bcfb` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-09-12 | 94,920 | 1.2 MB | `5d558d583a0480067bac7fa615fd6edc262d275a7350c1b4625080be9e136617` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-09-12 | 72,000 | 1009.4 KB | `3fbbd2092f2ae57017fd3653a7d80f58143643f9b1e5db44968ceace48291497` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-09-12 | 254,376 | 3.5 MB | `4b86e32026a8b90d95f3ee0348d3657a8a830f5e68d9c5a1973025d634d18f2b` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-09-12 | 44,802 | 670.1 KB | `bba7a0eec5bd7b64b5b885e86697c2bdd54e747bf31b9705c4b9190984330d21` |
