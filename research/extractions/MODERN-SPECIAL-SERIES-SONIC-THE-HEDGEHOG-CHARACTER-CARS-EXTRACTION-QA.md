# Sonic the Hedgehog Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Sonic the Hedgehog Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `39854e3dd5aef78722bde9930bcca5e541bb6e07`
- Source manifest SHA-256: `7A52D11A2CE5AFCACAC329413DA61606BCC2A29EC088492905F7B64CEAB1C30A`
- Source size (bytes): 356852
- Fandom revision ID: 792671
- Product tables extracted: 2
- Product rows extracted: 4
- Embedded table image references: 8
- Links retained from product cells: 16
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-SONIC-THE-HEDGEHOG-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
