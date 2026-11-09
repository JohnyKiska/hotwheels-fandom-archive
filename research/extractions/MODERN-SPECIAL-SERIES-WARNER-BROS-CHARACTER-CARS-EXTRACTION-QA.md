# Warner Bros. Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Warner Bros. Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `c9ec6d2a47d1b6882263e1046ff651325adcb685`
- Source manifest SHA-256: `0B40BCBCDECDBC8FA1823A7EA11D3B24BA34D1032A8A1479A09B10F1A039F2C3`
- Source size (bytes): 369961
- Fandom revision ID: 605652
- Product tables extracted: 3
- Product rows extracted: 12
- Embedded table image references: 24
- Links retained from product cells: 48
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-WARNER-BROS-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
