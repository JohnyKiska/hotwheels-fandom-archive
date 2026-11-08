# Mainline 2003: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2003/List of 2003 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `3abfa21a2eef023d7cf0f278cd90f1a7df1a25b6`
- File size: 580,483 bytes
- Manifest SHA-256: `6f839a185736bbdcbda79b428e53b4d53eca1690e366d638dde9fb2cfc438e71`
- Fandom revision: 797937

Machine-readable export: [MAINLINE-2003.csv](MAINLINE-2003.csv). It preserves table index, section heading, row position, original column count, and raw source headers. Optional fields are mapped by header name.

## Extraction method

Extracted all 22 product tables independently. The 2003 Hot Wheels table (table 21) uses five columns and omits Series #. All other tables use six columns. Source row order and table boundaries are retained.

## QA results

| Check | Result |
|---|---:|
| Product tables | 22 |
| Source rows | 222 |
| Unique Toy # | 220 |
| Unique Collector # | 220 |
| Collector # range | 001–220, no gaps |
| Rows marked `(2nd Color)` | 1 |
| Rows marked `(3rd Color)` | 1 |
| Treasure Hunt rows | 12 |
| Missing values in fields present in each table | 1 blank Series # |
| Photo cells empty | 222 / 222 |

The only repeated Collector # group is #035, with three rows sharing Toy #56391: Boom Box, Boom Box (2nd Color), and Boom Box (3rd Color). This is a documented multi-color group, not three Collector # positions.

## Table structure

- Treasure Hunts: Collector #001–012.
- 2003 First Editions: 44 rows across 42 Series # positions (013–054); #035 has three color entries.
- Wild Wave through Sega Games: series tables covering #055–114.
- Alt Terrain, Pride Rides, Roll Patrol, Track Aces, Wastelanders, Work Crewsers and Final Run cover later positions.
- 2003 Hot Wheels: 32 rows, five-column schema, no Series # column. It contributes positions among #115–220 not represented by the other series-specific tables.
- One Pride Rides row, Sonic Special (Collector #207), has a genuinely blank Series # in a table where the column exists. Preserve it as a source-level blank.
- One Roll Patrol row uses literal Series # `Unnumbered`; preserve that string rather than coercing to blank or zero.

## Interpretation notes

- Numeric Collector # sequence is continuous 001–220.
- Do not treat the 2003 Hot Wheels table's absent Series # column as missing data.
- The #035 Boom Box color entries share both Toy # and Collector #; preserve each source row and its color label.
- The 2003 page uses a five-column table schema alongside six-column tables in the same year. Preserve table-level schema.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
