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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-09-19 | 124,388 | 1.7 MB | `7fe85b7ffbecf772ff5fcb10a4d87b12a21ff4eed6e093f201e3176ad800dcd6` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-09-19 | 76,270 | 1.0 MB | `777267d26fa5768290e6dc505a0479657f207cb55e1efe906cb2dd9116c367ff` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-09-19 | 63,600 | 862.6 KB | `50b0d397fe83b320c1f7535d3dd5a989399e0d9086f59d4fff1b185642d0c97c` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-09-19 | 649,530 | 9.2 MB | `1eae3c3eb95b152d6a5d1dbe1232c922aeb653466bc0cab459faa27dc8a07c30` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-09-19 | 45,900 | 576.9 KB | `5d0f4d5368425f025e452a57fac6e59722b381364f87af5c4d2612a13c219ee7` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-09-19 | 32,051 | 522.2 KB | `393641d6657198de89b8566012381d49efb1fcd4838c8c2dd44c6e27a1164ba8` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-09-19 | 355,491 | 5.0 MB | `07ff19bedda66297035599e9b4ba663ea84bb332b39325effbf407da5ed71a76` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-09-19 | 94,960 | 1.2 MB | `eb0988dfe966198ba0970fa5605a32dd672a3f9163a696fe1fb3fca98f0745a3` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-09-19 | 72,040 | 1008.1 KB | `e3b2d4b41536cb65de64c86a2efcf270125140610244b5caffd85898c673b898` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-09-19 | 254,426 | 3.5 MB | `c955d5d258b240a6c851bf2fb136fa31bf46ee60b907c531c91c01050f46d6b7` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-09-19 | 44,852 | 669.9 KB | `e36ef3a0bb2d89826849c7cc840e55b954104d2b68940382d3d33d30d92fd145` |
