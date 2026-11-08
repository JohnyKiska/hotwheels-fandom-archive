# Mainline 2011: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2011/List of 2011 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `a7bc93b9896f6a8c8d6ca25ac0eaa8cd87984c15`
- File size: 787,898 bytes
- Manifest SHA-256: `cfd318bd11e0585e52cb68ebd21ee5f975518780953fd9fdac0f27ba8b0fa159`
- Fandom revision: 806210

Machine-readable export: [MAINLINE-2011.csv](MAINLINE-2011.csv). It preserves source table index, section heading, row position, all six source columns, and raw values.

## Extraction method

Extracted all 23 product tables separately, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline series tables | 21 | 429 | 429 | 244 numeric values, 001–244 |
| Windshield Banner Exclusives + Redline Exclusives | 2 | 20 | 20 (all repeat Mainline Toy #) | Existing numeric values |
| Total source rows | 23 | 449 | 429 | 244 numeric values |

Mainline checks:

- Collector # sequence is continuous from 001 through 244; no gaps.
- The source sequence ends at 244. Do not create 245–250.
- 119 Mainline rows marked `(2nd Color)`.
- 15 Treasure Hunt and 15 Super Treasure Hunt rows (Series-label counts).
- No missing values in the six source columns.
- All Photo cells are empty.

Additional sections:

- Hot Wheels Windshield Banner Exclusives: 10 rows.
- Redline Exclusives: 10 rows.
- All 20 rows repeat Toy # values already present in Mainline; all 20 are exact six-column row repeats. Preserve the two section contexts as source appearances, but do not create new releases by counting them as additional products.

## Interpretation notes

- 2011 numeric Collector # sequence ends at 244, not 250.
- The two exclusives tables are separate source sections but their rows are exact repeats of Mainline rows in this archived page. Retain source provenance while linking them to the same source-row content; do not silently discard the section membership.
- Toy # is unique in the 21 Mainline tables but repeats in the two cross-listed exclusives sections.
- TH/STH are indicated in Series text for this page.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
