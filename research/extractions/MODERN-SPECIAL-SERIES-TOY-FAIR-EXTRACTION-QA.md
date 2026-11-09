# Toy Fair Extraction QA

- Source: `Modern Special Series/Toy Fair _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `f51899691bcddbdb91788e57b548c78ffe59fdb3`
- Source manifest SHA-256: `8C389F16BBFE308BE771839AA6615885C85F8407C5557AF99320D5D19B104C73`
- Source size (bytes): `f51899691bcddbdb91788e57b548c78ffe59fdb3`
- Fandom revision ID: 770072
- Product tables extracted: 1
- Product rows extracted: 47
- Embedded table image references: 48
- Links retained from product cells: 101
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-TOY-FAIR.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded; tables with headers and data rows are retained.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass.
- This is a source-preserving extraction, not a normalization or deduplication pass.
