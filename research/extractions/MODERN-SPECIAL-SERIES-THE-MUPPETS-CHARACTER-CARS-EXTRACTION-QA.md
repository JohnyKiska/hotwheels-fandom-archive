# The Muppets Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/The Muppets Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `b61e1c104ebd671fe34343f4c922dd497e53fdf9`
- Source manifest SHA-256: `EFABB8AD70C4541F51185C76B0721CE0FEBCC466D656BF21A0F91C5586A766EC`
- Source size (bytes): 356088
- Fandom revision ID: 759440
- Product tables extracted: 1
- Product rows extracted: 6
- Embedded table image references: 12
- Links retained from product cells: 26
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-THE-MUPPETS-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
