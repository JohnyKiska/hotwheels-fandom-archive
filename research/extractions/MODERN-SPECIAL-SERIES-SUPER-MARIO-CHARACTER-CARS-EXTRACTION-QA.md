# Super Mario Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Super Mario Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `a20f62788fef8c33e99ca068051cd780858036f3`
- Source manifest SHA-256: `2EFFAD309E57B458466975593A384B338001ED03077097EAD028855FC836886C`
- Source size (bytes): 444414
- Fandom revision ID: 641313
- Product tables extracted: 8
- Product rows extracted: 49
- Embedded table image references: 94
- Links retained from product cells: 192
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-SUPER-MARIO-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
