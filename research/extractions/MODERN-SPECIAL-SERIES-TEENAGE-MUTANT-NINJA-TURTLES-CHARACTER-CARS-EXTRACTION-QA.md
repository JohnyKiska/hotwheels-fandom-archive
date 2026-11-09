# Teenage Mutant Ninja Turtles Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Teenage Mutant Ninja Turtles Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `33d48afb99d0e96d8484ca4d149d8386bde0ce48`
- Source manifest SHA-256: `CC3EE425993B09DC90D1D8471BE028A2C4A138DD247BBA7CF223CF6C121BF79E`
- Source size (bytes): 357027
- Fandom revision ID: 649579
- Product tables extracted: 6
- Product rows extracted: 17
- Embedded table image references: 34
- Links retained from product cells: 68
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-TEENAGE-MUTANT-NINJA-TURTLES-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
