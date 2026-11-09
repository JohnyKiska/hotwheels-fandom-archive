# Sanrio Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Sanrio Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `a97d4cc212c10ae38ed7306d64ac6556ec0bf2ea`
- Source manifest SHA-256: `A4B82D7E5E1CD90F15B675EA01B625F16E155F1A9FFBBFA8206D0273DF18E3CD`
- Source size (bytes): 375508
- Fandom revision ID: 512364
- Product tables extracted: 4
- Product rows extracted: 15
- Embedded table image references: 26
- Links retained from product cells: 56
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-SANRIO-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
