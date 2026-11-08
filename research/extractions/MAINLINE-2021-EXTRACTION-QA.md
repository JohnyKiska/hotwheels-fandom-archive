# Mainline 2021: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2021/List of 2021 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `7371922799d2da7fc13b6f2f2cd66cc9daec9f8d`
- File size: 822,471 bytes
- Manifest SHA-256: `61b1338a674080706dbd89ba3e4635272ce0979861f112050f36f1e1df3186ca`
- Fandom revision: 797153

Machine-readable export: [MAINLINE-2021.csv](MAINLINE-2021.csv). The export preserves source table index, section heading, row order, all six cells, and the original Collector-column label.

## Extraction method

Extracted both product tables separately, preserving source row order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Scope | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|
| Mainline annual table | 447 | 447 | 250 numeric values, 001–250 |
| Hot Wheels id table | 8 | 8 | `No #` on all 8 rows |
| Total source rows | 455 | 455 | 251 distinct raw values including `No #` |

Mainline table checks:

- 134 rows marked `(2nd Color)`.
- 15 Super Treasure Hunt rows and 15 Treasure Hunt rows (Series-label counts).
- No missing Toy #, Collector #, Model Name, Series or Series #.
- All 447 Photo cells are empty.
- 161 numeric Collector # values have multiple rows; Collector # is not a unique release key.

Hot Wheels id table checks:

- 8 rows, Toy # GTD61–GTD64 with additional products in the same source table.
- Collector # is recorded as `No #`; these rows must not be forced into the numeric Mainline Collector # namespace.
- Keep Hot Wheels id as a separate table/program scope, not as eight additional entries in the 001–250 annual Mainline sequence.

First Mainline row: `GRX19 | 001 | The Nash | HW Dream Garage New for 2021! | 2/5`.

Last Mainline row: `GTD13 | 250 | Shelby Cobra 427 S/C | Muscle Mania Super Treasure Hunt | 10/10`.

## Interpretation notes

- Toy # is unique within each table in this source snapshot, but that does not establish universal uniqueness across years/programs.
- Collector # is scoped to the annual Mainline table. The `No #` values in Hot Wheels id are retained literally and kept in a distinct scope.
- Color labels and TH/STH series labels are source assertions; they do not establish casting identity.
- The Photo column is empty in every row.
- This archived Fandom page does not independently verify Mattel release status or tooling identity.
