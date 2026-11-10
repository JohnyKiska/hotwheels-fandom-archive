# Pro Racing 1:43 image review, batch 01

Date: 2026-11-10

## Scope
- Reviewed gallery items 1-10 of 55.
- Downloaded image assets were retrieved from the repository and visually inspected.
- All ten downloads succeeded; original source URLs, local paths, byte counts and SHA-256 hashes are recorded in `MANIFEST.csv`.

## Visual findings
| Gallery items | Observation | Review outcome |
|---|---|---|
| 1-3 | Red Formula-style car(s) in display packaging; Ferrari branding visible. Item 3 shows an F1 2000 marking on the base/package. | Visual evidence recorded; exact product/release mapping not asserted. |
| 4-6 | Silver/white Formula-style car in illustrated/display packaging. | Ford attribution and exact model cannot be confirmed from the small images. Keep unresolved. |
| 7-9 | Red Formula-style car(s) in Williams-branded display packaging; Williams F1 marking visible. | Family association supported visually; exact model/release not asserted. |
| 10 | Separate seated red racing-driver figure in helmet and suit. | Ancillary figure; identity unresolved. |

## Data handling
- Items 1-10 in `pro-racing-1-43-image-review.csv` now have `review_status=reviewed` and `visual_inspection_status=inspected`.
- Candidate entity fields were not promoted to canonical links.
- No casting, variant, release, or assortment records were created from visual appearance alone.
- Items 11-55 remain untouched and await image retrieval and review.

## QA
- 10/10 assets present in the manifest with `download_status=downloaded`.
- The review is limited by source thumbnails resized to approximately 185 px wide. Fine tampo, base text and small packaging details are not treated as confirmed.
