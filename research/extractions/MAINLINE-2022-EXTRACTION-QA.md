# Mainline 2022: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2022/List of 2022 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `556f1639e79f5531f1f57a8688c0913bca66db48`
- File size: 815,188 bytes
- Manifest SHA-256: `7d9bd56349be291743e9340219a5b1018ad47643d4998381356c5114dcee4a`
- Fandom revision: 797387

Machine-readable export: [MAINLINE-2022.csv](MAINLINE-2022.csv).

## Extraction method

Extracted the first and only product data table, preserving source row order and all six source columns: Toy #, Col.#, Model Name, Series, Series #, Photo. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Check | Result |
|---|---:|
| Product data tables | 1 |
| Data rows | 447 |
| Unique Toy # | 447 |
| Duplicate Toy # | 0 |
| Unique Collector # | 250 |
| Collector # range | 001–250 |
| Collector # values with multiple rows | 167 |
| Rows marked `(2nd Color)` | 142 |
| Super Treasure Hunt rows | 15 |
| Treasure Hunt rows excluding STH | 15 |
| Missing Toy #, Collector #, Model Name, Series or Series # | 0 |
| Photo cells empty | 447 / 447 |
| Distinct raw Series labels | 148 |

First row: `HCT05 | 001 | 1970 Pontiac Firebird | HW Dream Garage New for 2022! | 1/5`.

Last row: `HCW29 | 250 | '72 Ford Gran Torino Sport | Muscle Mania | 10/10`.

## Interpretation notes

- Toy # is unique within this extracted 2022 table; this does not establish universal uniqueness across years or source scopes.
- Collector # is not a unique row/release key. 167 values have multiple rows, including color variants and special treatments.
- The 142 `(2nd Color)` labels are retained as source text and do not independently prove casting identity.
- TH and STH are row counts derived from Series labels.
- Photo is empty in all source rows, which reflects the source table.
- This archived Fandom list does not independently verify Mattel release status or tooling identity.
