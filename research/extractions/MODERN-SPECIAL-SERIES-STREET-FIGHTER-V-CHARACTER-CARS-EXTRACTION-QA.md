# Street Fighter V Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Street Fighter V Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `a40e3c20b066c9c36bb7b4be06c386c1ecf22e06`
- Source manifest SHA-256: `1C724D568AE53D6AA32888BBF904DC20F2B002D308A9255017419D2E92C8BD72`
- Source size (bytes): 352966
- Fandom revision ID: 655518
- Product tables extracted: 1
- Product rows extracted: 5
- Embedded table image references: 10
- Links retained from product cells: 20
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-STREET-FIGHTER-V-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
