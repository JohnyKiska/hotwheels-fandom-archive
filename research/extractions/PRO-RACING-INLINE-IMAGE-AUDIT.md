# Pro Racing inline image audit (1997, 2001, 2003–2005)

Date: 2026-11-10

## Scope and method

Inspected the archived source HTML for the five annual Pro Racing pages classified `NO_GALLERY` in `research/galleries/GALLERY-SCAN.csv`. Compared every HTML `<img>` element with the existing annual product extraction CSVs, including `cell_image_metadata_json` and `raw_row_html`.

Source pages and blob SHAs:

| Year | Source HTML blob SHA | HTML img elements | Inside product tables | Outside tables |
|---|---|---:|---:|---:|
| 1997 | `17fb275932b3e7ec349c869b1e62f14995bbaac8` | 162 | 156 | 6 |
| 2001 | `9011f6900c3841b1c467b52e7fc1aa0bf7480daa` | 100 | 94 | 6 |
| 2003 | `79b5c55a7be437c2229f933848e66b400d351db0` | 145 | 139 | 6 |
| 2004 | `e2ed0061bb2b378d92a03eaa18f720d93a688c0b` | 76 | 70 | 6 |
| 2005 | `a2e39220a14c4a97b56cf98098c9416483823703` | 44 | 38 | 6 |
| **Total** | | **527** | **497** | **30** |

## Findings

- All 497 image elements within product tables are already retained by the corresponding annual extraction CSVs. The image attributes are represented in `cell_image_metadata_json`, and their original context is preserved in `raw_row_html`.
- The source/CSV image-element counts reconcile exactly: each existing CSV contains two serialized copies of each table image's `data-image-name` attribute (one in cell metadata and one in raw row HTML), giving 156, 94, 139, 70, and 38 distinct image elements respectively.
- The six images outside tables on each page are site/community header and Fandom footer branding assets, not article product photography.
- No additional article-body inline images were found outside the already-extracted product tables on these five pages.
- The five pages remain correctly classified `NO_GALLERY`: this status concerns dedicated Gallery containers only and does not mean that the page has no images.

## Disposition

No new image-extraction CSV was created and no rows were added to `GALLERY-EXTRACTION.csv`. Creating a second image stream for the 497 table images would duplicate evidence already preserved in the product extraction CSVs. The proposed Inline Image extraction task for these five pages is therefore closed as **already covered by existing table extraction; no additional article-body images found**.

Future image work should focus on pages where article-body images are not contained in extracted product-table rows, and should explicitly exclude site chrome, navigation, and footer assets.
