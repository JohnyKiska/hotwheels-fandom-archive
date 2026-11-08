# Mainline 2023: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2023/List of 2023 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `3af550f4912fd6d177848206aa583abaa75a00ca`
- File size: 830,879 bytes
- Manifest SHA-256: `ab3c9a92ac300bbb0e437bfb09da3e3254952f135e21145683ac1fbe6cd91599`
- Fandom revision: 772739

Machine-readable export: [MAINLINE-2023.csv](MAINLINE-2023.csv).

## Extraction method

Extracted the first and only product data table, preserving source row order and all six source columns: Toy #, Col.#, Model Name, Series, Series #, Photo. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Check | Result |
|---|---:|
| Product data tables | 1 |
| Data rows | 445 |
| Unique Toy # | 445 |
| Duplicate Toy # | 0 |
| Unique Collector # | 250 |
| Collector # range | 001–250 |
| Collector # values with multiple rows | 165 |
| Rows marked `(2nd Color)` | 141 |
| Super Treasure Hunt rows | 15 |
| Treasure Hunt rows excluding STH | 15 |
| Missing Toy #, Collector #, Model Name, Series or Series # | 0 |
| Photo cells empty | 445 / 445 |
| Distinct raw Series labels | 138 |

First row: `HKG27 | 001 | Volvo P1800 Gasser | HW Dream Garage New for 2023! | 1/5`.

Last row: `HKG70 | 250 | McLaren Solus GT | HW Exotics New for 2023! | 10/10`.

## Interpretation notes

- Toy # is unique within this extracted 2023 table; this does not establish universal uniqueness across years or source scopes.
- Collector # is not a unique row/release key. 165 values have multiple rows, including color variants and special treatments.
- The 141 `(2nd Color)` labels are retained as source text and do not independently prove casting identity.
- TH and STH are row counts derived from Series labels.
- Photo is empty in all source rows, which reflects the source table.
- This archived Fandom list does not independently verify Mattel release status or tooling identity.
