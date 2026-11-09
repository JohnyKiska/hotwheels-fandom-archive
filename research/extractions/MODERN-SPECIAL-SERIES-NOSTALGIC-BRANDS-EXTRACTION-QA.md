# Nostalgic Brands Extraction QA

- Source: `Modern Special Series/Nostalgic Brands _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `659e20ad36d08a0b09c4537f9c3142efe6db4052`
- Source manifest SHA-256: `D0926300F9374EB153CC5A15B77E90BEEB95ABB3CB835A10954CFEEF56911FA8`
- Source size (bytes): 468857
- Fandom revision ID: 798356
- Product tables extracted: 12
- Product rows extracted: 91
- Embedded table image references: 176
- Links retained from product cells: 358
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-NOSTALGIC-BRANDS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
