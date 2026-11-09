# TNT-Bird extraction QA

- Source: `Early Collections/TNT-Bird _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `fc25ac24e5f93d71789f2649de64a304f70db561`
- Manifest SHA-256: `DB87462B499536336E8B029308157350F752890864C1450E9CEE00BF65591335`
- Source size from MANIFEST: 360,478 bytes; fetched HTML content length: 360,466 characters.
- Fandom revision ID: 776418.

## Extraction
- Product tables: 2.
- Table 1, **Original Versions [ ]**: 11 data rows, 12 columns. Headers: Year, Series, Color, Tampo, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes, Photo. 11 populated Toy # values, 1 distinct; repeats: `6407` (11). Years: 1970. Series labels: Spoilers.
- Table 2, **Re-Tooled Versions [ ]**: 3 data rows, 12 columns. Headers: Year, Series, Color, Tampo, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes, Photo. 3 populated Toy # values, 3 distinct; repeats: none. Years: 2006, 2010, 2016. Series labels: HWC.com 5 - Neo-Classics | 5/6; 24th Annual Hot Wheels Collectors Convention | RLC Party; HWC Spoilers Series.
- Separate standard Wikia gallery items: 8.
- Total CSV records: 22.
- Embedded product-table image references: 14; gallery entries: 8.
- Raw source headers, cell values and HTML, source order, section names, links and per-cell image metadata retained.

## Gallery
- Item 1: `1970 Fan Club CASTINGS pg.jpg`; alt `1970 Fan Club magazine Car/Image #24`; file link `/wiki/File:1970_Fan_Club_CASTINGS_pg.jpg`.
- Item 2: `20190510 212214-1-.JPG`; alt ``; file link `/wiki/File:20190510_212214-1-.JPG`.
- Item 3: `20190510 212154-1-.JPG`; alt ``; file link `/wiki/File:20190510_212154-1-.JPG`.
- Item 4: `1970 Spoilers TNT-Bird Green Interior Variation.jpg`; alt `Green TNT-Bird with Interior Variation`; file link `/wiki/File:1970_Spoilers_TNT-Bird_Green_Interior_Variation.jpg`.
- Item 5: `RLC 2006 TNT Bird Green China K3384.jpg`; alt `RLC 2006`; file link `/wiki/File:RLC_2006_TNT_Bird_Green_China_K3384.jpg`.
- Item 6: `Collectors Convention 24th 2010 T-Bird Spoiler Thailand R8426.jpg`; alt `24th Annual Collectors Convention RLC Party 2010`; file link `/wiki/File:Collectors_Convention_24th_2010_T-Bird_Spoiler_Thailand_R8426.jpg`.
- Item 7: `Collectors Convention 24th 2010 T-Bird Spoiler Thailand R8426 Back of Card.jpg`; alt `24th Annual Collectors Convention RLC Party Back of Card 2010`; file link `/wiki/File:Collectors_Convention_24th_2010_T-Bird_Spoiler_Thailand_R8426_Back_of_Card.jpg`.
- Item 8: `TNTBird1970Poster.png`; alt `1970 Poster`; file link `/wiki/File:TNTBird1970Poster.png`.

## Article structure
- Article-level headings include Debut series, Produced, Designer, Number, Contents and Description. These are outside the product tables and are not transformed into invented structured product fields in this extraction.
- Both Original Versions and Re-Tooled Versions are preserved as separate source tables. No rows are merged across tables.

## Output
- `research/extractions/EARLY-COLLECTIONS-TNT-BIRD.csv`
