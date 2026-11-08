# Mainline 2015: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2015/List of 2015 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `945d2bf5200a935277f529f2dd0ea73796de2840`
- File size: 814,789 bytes
- Manifest SHA-256: `447748a8a71ea464382619a62ae1d1204b1c2bd719ab46b5ee4891389f658787`
- Fandom revision: 790646

Machine-readable export: [MAINLINE-2015.csv](MAINLINE-2015.csv). It preserves table index, section heading, row order, original column count and raw source headers. The export maps fields by header name, not by fixed column position.

## Extraction method

Extracted all 35 data tables independently. Each table's own header determines the mapping of Toy #, Collector #, Model Name, Series, Series #, and Photo. This is important because the annual Mainline tables use a five-column schema and do not contain a Series # column, while the additional Scavenger Hunt table has six columns.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline series tables | 34 | 433 | 433 | 250 numeric values, 001–250 |
| Scavenger Hunt | 1 | 4 | 4 | `No #` on all rows |
| Total | 35 | 437 | 437 | 251 distinct raw values including `No #` |

Mainline checks:

- All 34 Mainline tables use exactly five columns: Toy #, Col.#, Model Name, Series, Photo.
- Series # is **not present** in the Mainline table schema. It is not a missing value and must not be synthesized from other fields.
- 142 rows are marked `(2nd Color)`.
- 15 Treasure Hunt and 15 Super Treasure Hunt rows are identified in Series labels.
- No missing values in the five source columns.
- All Photo cells are empty.

Additional section:

- Scavenger Hunt: 4 rows; its table has six columns, including Series #.
- All four rows have Collector # = `No #`. Preserve this separate source scope.

## Data-model implications

- Do not assume all annual Mainline pages share a fixed six-column schema.
- Preserve the source header list and column count per table/page; map optional fields by header label.
- Absence of Series # in the 2015 Mainline tables is a schema difference, not an extraction defect.
- Keep Scavenger Hunt separate from numeric Mainline Collector # records.
- Toy # is unique within this page's extracted rows, but this does not establish global uniqueness across years/programs.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
