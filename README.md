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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-08-29 | 124,298 | 1.7 MB | `62e13f95ccccc2e266c617d9a0a05f551d1df43bf5cb61881754846258731df6` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-08-29 | 76,150 | 1.0 MB | `d0ba70efdc4f9267ae3806d4c5e3f92cec62a2a7efe78116b0d2e8604dc00427` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-08-29 | 63,300 | 861.8 KB | `6c79e8cfe0745f34f60751a01544c0e22774c8609e0190b99a21867621c4e270` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-08-29 | 648,930 | 9.2 MB | `a0b6df83411ab3d531d079a767eec94a51f7c40141b86ed4c9a0c2b1eb8c74b3` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-08-29 | 45,720 | 575.0 KB | `0959faa2e0351f7578abe0b4d49cae779e249bcd349f23e2c7e96e47c645a354` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-08-29 | 31,975 | 521.2 KB | `2aa2af72d753a5dea6f8bbeab2fd809118f978acf022cf1c9a0de9c6b6d712e5` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-08-29 | 355,190 | 5.0 MB | `dae96ba6449bdf5aa8f0f793a1b578313d1f50b95e7655d503e91aa84e1b051e` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-08-29 | 94,840 | 1.2 MB | `432808253c942714dc5bd4ac5bdf1ba1e29c02ada2e0eb8d2308a025b1baff76` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-08-29 | 71,920 | 1007.7 KB | `7e136cf0f38c0e4dc426e3a3c313b158bfa05b96a40b078ba2b8938e5fb1180c` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-08-29 | 254,276 | 3.5 MB | `48299028e10d5ef967756dc4d2c4a4e04a462ae7978f206f974957c46c7e8d56` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-08-29 | 44,700 | 668.4 KB | `f9b312c50b6f9e1a862a0af6dfa8cc0d315c23f18353384c17b5d068c9f16d81` |
