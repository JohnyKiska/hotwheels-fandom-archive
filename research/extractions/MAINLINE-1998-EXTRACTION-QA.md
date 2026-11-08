# Mainline 1998: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1998/List of 1998 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `25bb3ec20a3ce5f3679f09b9b244fcb2024f3ebf`
- File size: 539,886 bytes
- Fandom revision: 811155
- Manifest SHA-256: `fada52789146ec7265cdded7c24e0e8df3ee5eb0798ecb959a0aeb744dc7b5fa`

Machine-readable export: [MAINLINE-1998.csv](MAINLINE-1998.csv). It preserves table index, section heading, source header list, raw row cell count, and all source values. Where the source row omits a trailing empty Photo 2 cell, the CSV records the raw cell count and pads the optional trailing field as empty.

## Extraction method

Extracted all 16 product tables independently. The 1998 Hot Wheels table uses five columns and omits Series #. Four tables declare a seventh `Photo 2` column; some rows in two of those tables omit the trailing empty cell. The Flyin' Aces header contains the source typo `Serie s`, which is preserved in Raw source headers while mapped to the Series field in the derived export.

## QA results

| Scope | Tables | Rows | Identifier scope |
|---|---:|---:|---|
| 1998 annual numbered list | 15 | 185 | 184 distinct numeric Collector # values |
| 1998 Bonus Cars | 1 | 4 | Collector # 001–004 in separate bonus scope |
| Total source rows | 16 | 189 | Preserve both scopes |

Annual numbered list checks:

- 185 rows, 184 unique Toy # values and 184 unique Collector # values.
- Collector # values span 633–908; 92 numeric values in that interval are not represented on this page.
- One repeated Collector # group: #780, Toy #19949 ('58 Corvette), appears twice in the 1998 Hot Wheels table.
- 12 Treasure Hunt rows.
- No `(2nd Color)` or Super Treasure Hunt rows identified.
- 1998 Hot Wheels table: 85 rows, five-column schema without Series #.
- All Photo and Photo 2 fields are empty.

Bonus Cars:

- Four rows: Firebird Funny Car (#001), '80s Camaro (#002), Custom Corvette Convertible (#003), Speed Machine (#004).
- Toy # is blank for the last two rows. Keep this separate from the annual numbered list.

## Table structure

- First Editions: 40 rows, Collector #637–684.
- Treasure Hunts: 12 rows, Collector #749–760.
- Twelve themed series tables follow, including Tattoo Machines, Techno Bits, Tropicool, Low 'N Cool, Biohazard, Dash 4 Cash, Race Team IV, Artistic License, Mixed Signals, Flyin' Aces, Sugar Rush and Tech Tones.
- 1998 Hot Wheels: 85 rows, Collector # range 643–908, five-column schema.
- Bonus Cars: separate four-row table.

## Interpretation notes

- Collector # is not a dense sequence in this page. The 92 unrepresented numbers between 633 and 908 are coverage observations, not automatically missing products or cancelled releases.
- Collector #780 / Toy #19949 appears twice; retain both source row occurrences and investigate whether this is a page duplicate.
- Preserve Photo 2 as an optional source field, even though its cells are empty in this snapshot.
- Preserve the literal header typo `Serie s` in provenance; use normalized field mapping only as a derived representation.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
