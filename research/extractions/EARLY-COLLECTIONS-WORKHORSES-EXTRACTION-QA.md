# Workhorses extraction QA

## Source
- Archived source: `Early Collections/Workhorses _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e0e72cc553f2b6eedf235cf863801f0346f76a27`
- Manifest SHA-256: `609E788E2E149D9F8A12556C78B38190BEB9E41F78A5AA55ACFE611ACCA5A67A`
- Source size: 485,493 bytes
- HTML content length: 485,483 characters
- Fandom revision ID: 767851
- Article title: Workhorses

## Extraction summary
- Product tables: 2
- Product rows: 86
- Separate standard Wikia gallery items: 0 detected
- Embedded image references in product-table cells: 172
- Distinct model-name labels: 34
- Populated Toy # cells: 86; distinct values: 40
- Repeated Toy # groups: 27
- Repeated model-name groups: 25
- CSV records: 86

## Table-level results
### Table 0: Original Card
- Product rows: 37
- Source columns (10): `Toy #`, `Vehicle Name`, `Color`, `Tampo`, `Wheel Type`, `Year`, `Country`, `Notes`, `Photo Loose`, `Photo Carded`
- Embedded image references: 74

### Table 1: 87-89 Card
- Product rows: 49
- Source columns (10): `Toy #`, `Vehicle Name`, `Color`, `Tampo`, `Wheel Type`, `Year`, `Country`, `Notes / Variations`, `Photo Loose`, `Photo Carded`
- Embedded image references: 98

## Repeated Toy # values
- `1168`: 3 source rows
- `1169`: 3 source rows
- `1171`: 7 source rows
- `1172`: 3 source rows
- `1173`: 4 source rows
- `1174`: 5 source rows
- `1695`: 2 source rows
- `1699`: 2 source rows
- `1790`: 2 source rows
- `1795`: 2 source rows
- `2537`: 2 source rows
- `2547`: 2 source rows
- `2800`: 3 source rows
- `2806`: 2 source rows
- `3254`: 2 source rows
- `3256`: 3 source rows
- `3715`: 3 source rows
- `3853`: 3 source rows
- `3916`: 2 source rows
- `3924`: 3 source rows
- `5027`: 2 source rows
- `5904`: 3 source rows
- `5905`: 2 source rows
- `5906`: 2 source rows
- `9526`: 2 source rows
- `9550`: 2 source rows
- `9640`: 2 source rows

## Repeated model-name labels
- `Airport Rescue`: 2 source rows
- `CAT Bulldozer`: 2 source rows
- `CAT Dump Truck`: 6 source rows
- `CAT Forklift`: 3 source rows
- `CAT Wheel Loader`: 3 source rows
- `Construction Crane`: 2 source rows
- `Fire Eater`: 2 source rows
- `Good Humor Truck`: 3 source rows
- `Hiway Hauler`: 11 source rows
- `Old Number 5`: 2 source rows
- `Oshkosh Snow Plow`: 2 source rows
- `Peterbilt Cement Mixer`: 3 source rows
- `Peterbilt Dump Truck`: 3 source rows
- `Peterbilt Tank Truck`: 6 source rows
- `Phone Truck`: 2 source rows
- `Rig Wrecker`: 2 source rows
- `Team Bus`: 4 source rows
- `Thunder Roller`: 3 source rows
- `Big Rig`: 2 source rows
- `CAT Earth Mover`: 2 source rows
- `CAT Road Roller`: 3 source rows
- `Flame Stopper`: 2 source rows
- `Rescue Ranger`: 3 source rows
- `School Bus`: 2 source rows
- `Sheriff Patrol`: 2 source rows

## Preservation and QA notes
- All data rows are retained in source order, separately by source table.
- Original source headers, per-cell tag/attributes/HTML, decoded cell values, and complete raw row HTML are preserved.
- Model links and per-cell image metadata (alt text, source URL, original filename/key, and linked file URL) are retained where present.
- Repeated Toy # values and repeated model labels remain separate records; no automatic deduplication or entity matching was performed.
- Photo Loose and Photo Carded are retained as source columns; image references remain attached to their original source cells.
- Table headings are recorded as source sections, not treated as canonical product taxonomy.
- No separate `wikia-gallery-item` gallery entries were detected in this page.
