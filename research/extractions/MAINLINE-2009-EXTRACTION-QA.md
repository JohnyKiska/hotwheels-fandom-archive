# Mainline 2009: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2009/List of 2009 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `83e304779e51c9a6f6d769b33fb85f495eb3a2c1`
- File size: 693,789 bytes
- Manifest SHA-256: `17ee43beed199b209b5c738e84b71321787a94d69fa7d97c16dab6fc0fea5b28`
- Fandom revision: 811763

Machine-readable export: [MAINLINE-2009.csv](MAINLINE-2009.csv). It preserves source table index, section heading, row position, all six source columns, and raw values.

## Extraction method

Extracted all 16 product tables separately, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline series tables | 14 | 342 | 202 | 190 numeric values, 001–190 |
| Redline Exclusives + Goodyear Tire Exclusives | 2 | 12 | 12 (all repeat Mainline Toy #) | Existing numeric values |
| Total source rows | 16 | 354 | 202 | 190 numeric values |

Mainline checks:

- Collector # sequence is continuous from 001 through 190; no gaps.
- 104 Mainline rows marked `(2nd Color)`.
- 12 Treasure Hunt and 12 Super Treasure Hunt rows (Series-label counts).
- 104 distinct Toy # values occur more than once within the 342 Mainline rows; Toy # is not a unique row/release key in this year.
- No missing values in the six source columns.
- All Photo cells are empty.

Additional sections:

- Redline Exclusives: 10 rows.
- Goodyear Tire Exclusives: 2 rows.
- All 12 rows are exact six-column repeats of rows in the Mainline tables. Preserve the source section membership without creating additional unique release records.

## Interpretation notes

- 2009 demonstrates that Toy # may be shared by multiple color entries within the same annual Mainline page. Do not use Toy # alone as a unique release key.
- Collector # is a separate sequence and is continuous only through 190 for this page. Do not manufacture positions 191–250.
- The two exclusive tables repeat Mainline source rows exactly. Retain their packaging/section provenance.
- TH/STH are represented in Series text.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
