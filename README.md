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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-08-22 | 124,268 | 1.7 MB | `fa7090dcccf4dc8da2f9491c2f8ae2aabac0870d93b25f0d94d70219c72390d2` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-08-22 | 76,110 | 1.0 MB | `bd9ff52b6bbf33db92046b9744762e7aabea65c50a3c0d141ca64af8820ad2b3` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-08-22 | 63,200 | 860.0 KB | `82e3f6caaa1707ea464a2e306720e2d811cda00f8453a503977e216a8f3cb9e9` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-08-22 | 648,730 | 9.2 MB | `ba3a9b1250eca87dd4eb7d70e20ba112f66c30b24c04356ce30daa7dad4691a1` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-08-22 | 45,660 | 574.7 KB | `32a0a6b71c02c6a7770ee2e4f1a5d30dc305cebd7f25c005f355eadb6c358675` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-08-22 | 31,950 | 521.0 KB | `09ee5504091cdc8d73d0764c9cf4ce2e1907bf68d157921ba52a5f916ad0f5a7` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-08-22 | 355,087 | 5.0 MB | `6283e719787628df85a8eee14c75b9479db4e3061b712e2cc4d8e2fa1ecaacdb` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-08-22 | 94,800 | 1.2 MB | `2e85d7f4a073d06025923b2ac7c2ca3cfc3556c9379f4e26834905192d9116ac` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-08-22 | 71,880 | 1007.4 KB | `9ce29dd15e7c579d0f00b14ef0471ca9df7b725b69d242b06a143956c6e4d985` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-08-22 | 254,225 | 3.5 MB | `8a2427de62d8c97544288d6115f035b00a7d01cf41beb010a6eb8a97c4a5f8d3` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-08-22 | 44,650 | 667.9 KB | `38163bca6edd92e4a101e4f73b7d394ff17ca48e3addd50adbdb8cc301b2f929` |
