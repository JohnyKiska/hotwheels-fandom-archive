# Premium Collector Set Extraction QA

- Source: `Modern Special Series/Premium Collector Set _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `5f4d11c2b0ffd91141758a90569fde9422fba639`
- Source manifest SHA-256: `D4C75995CAFD29CB82AD86F0A515344CC9D3E9FFF63FCAD618EF63376C7FEDD9`
- Source size (bytes): 545811
- Fandom revision ID: 808975
- Product tables extracted: 31
- Product rows extracted: 123
- Embedded table image references: 151
- Links retained from product cells: 725
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-PREMIUM-COLLECTOR-SET.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
