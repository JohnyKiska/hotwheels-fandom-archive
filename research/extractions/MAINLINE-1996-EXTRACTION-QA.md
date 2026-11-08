# Mainline 1996: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1996/List of 1996 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `52edccf7b1763faf2e2c06a0c174d031a63e574b`
- File size: 498,126 bytes (Git tree size)
- Manifest SHA-256: `ecbf6317de37e3f8561a2b179406be8e8f37dcdecc85485e8595312fe77a0ade`
- Fandom revision: 800722

Machine-readable export: [MAINLINE-1996.csv](MAINLINE-1996.csv). It preserves source table index, section heading, row position, original column count, raw headers, and cell values. Optional fields are mapped by source header name.

## Extraction method

Extracted all 17 product tables and 141 source rows. Table order, section labels, and row order are retained. Navigation, category and footer tables are excluded.

## QA results

| Check | Result |
|---|---:|
| Product tables | 17 |
| Source rows | 141 |
| Unique Toy # | 136 |
| Unique Collector # values, including 000 | 136 |
| Numeric Collector # values | 132 |
| Numeric Collector # range | 182–507 (non-dense) |
| Exact duplicate source rows | 2 |
| Treasure Hunt rows | 12 |
| Bonus Cars rows | 4 |
| 1996 Hot Wheels rows | 64 |
| Rows in five-column schema without Series # | 64 |
| Series # cells containing zero-width Unicode | 4 |
| Photo cells empty | 141 / 141 |

### Duplicate source rows

The 1996 Hot Wheels table repeats two rows exactly:

- Collector #473, Toy #15963, BMW M1 appears twice.
- Collector #491, Toy #16298, Rocket Shot appears twice.

These are exact repeated source rows, not confirmed distinct releases. Both are retained in the CSV with table row positions.

### Cross-scope Toy # reuse

Three Bonus Cars share Toy # values with Treasure Hunt rows:

- Toy #15083: Custom Mustang (Bonus Cars) / Auburn 852 (Treasure Hunts).
- Toy #15076: Twin Mill (Bonus Cars) / Ferrari 250 (Treasure Hunts).
- Toy #15077: Classic Nomad (Bonus Cars) / Jaguar XJ220 (Treasure Hunts).

These are source-level cross-scope identifier collisions and must not be merged by Toy # alone.

## Table inventory

- Table 1: 1996 Model Series: 1 row
- Table 2: First Editions: 12 rows
- Table 3: Race Truck Series: 4 rows
- Table 4: Flamethrower Series: 4 rows
- Table 5: Space Series: 4 rows
- Table 6: 1996 Race Team Series II: 4 rows
- Table 7: Mod Bod Series: 4 rows
- Table 8: Dark Rider Series II: 4 rows
- Table 9: Sports Car Series: 4 rows
- Table 10: Splatter Paint Series: 4 rows
- Table 11: Street Eaters Series: 4 rows
- Table 12: Fast Food Series: 4 rows
- Table 13: Silver Series II: 4 rows
- Table 14: Fire Squad Series: 4 rows
- Table 15: Treasure Hunts: 12 rows
- Table 16: 1996 Hot Wheels: 64 rows
- Table 17: 1996 Bonus Cars: 4 rows

## Interpretation notes

- Collector #000 is used by all four Bonus Cars; retain this as a distinct Bonus Cars identifier scope.
- Numeric Collector # values are non-dense in the annual page. Do not interpret unrepresented values as missing products without external evidence.
- The 1996 Hot Wheels table uses five columns and has no Series # field; this is a source schema difference, not missing data.
- Four Series # cells contain zero-width Unicode. Preserve raw values and normalize only in derived fields.
- Exact repeated rows and cross-scope Toy # collisions are separate phenomena and must remain distinguishable.
- Fandom is a secondary source and does not independently establish Mattel release status or casting/tooling identity.
