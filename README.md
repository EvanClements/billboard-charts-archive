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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-08-15 | 124,238 | 1.7 MB | `18f7d31a7e347c07a5439d4be09d9eeebc628393ccef087f5d7cbe29ccf34086` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-08-15 | 76,070 | 1.0 MB | `dd94384f7bd627f34d0b55ee16ff688eb4d3962c3ba6453039a706ea2b65b4bd` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-08-15 | 63,100 | 859.0 KB | `52a0c213a69a22a6660a6087d8230c3cb69b74ce8425a6623ecb2e29f09930d9` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-08-15 | 648,530 | 9.2 MB | `0d1a561d8ee846194833c1916922d61750374158068110dba70e94f05d1ea921` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-08-15 | 45,600 | 574.2 KB | `da62a6816dd7a0e84d0da58019a29224899a5492637ff4125fa444e7a2819184` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-08-15 | 31,925 | 520.8 KB | `95934997896dbef18891e06aeff3621f445ee4e0fd0ae18a095a9c8f67a0c0a2` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-08-15 | 354,987 | 5.0 MB | `9970eb6d6344d62c03e5f44ab1c063a64f0a6500e51d010093806a44536585ba` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-08-15 | 94,760 | 1.2 MB | `d852b3b4b0405144e8af9902732587c8a7f213451ae7097a74127502d8a186c0` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-08-15 | 71,840 | 1006.9 KB | `30d1fffa99116b06ded24687639464c5445da0cec0b69a964daf08d29828de0b` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-08-15 | 254,175 | 3.5 MB | `d20753bbd566aeb9527805375a3952e8adc19d31d969e4c839d6f07de08ae082` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-08-15 | 44,600 | 667.5 KB | `b664338fcca6c930731b428def98e7481d8b933b218e3003c812ec6653ab018b` |
