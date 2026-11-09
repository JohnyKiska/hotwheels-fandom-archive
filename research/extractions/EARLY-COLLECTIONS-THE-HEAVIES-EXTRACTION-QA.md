# The Heavies extraction QA

- Source: `Early Collections/The Heavies _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `44d592cfc35a9c1c747410900307c127172d776a`
- Manifest SHA-256: `D8478C5D6ADCA735AD7157850F29C66B10FB8282935CA15C1A2C03B5D916DF67`
- Source size from MANIFEST: 333,247 bytes; fetched HTML content length: 333,237 characters.
- Fandom revision ID: 767755.

## Extraction

- Product tables: 1.
- Table 1, **The Heavies**: 7 data rows, 9 source columns. Headers: Toy #, Collector #, Vehicle Name, Color, Tampo, Wheel Type, Notes, Photo Loose, Photo Carded.
- 7 populated Toy # values, 7 distinct: 9647, 7621, 1337, 9645, 9643, 9184, 7659.
- 7 populated Collector # values, 7 distinct: 33, 10, 99, 25, 20, 48, 26.
- Vehicle-name labels: '56 Hi-Tail Hauler; Funny Money; Geoffrey's Pick Up; GMC Motor Home; Letter Getter; Maxi Taxi; Ramblin' Wrecker.
- Separate standard Wikia gallery items: 2.
- Total CSV records: 9.
- Embedded product-table image references: 14. Photo Loose and Photo Carded contain image references in every product row; 14 embedded image references are retained separately in cell metadata.
- Raw source headers, cell values and HTML, source order, links and per-cell image metadata retained. Gallery caption, alt text, filename, file link and image metadata retained independently.

## Gallery
- Item 1: `PATCH THE HEAVIES GMC Motorhome b.jpg`; alt `Mail-Away PATCH THE HEAVIES`; caption `Mail-Away PATCH &lt;b&gt;THE HEAVIES&lt;/b&gt;`; file link `/wiki/File:PATCH_THE_HEAVIES_GMC_Motorhome_b.jpg`.
- Item 2: `Back of Patch Card.jpg`; alt `Back of Patch Cards`; caption `Back of Patch Cards`; file link `/wiki/File:Back_of_Patch_Card.jpg`.

## Article structure
- The source page has one product table and a separate Gallery section. No additional product tables were detected.
- No values were inferred, and no records were merged by Toy #, Collector # or vehicle name.

## Output
- `research/extractions/EARLY-COLLECTIONS-THE-HEAVIES.csv`
