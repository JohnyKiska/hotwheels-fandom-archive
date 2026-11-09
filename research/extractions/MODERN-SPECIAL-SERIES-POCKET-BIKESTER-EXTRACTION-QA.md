# Pocket Bikester Extraction QA

- Source: `Modern Special Series/Pocket Bikester _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `37b9aa764dd0b6494f468e7ff516af5fa3e4e7e8`
- Source manifest SHA-256: `5C8610030B0449DA4AE6908B889664BCF39620E6B2C2276BB25DE66AB8BAB652`
- Source size (bytes): 359448
- Fandom revision ID: 796823
- Product tables extracted: 1
- Product rows extracted: 7
- Embedded table image references: 7
- Links retained from product cells: 25
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-POCKET-BIKESTER.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
