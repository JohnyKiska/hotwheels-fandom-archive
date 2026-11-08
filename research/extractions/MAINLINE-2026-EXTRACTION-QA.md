# Mainline 2026: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2026/List of 2026 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `7861f85d0d1eed1238423d1c31f803f8e330c79d`
- File size: 811,725 bytes
- Manifest SHA-256: `2ba3b09c10aa7779630921628ea03efa265a6d1c0110038a4c2d766f3c88d0cd`
- Fandom revision: 816337

Machine-readable export: [MAINLINE-2026.csv](MAINLINE-2026.csv).

## Extraction method

Extracted the first and only product data table in the archived HTML. Preserved the source row order and six source columns: Toy #, Col.#, Model Name, Series, Series #, Photo. HTML tags were removed from cell text, common HTML entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Check | Result |
|---|---:|
| Product data tables | 1 |
| Data rows | 440 |
| Unique Toy # | 440 |
| Duplicate Toy # | 0 |
| Unique Collector # | 250 |
| Collector # range | 001–250 |
| Collector # values with multiple rows | 163 |
| Collector # values with 3 rows | 27 |
| Rows marked `(2nd Color)` | 137 |
| Super Treasure Hunt rows | 15 |
| Treasure Hunt rows excluding STH | 15 |
| Missing Toy #, Collector #, Model Name, Series or Series # | 0 |
| Photo cells empty | 440 / 440 |
| Distinct raw Series labels | 126 |

First row: `JJJ02 | 001 | Mazda MX-5 Miata | HW Dream Garage | 1/5`.

Last row: `JJH78 | 250 | Porsche 908-3 | Cool Classics New for 2026! | 10/10`.

## Interpretation notes

- Toy # is unique within this extracted 2026 table, but this does not establish a universal uniqueness rule across years or source scopes.
- Collector # is not a unique row/release key: 163 values have multiple rows, including color variants and special treatments.
- The 137 `(2nd Color)` labels are preserved as source text and should not be used alone to infer casting identity.
- TH and STH are counts of rows identified by their Series labels, not necessarily counts of distinct castings.
- Photo is empty in every source row; this is not an extraction failure.
- The archived Fandom list does not independently establish Mattel production/release status or tooling identity.
