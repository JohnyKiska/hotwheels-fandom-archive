# Mainline 1999: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1999/List of 1999 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `caa991206ebce8c649ed27b27d2316e15da49249`
- File size: 551,309 bytes
- Manifest SHA-256: `efd9a11187058939bb2530630bb81df3f038c7585e92ab5907dcb454d4c15f00`
- Fandom revision: 799669

Machine-readable export: [MAINLINE-1999.csv](MAINLINE-1999.csv). It preserves table index, section heading, row position, original column count and raw headers.

## Extraction method

Extracted all 17 product tables separately. The 1999 Hot Wheels table uses five columns and omits Series #. Final Run and Bonus Cars are retained as separate source scopes.

## QA results

| Scope | Tables | Rows | Identifiers |
|---|---:|---:|---|
| 1999 annual numbered list | 15 | 196 | Collector # 649–1121, non-dense |
| 1999 Final Run | 1 | 12 | Collector # blank; Series # 01/12–12/12 |
| 1999 Bonus Cars | 1 | 4 | Toy # blank; Collector # 001–004 in bonus scope |
| Total | 17 | 212 | Three distinct scopes |

Annual numbered list checks:

- 196 rows, 196 unique Toy #, 196 unique Collector #.
- Collector # values span 649–1121, but 277 numeric values in that interval are not represented on this page. Do not treat these automatically as missing products; they may belong to other product scopes or be unused numbers.
- 12 Treasure Hunt rows.
- No `(2nd Color)` or Super Treasure Hunt rows identified.
- The 1999 Hot Wheels table has 109 rows and a five-column schema without Series #.
- No repeated Toy # or Collector # within the 196 numbered-list rows.

Final Run:

- 12 rows; all Collector # cells blank, Series # 01/12–12/12.
- Keep Final Run separate from the annual numbered list.

Bonus Cars:

- Four rows: '56 Flashsider, Shock Factor, Buick Wildcat, Power Pipes.
- Toy # blank; Collector # 001–004. Keep as separate Bonus Cars scope, not annual #001–004.

## Table structure

- 1999 First Editions: Collector #649–926, 26 rows.
- 1999 Treasure Hunts: #929–940, 12 rows.
- Series tables: #941–988, 49 rows, including X-Ray Cruiser's 1A/4 and 1B/4 labels.
- 1999 Hot Wheels: 109 rows, Collector #991–1121, five-column schema.
- Final Run and Bonus Cars have independent identifier behavior.

## Interpretation notes

- The 1999 annual Collector # system is not a 001-based annual sequence. Preserve the literal numeric values and scope.
- The 277 unrepresented numbers between 649 and 1121 are a coverage question, not an automatic list of cancelled or missing products.
- Do not infer Series # for 1999 Hot Wheels.
- Do not infer Toy # for Bonus Cars or Collector # for Final Run.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
