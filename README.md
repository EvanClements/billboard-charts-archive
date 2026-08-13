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
| Adult Contemporary | [`data/adult-contemporary.parquet`](data/adult-contemporary.parquet) | 1961-07-22 | 2026-08-08 | 124,208 | 1.7 MB | `2c4dbc676cd0d9d95ce816c78e4151fd33585a0f121382dd5ae8b4e24568888b` |
| Alternative Airplay | [`data/alternative-airplay.parquet`](data/alternative-airplay.parquet) | 1988-09-10 | 2026-08-08 | 76,030 | 1.0 MB | `09b553d7b4f668047047132fb879c2bd8d5d813f78c9835353be11860772d3ed` |
| Billboard Artist 100 | [`data/artist-100.parquet`](data/artist-100.parquet) | 2014-07-19 | 2026-08-08 | 63,000 | 858.0 KB | `5553af209ff37d4d65024ee3c44c2be95088ac920394b955d3d2582cf4cf4e0e` |
| Billboard 200™ | [`data/billboard-200.parquet`](data/billboard-200.parquet) | 1963-01-05 | 2026-08-08 | 648,330 | 9.2 MB | `076cac1545c274f912242630de77b2ca463ba44d651fc1fde7344aec85b3f071` |
| Country Airplay | [`data/country-airplay.parquet`](data/country-airplay.parquet) | 2012-01-21 | 2026-08-08 | 45,540 | 572.8 KB | `d78622ac71a4e575e760388334b6cfe4c6559f22650b4756aabf55af9e14f4d3` |
| Hot Dance/Electronic Songs | [`data/dance-electronic-songs.parquet`](data/dance-electronic-songs.parquet) | 2013-08-10 | 2026-08-08 | 31,900 | 520.2 KB | `cd486be959bf0175998fc4d883e9f0946b81791375d58a153bf01adbc4bb740f` |
| Billboard Hot 100™ | [`data/hot-100.parquet`](data/hot-100.parquet) | 1958-08-09 | 2026-08-08 | 354,887 | 5.0 MB | `2857c9084c377863e48ee5e6c8099cc590c14fdfe27452a33e439d45db325b46` |
| Mainstream Rock Airplay | [`data/hot-mainstream-rock-tracks.parquet`](data/hot-mainstream-rock-tracks.parquet) | 1981-03-21 | 2026-08-08 | 94,720 | 1.2 MB | `e935cbc2dc6366f8441e8fb2b06913122c942e93e6ceff9c76fcc166e97112b6` |
| Pop Airplay | [`data/pop-songs.parquet`](data/pop-songs.parquet) | 1992-03-21 | 2026-08-08 | 71,800 | 1006.3 KB | `1a8af188ac7211da83d40e0679c242561a1776fb95299f497d5b0d19e27c7d23` |
| Hot R&B/Hip-Hop Songs | [`data/r-b-hip-hop-songs.parquet`](data/r-b-hip-hop-songs.parquet) | 1958-10-25 | 2026-08-08 | 254,125 | 3.5 MB | `0a74de9c836ae2ab06b786e5ae77f056a9e9b0731f8e69caca818a10cb87cc15` |
| Hot Rock & Alternative Songs | [`data/rock-songs.parquet`](data/rock-songs.parquet) | 2009-07-18 | 2026-08-08 | 44,550 | 667.0 KB | `e8e08b46e740cfcf7c9464b041625d6149e54a31c12de15f3070d8981809eb83` |
