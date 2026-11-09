# Sugar Caddy extraction QA

- Source: `Early Collections/Sugar Caddy _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `550488166f32055add61cba2d38393306c9b8b62`
- Manifest SHA-256: `A90241068A42C2841DE36EAEE60C58D95855B6C22B8E8C2A8E7A1CEAD9A5D160`
- Source size from MANIFEST: 360,833 bytes; fetched HTML content length: 360,821 characters.
- Fandom revision ID: 807115.

## Extraction
- Product tables: 3; total product rows: 16.
- **Original Versions**: 12 data rows, 12 source columns (Year, Series, Color, Stickers, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes | / | Variations, Photo).
- **CIPSA Versions**: 3 data rows, 9 source columns (Color, Stickers, Base Color, Window Color, Interior Color, Wheel Type, Country, Notes | / | Variations, Photo).
- **Retooled Versions**: 1 data rows, 12 source columns (Year, Series, Color, Tampo, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes | / | Variations, Photo).
- Separate standard Wikia gallery items: 4.
- Total CSV records: 20.
- Embedded product-table image references: 17; unique gallery assets: 4.
- Toy # is present in 13 product rows across Original Versions and Retooled Versions; 2 distinct populated values. `6418` appears 12 times and `P2141` once. CIPSA Versions has no Toy # column.
- Table schemas differ by section: Original Versions and Retooled Versions have 12 columns, while CIPSA Versions has 9. Fields are retained as published, with no schema normalization or row deduplication.
- Raw source headers, cell values and HTML, source order, model links, and per-cell image metadata (alt, filename, image key, src/data-src and dimensions) retained.

## Gallery
- Item 1: `Suggar Caddy 2009 Proto.jpg`; alt `Prototype - 2009 HWC.com Series 8: Neo-Classics`; file link `/wiki/File:Suggar_Caddy_2009_Proto.jpg`.
- Item 2: `RLC 2009 Sugar Caddy Magenta China P2141.jpg`; alt `RLC 2009`; file link `/wiki/File:RLC_2009_Sugar_Caddy_Magenta_China_P2141.jpg`.
- Item 3: `HWC Series Eight Sugar Caddy.jpg`; alt ``; file link `/wiki/File:HWC_Series_Eight_Sugar_Caddy.jpg`.
- Item 4: `Suggar Caddy 2009 3D Render.jpg`; alt `2009 HWC.com Series 8: Neo-Classics - 3D Render`; file link `/wiki/File:Suggar_Caddy_2009_3D_Render.jpg`.

## Notes
- The article separates Original Versions, CIPSA Versions and Retooled Versions into distinct tables. Their different schemas are preserved.
- Gallery assets are separate records and are not treated as product rows.
- No identities, missing years, or release/package relationships are inferred beyond the source cells.

## Output
- `research/extractions/EARLY-COLLECTIONS-SUGAR-CADDY.csv`
