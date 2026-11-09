# Super Streeters extraction QA

- Source: `Early Collections/Super Streeters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `963b63c8a2df9d844fcc4404df9e7c0c4e5778aa`
- Manifest SHA-256: `28062DDB1DC01A927BECD7E51C433506A1E3B322060550793081F3C407BD5108`
- Source size from MANIFEST: 358,718 bytes; fetched HTML content length: 358,678 characters.
- Fandom revision ID: 789451.

## Extraction
- Product tables: 1; section: Main product table; 13 data rows, 9 source columns (Toy #, Collector #, Vehicle Name, Color, Tampo, Wheel Type, Notes, Photo Loose, Photo Carded).
- Separate standard Wikia gallery items: 8.
- Total CSV records: 21.
- Embedded product-table image references: 26; gallery entries: 8.
- Toy # values: 13 populated rows, 11 distinct; repeats: `9241` (3).
- Collector # values: 13 populated rows, 10 distinct; repeats: `36` (2), `59` (3).
- Vehicle-name labels: 10 distinct; repeats: `Corvette Stingray` (3), `Super Van` (2).
- Raw source headers, cell values and HTML, source order, model links, and per-cell image metadata (alt, filename, image key, src/data-src and dimensions) retained. Blank Photo Loose and Photo Carded cells are preserved as blank values.

## Gallery
- Item 1: `PATCH SUPER STREETERS Hot Bird b.jpg`; alt `Mail-Away PATCH SUPER STREETERS`; file link `/wiki/File:PATCH_SUPER_STREETERS_Hot_Bird_b.jpg`.
- Item 2: `Back of Patch Card.jpg`; alt `Back of Patch Cards`; file link `/wiki/File:Back_of_Patch_Card.jpg`.
- Item 3: `PATCH Card Super Streeters No.2500 Upfront 924 r1.jpg`; alt `Patch Card Super Streeters No.2500 ●36 Upfront 924`; file link `/wiki/File:PATCH_Card_Super_Streeters_No.2500_Upfront_924_r1.jpg`.
- Item 4: `PATCH Card Super Streeters No.2500 Upfront 924 r1T.jpg`; alt `Patch Card Super Streeters No.2500 ●36 Upfront 924`; file link `/wiki/File:PATCH_Card_Super_Streeters_No.2500_Upfront_924_r1T.jpg`.
- Item 5: `PATCH Card Super Streeters No.2500 Upfront 924 r2.jpg`; alt `Patch Card Super Streeters No.2500 ●36 Upfront 924`; file link `/wiki/File:PATCH_Card_Super_Streeters_No.2500_Upfront_924_r2.jpg`.
- Item 6: `PATCH Card Super Streeters No.2504 Hare Splitter Rack-RED r1.jpg`; alt `Patch Card Super Streeters No.2504 48 Hare Splitter`; file link `/wiki/File:PATCH_Card_Super_Streeters_No.2504_Hare_Splitter_Rack-RED_r1.jpg`.
- Item 7: `PATCH Card Super Streeters No.2504 Hare Splitter Rack-RED r1C.jpg`; alt `Patch Card Super Streeters No.2504 48 Hare Splitter`; file link `/wiki/File:PATCH_Card_Super_Streeters_No.2504_Hare_Splitter_Rack-RED_r1C.jpg`.
- Item 8: `PATCH Card Super Streeters No.2504 Hare Splitter Rack-RED r2.jpg`; alt `Patch Card Super Streeters No.2504 48 Hare Splitter`; file link `/wiki/File:PATCH_Card_Super_Streeters_No.2504_Hare_Splitter_Rack-RED_r2.jpg`.

## Notes
- The source table includes Toy #, Collector #, and model variation data. Repeated identifiers and model labels remain distinct rows.
- The page's table markup is preceded by a Fandom UI heading ("New to Fandom? Unlock more settings"), not a meaningful product section heading. The extraction records it as the main product table without treating that UI label as a collection section.
- No year values are inferred; the table has no Year column.

## Output
- `research/extractions/EARLY-COLLECTIONS-SUPER-STREETERS.csv`
