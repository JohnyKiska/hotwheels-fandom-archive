# Mainline 2000: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2000/List of 2000 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `1a15730f64f718f37cd94244b3fad3d5d07f1b25`
- File size: 581,593 bytes
- Manifest SHA-256: `f0a544d00062e84c1be8f8b7f5cb653c7e8a3373f6c01b19b07fe9ce656170f6`
- Fandom revision: 799670

Machine-readable export: [MAINLINE-2000.csv](MAINLINE-2000.csv). It preserves table index, section heading, row position, original column count and raw headers. Optional fields are mapped by header name.

## Extraction method

Extracted all 17 product tables separately, preserving table boundaries and row order. The `2000 Hot Wheels` table uses five columns and omits Series #. The `Virtual Collection` and `Bonus Cars` tables are kept as separate source scopes.

## QA results

| Scope | Tables | Rows | Notes |
|---|---:|---:|---|
| Core annual series + 2000 Hot Wheels | 15 | 210 | 210 distinct Collector # values |
| Virtual Collection | 1 | 35 | Separate table; Series # values are alphanumeric codes |
| Bonus Cars | 1 | 4 | Toy # blank; Collector # 001–004 in separate bonus scope |
| Total source rows | 17 | 249 | 245 distinct nonblank Toy # values |

Collector # coverage:

- Across core + Virtual Collection tables, 245 distinct numeric Collector # values are represented.
- The values 147, 170, 184, 185 and 186 are not present in any of these tables.
- The 35 Virtual Collection Collector # values fill 35 positions absent from the other annual tables, but their distinct Series # codes and separate heading mean their identity/relationship must remain explicit.
- Bonus Cars reuses Collector # 001–004 but has no Toy #. Do not merge those rows into the main annual sequence.

Other checks:

- 12 Treasure Hunt rows; no Super Treasure Hunt rows.
- No `(2nd Color)` rows.
- No missing values in fields present in each table, except the four blank Toy # cells in Bonus Cars.
- The 2000 Hot Wheels table has 114 rows and a five-column schema without Series #.
- All Photo cells are empty.

## Source structure

- Tables 1–14: numbered series covering the early annual sequence through #096.
- Virtual Collection: 35 entries, Collector # values #097 and selected values through #173; Series # contains alphanumeric codes such as `LIV42DA`, not fractional series positions.
- 2000 Hot Wheels: 114 rows, five-column schema, Collector # values spanning #098–#250.
- 2000 Bonus Cars: four entries (Way 2 Fast, 1970 Mustang Mach 1, Jaguar XK8, Super Modified), Toy # blank, Collector # 001–004, separate source scope.

## Interpretation notes and unresolved questions

- Do not assume the Virtual Collection is either part of or separate from the canonical Mainline product namespace solely from its table heading. It overlaps/bridges Collector # positions in a way that needs external source verification.
- Five numeric Collector # values (147, 170, 184, 185, 186) are absent. Do not create placeholder releases without evidence.
- The 2000 Hot Wheels table has no Series # column by source design.
- Bonus Cars has blank Toy # values and reuses Collector # 001–004; preserve as separate source assertions.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
