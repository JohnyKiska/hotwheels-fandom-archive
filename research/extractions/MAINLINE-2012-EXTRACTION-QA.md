# Mainline 2012: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2012/List of 2012 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `80c099e16a052f566d516ef7f9ab5a0fb88d3b78`
- File size: 786,466 bytes
- Manifest SHA-256: `c6b0273581406171c5f09911b97ce676395102dacb47cf543f174471b0e41ceb`
- Fandom revision: 778347

Machine-readable export: [MAINLINE-2012.csv](MAINLINE-2012.csv). It preserves table index, section heading, row position, all six source columns and raw values.

## Extraction method

Extracted all 26 product tables separately, preserving source row order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty cells were retained.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline annual series | 23 | 387 | 387 | 247 numeric values, 001–247 |
| Windshield Banner Exclusives + Redline Exclusives | 2 | 20 | 20 (all Toy # already occur in Mainline) | Existing numeric values |
| Year of the Dragon Edition | 1 | 1 | 1 | `No #` |
| Total source rows | 26 | 408 | 388 | 248 distinct raw values including `No #` |

Mainline checks:

- Numeric Collector # values are continuous from 001 through 247; no gaps.
- 110 Mainline rows marked `(2nd Color)` (9 additional rows in the two exclusives tables also carry that label).
- 15 Treasure Hunt and 15 Super Treasure Hunt rows (Series-label counts).
- No duplicate Toy # within the 23 Mainline tables.
- 407 non-empty Series # cells contain zero-width Unicode in the source; raw values are preserved in the CSV.

Additional tables:

- Hot Wheels Windshield Banner Exclusives: 10 rows.
- Redline Exclusives: 10 rows.
- All 20 Toy # values already appear in the Mainline tables. Sixteen rows are exact six-column repeats; four rows differ in Model Name text under the same Toy #: V5473, V5615, V5651 and V5431. Preserve these section rows rather than deduplicating automatically.
- Year of the Dragon Edition: Y5852 / Rodzilla, Collector # = `No #`; Series # is blank in the source row.

## Interpretation and unresolved cases

- 2012's numeric Collector # sequence ends at 247, not 250. Do not manufacture 248–250.
- The two exclusives tables are cross-listed source sections, not 20 additional Collector # positions. Keep their packaging/section context and source row occurrences.
- The four non-identical repeated Toy # records require review: V5473 (Amazoom), V5615 ('67 Pontiac GTO (2nd Color)), V5651 (Aston Martin One-77 (3rd Color)), V5431 (Lamborghini Estoque).
- The Year of the Dragon Edition has no Collector # and a blank Series #; preserve the literal source state.
- Zero-width characters in Series # should be preserved in raw source and normalized only in derived values.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
