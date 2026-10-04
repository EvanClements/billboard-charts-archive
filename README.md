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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-09-19 | 124,388 | 1.7 MB | `616ab679a5abeed7f8512871362f354253271fe40b789719aba6d720b8b7698c` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-09-19 | 76,270 | 1.0 MB | `d9d20521a61da398a975e696a5cc0d2e372b857ee5016ce166752918194188e0` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-09-19 | 63,600 | 865.8 KB | `0cf3400efca37022896323e06d6773f989dd02bc70dd01b9386fa96a99232301` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-09-19 | 649,530 | 9.2 MB | `23113ee198718136eb05ef17e62307c1d7dce6b7c0981fbac29315160439a3e2` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-09-19 | 45,900 | 577.6 KB | `38919e611eac9f364db43434938503c5b814380c0b699426e87b5c664f6d16de` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-09-19 | 32,051 | 523.2 KB | `07d141e421ce5d59211cb1cd7d16bdf12641d3d27a930c63baef7140ddde2073` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-09-19 | 355,491 | 5.0 MB | `163d4e6a7a720d6b548bd5a003cc4662cc9c0da2b86e87ec91eb952646624134` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-09-19 | 94,960 | 1.2 MB | `e1f816408cbd485be3fec183db3990592aaf6f81ff66d9eb09af4a7596b4cbea` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-09-19 | 72,040 | 1009.7 KB | `5f8a47c85a9cd25b0943127c6372bc1f279d88aeb8047e9287e20d4514616771` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-09-19 | 254,426 | 3.5 MB | `52318e760c60cb06e2a6cd6bb1da336481a2dff6775b1bbfb7d0bac252e9a203` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-09-19 | 44,852 | 671.1 KB | `82447c27028c7b1872d44d4a6ff5c082e098f1653dd2b52d798202c98e36921f` |
