# Mainline 2005: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2005/List of 2005 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `922d3e1d1707a18d79028d40313168948f7912c8`
- File size: 575,914 bytes
- Manifest SHA-256: `857418e237001093e5c04999b17adb6c1a505d188680942ad5eb608f8d0e611e`
- Fandom revision: 797737

Machine-readable export: [MAINLINE-2005.csv](MAINLINE-2005.csv). It preserves table index, section heading, row position, original column count, and raw source headers. Optional fields are mapped by header name.

## Extraction method

Extracted all 19 product tables separately, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Zero-width Unicode was retained.

## QA results

| Scope | Tables | Rows | Collector # |
|---|---:|---:|---:|
| Mainline tables with Series # | 18 | 202 | 001–133 and 184–187 |
| 2005 Open Stock | 1 | 86 | 134–183 |
| Total | 19 | 288 | 001–187, no gaps |

Overall checks:

- 288 source rows.
- 187 unique Toy # and 187 unique Collector # values.
- 77 Toy # values occur more than once across the source rows.
- 40 rows marked `(2nd Color)`.
- 13 Treasure Hunt rows (including the Mail-In entry); no Super Treasure Hunt rows identified.
- No missing values in the columns actually present in each table.
- All 288 Photo cells are empty.
- 135 non-empty Series # cells contain zero-width Unicode characters; these are preserved in the CSV.

## 2005 Open Stock schema

- 86 rows, Collector # 134–183.
- Header: `Toy # | Col. # | Model Name | Series | Photo`.
- Series # is absent by source design, not a missing value.
- Preserve the five-column schema and do not synthesize Series #.

## Interpretation notes

- Collector # is continuous from 001 through 187, including Open Stock 134–183.
- Toy # repeats across multiple color variants; it is not a unique row/release key.
- Open Stock is part of the annual list but has a different source schema.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
