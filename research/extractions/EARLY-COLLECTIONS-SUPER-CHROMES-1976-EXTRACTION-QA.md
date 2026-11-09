# Super Chromes (1976) extraction QA

- Source: `Early Collections/Super Chromes (1976) _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `658a01422af975de2968285f809f07cbdbc8f272`
- Manifest SHA-256: `A6C523DD16C5B102392FEC26D70C9E3415998B8B2A49025242B96B8146FB27E2`
- Source size from MANIFEST: 376,448 bytes; fetched HTML content length: 376,436 characters.
- Fandom revision ID: 714219.

## Extraction
- Product tables: 3; total product rows: 46.
- **1976**: 25 data rows, 11 source columns (Name, Color, Tampos, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes, Photo).
- **1977**: 19 data rows, 11 source columns (Name, Color, Tampos, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes | / | Variations, Photo).
- **1978**: 2 data rows, 11 source columns (Name, Color, Tampo, Base Color | / | Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes | / | Variations, Photo).
- Separate standard Wikia gallery items: 4.
- Total CSV records: 50.
- Embedded product-table image references: 46; separate gallery items: 4.
- Toy # values: 46 populated rows; 13 distinct values. Repeated values: `9201` (2), `9202` (2), `9203` (3), `9204` (2), `9205` (4), `9206` (3), `9207` (3), `9208` (5), `9209` (2), `9210` (3), `9211` (2), `9212` (3), `9505` (12).
- Source sections are year-specific (1976, 1977, 1978); all source rows remain separate, including repeated models and identifiers.
- Raw source headers, cell values and HTML, source order, model links, and per-cell image metadata (alt, filename, image key, src/data-src and dimensions) retained.

## Gallery
- Item 1: `Must superchromes.jpg`; alt `Early '76 Checklist`; file link `/wiki/File:Must_superchromes.jpg`.
- Item 2: `Mustang stocker bp RL.jpg`; alt ``; file link `/wiki/File:Mustang_stocker_bp_RL.jpg`.
- Item 3: `6-pack SuperChromes.jpg`; alt ``; file link `/wiki/File:6-pack_SuperChromes.jpg`.
- Item 4: `Japan Red Box 47 P-911 r-4C.jpg`; alt `Japan Red Box 47`; file link `/wiki/File:Japan_Red_Box_47_P-911_r-4C.jpg`.

## Notes
- Table column labels differ slightly across years (for example, Tampos/Tampo and Notes/Notes / Variations); the original schema is preserved.
- No records are merged or deduplicated. Model identity and release/package relationships are not inferred from repeated names or Toy #.

## Output
- `research/extractions/EARLY-COLLECTIONS-SUPER-CHROMES-1976.csv`
