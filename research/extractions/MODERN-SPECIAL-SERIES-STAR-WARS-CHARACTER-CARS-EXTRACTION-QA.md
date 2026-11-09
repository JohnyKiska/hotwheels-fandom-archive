# Star Wars Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Star Wars Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `e1a71f27cfe72e51eecc6d58b8ed3c60d81390d1`
- Source manifest SHA-256: `DBA8B280814373986DAB14AB82AB77724AD4CD73E9B9EA459B4C89CB0D8FE944`
- Source size (bytes): 887617
- Fandom revision ID: 778377
- Product tables extracted: 33
- Product rows extracted: 317
- Embedded table image references: 582
- Links retained from product cells: 1213
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-STAR-WARS-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
