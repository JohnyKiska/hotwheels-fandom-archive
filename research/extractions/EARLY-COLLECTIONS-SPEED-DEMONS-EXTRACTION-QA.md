# Speed Demons extraction QA

## Source
- File: `Early Collections/Speed Demons _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `bf6c7dca8fae920b5c79db2c787fd3f70460b900`
- Manifest SHA-256: `6AB1727440FE886C5BAD79754FB86AFF03AE691F9C1E61851544F0C4E5746898`
- Source size: 356,322 bytes (manifest); extracted HTML: 356,312 characters.
- Fandom revision ID: 726384.

## Extraction
- 2 product tables, 22 product rows.
- Table 1: 6 rows, 9 columns; section heading: `1986 Original Card`.
- Table 2: 16 rows, 10 columns; section heading: `1987 - 1989 Card`.
- The two source schemas differ: the second table includes a `Year` column.
- 0 standard Wikia gallery items. Loose and carded images are embedded in table cells and are retained as cell-level image metadata.
- 22 total CSV records. Source order, raw cell values/HTML, links, image filenames, keys and URLs retained.

## QA observations
- Toy # populated: 22/22; blank: 0.
- Distinct populated Toy #: 11.
- Repeated Toy # groups: [["2057",2],["2058",3],["2059",3],["2060",2],["2061",2],["2062",4],["4389",2]].
- Distinct model-name labels: 11.
- Repeated model-name labels: [["Cargoyle",3],["Double Demon",2],["Eevil Weevil",4],["Fangster",3],["Turboa",2],["Vampyra",2],["Rodzilla",2]].
- The same Toy # across different years, countries or table scopes is preserved as separate source rows. No deduplication or casting/release/package identity inference was performed.
- Article text states the series was introduced in 1986 and ran through 1989; it also states all 11 castings were new models designed by Larry Wood. These statements are contextual prose, not a substitute for row-level product facts.

## Output
- CSV: `research/extractions/EARLY-COLLECTIONS-SPEED-DEMONS.csv`
