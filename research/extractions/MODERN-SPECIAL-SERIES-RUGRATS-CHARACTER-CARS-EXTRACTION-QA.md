# Rugrats Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Rugrats Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `ebe7d2c673dbd0e41b5d4ee89fa1ad7722902bf4`
- Source manifest SHA-256: `C066325EE99D0093448BA5134A11995FD3D40865EF14CCA74AFCDED51A111927`
- Source size (bytes): 326127
- Fandom revision ID: 687008
- Product tables extracted: 2
- Product rows extracted: 5
- Embedded table image references: 10
- Links retained from product cells: 20
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-RUGRATS-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
