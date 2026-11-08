# Mainline 2002: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2002/List of 2002 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `04b976fdfaf57e33c688e76e5171b36b83844d4e`
- File size: 604,441 bytes
- Manifest SHA-256: `168684b33bc0a496eb737cbbc9cffb70eebeaad6916f23bd185b0466a733a9dc`
- Fandom revision: 777856

Machine-readable export: [MAINLINE-2002.csv](MAINLINE-2002.csv). It preserves source table index, section heading, row position, original column count and raw headers. Optional fields are mapped by header name.

## Extraction method

Extracted all 19 product tables separately. The 2002 Hot Wheels table (table 18) uses five columns and omits Series #. The Final Run table (table 19) is a separate program table and is not part of the annual Mainline Collector # sequence.

## QA results

| Scope | Tables | Rows | Identifier scope |
|---|---:|---:|---|
| 2002 annual Mainline | 18 | 240 | Collector # 001–240, continuous |
| 2002 Final Run | 1 | 3 | Separate Final Run scope; Series # 1/12, 4/12, 6/12 |
| Total source rows | 19 | 243 | Do not combine identifiers across scopes |

Mainline checks:

- 240 rows, 240 unique Collector # values, 240 unique Toy # values.
- 12 Treasure Hunt rows.
- No `(2nd Color)` labels or Super Treasure Hunt rows found.
- The 2002 Hot Wheels table has 126 rows and a five-column schema without Series #; this is not missing data.
- No missing values in the fields present in each table.
- Photo cells are empty.

Final Run rows:

- 3 rows: Porsche 928 (001), Ferrari 308 (004), Firebird Funny Car (006).
- These use Final Run Series # values 1/12, 4/12 and 6/12.
- Their Collector # values overlap with the annual Mainline numbering. Treat Final Run as a separate program/identifier namespace, not as additional Mainline positions.

## Interpretation notes

- Annual Mainline Collector # sequence is 001–240.
- Do not combine Final Run Collector # with annual Mainline Collector #; scope identifiers by program/year/source.
- Preserve the five-column 2002 Hot Wheels schema without Series #.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
