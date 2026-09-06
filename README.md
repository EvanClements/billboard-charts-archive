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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-09-05 | 124,328 | 1.7 MB | `930ca64efac8f60e4595ce10ebcb22e72c862d755cfb767c9b6afaa08d8b4f30` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-09-05 | 76,190 | 1.0 MB | `b72ddd3727e14c6f40ed6ef6ed62e2cfcf5f40d03a9ad26381fa9214a6eaaee4` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-09-05 | 63,400 | 863.1 KB | `1eaf5ee945dd69e9a685811c6894685b9adf0db87a7d7e6d890fd78a14a1cf12` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-09-05 | 649,130 | 9.2 MB | `1f3165558e5d25f27d55da829512fbdb06b5d445510b8e462c24ec67976dd32f` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-09-05 | 45,780 | 575.4 KB | `d8124854f5c872f8cbe0dafafe32c24bf83453dc503cdabbaf3c735c3310c079` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-09-05 | 32,000 | 521.3 KB | `bcc4693737e1cba2aeba7d7a304df3db67eab4e453aa6aca3f6172c0eacbcfd1` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-09-05 | 355,291 | 5.0 MB | `3fdf75e64a186a50681a22af640b9a782a1702789bbcaeea5bc70fcdcd9c624a` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-09-05 | 94,880 | 1.2 MB | `ab5bed9970b5a602c95615b40576fe32c6ca59fac30c2c1a7d9ace80e1adb9af` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-09-05 | 71,960 | 1008.8 KB | `31d962e79ef1e595de01e2bacefde701e819cfe0201bd3f24e7b022dfd722789` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-09-05 | 254,326 | 3.5 MB | `9359000499db82811fdd4bf4d9fcfb1ed7c89d20cc6ac0136e6934538782f507` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-09-05 | 44,752 | 668.8 KB | `85984046fdada49fed2783821544c8f414861875db63d978f625cdb0cda05cb7` |
