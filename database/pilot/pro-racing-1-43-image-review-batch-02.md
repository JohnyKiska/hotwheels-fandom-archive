# Pro Racing 1:43 image review, batch 02

Date: 2026-11-10

## Scope
- Reviewed gallery items 11-20 of 55.
- All ten assets were downloaded successfully and visually inspected from repository copies.
- Asset paths, source URLs, byte counts and SHA-256 values are recorded in `assets/pro-racing-1-43/MANIFEST.csv`.

## Visual findings
| Items | Observation | Review outcome |
|---|---|---|
| 11 | Second view of the seated red racing-driver figure. | Identity remains unresolved. |
| 12-14 | 2002 McLaren Formula 1 model: package front with Williams/Kimi markings, package reverse and model underside. | Visual group consistent with McLaren FEP sample; no exact release/variant link asserted. |
| 15-16 | Green Jaguar Formula 1 model in signed display case, plus underside view. | Consistent with signed Jaguar sample group; signatures not authenticated. |
| 17-19 | Red Ferrari Formula 1 model in desert-themed display, close-up and rear/display-base view. | Strong visual support for King of the Desert sample family; exact release provenance not independently established. |
| 20 | Close view of red Ferrari F1 car and package label referencing Michael Schumacher. | Consistent with 2003 Ferrari sample group; exact variant/release not asserted. |

## Data handling
- Items 11-20 now have `review_status=reviewed` and `visual_inspection_status=inspected`.
- No candidate fields were promoted to canonical relations.
- Items 21-55 remain untouched.

## QA
- 10/10 assets in this batch have `download_status=downloaded`.
- Images are small source thumbnails (approximately 185 px wide); tiny printed details and signatures are not treated as verified.
