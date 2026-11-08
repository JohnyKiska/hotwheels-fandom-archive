# Mainline 2013: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2013/List of 2013 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `adc821e992539962070987977f15fec9c8c2e889`
- File size: 827,201 bytes
- Manifest SHA-256: `6bc26729de4322560106923a19e4daa18085448bad46d98bdbad8b2bc37887d7`
- Fandom revision: 790643

Machine-readable export: [MAINLINE-2013.csv](MAINLINE-2013.csv). It preserves table index, section heading, row position, original column count and raw headers. Fields are mapped by header name.

## Extraction method

Extracted all 31 product tables independently. The 30 annual Mainline series tables use a five-column schema; the separate Kroger-exclusive Scavenger Hunt table uses six columns and includes Series #.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline series tables | 30 | 433 | 433 | 250 numeric values, 001–250 |
| Scavenger Hunts (Kroger Exclusive) | 1 | 6 | 6 | `No #` on all rows |
| Total | 31 | 439 | 439 | 251 distinct raw values including `No #` |

Mainline checks:

- All 30 Mainline tables use five columns: Toy #, Col.#, Model Name, Series, Photo.
- Series # is absent from the Mainline source schema. It is not a missing field.
- 138 rows marked `(2nd Color)`.
- 15 Treasure Hunt and 15 Super Treasure Hunt rows are identified by Series labels.
- No missing values in the five source columns.
- All Photo cells are empty.

Additional section:

- Mission Madness - Scavenger Hunts (Kroger Exclusive): 6 rows, with Series # values 1/6–6/6 and Collector # = `No #`.
- Keep this separate from the numeric Mainline Collector # sequence.

## Data-model implications

- The annual Mainline page is divided into series tables and does not provide a Series # field in those tables.
- Preserve the source header list and map optional fields by header name. Do not infer Series # from ordering or other page content.
- Scavenger Hunt rows use a distinct source scope and must not be assigned numeric Collector #.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
