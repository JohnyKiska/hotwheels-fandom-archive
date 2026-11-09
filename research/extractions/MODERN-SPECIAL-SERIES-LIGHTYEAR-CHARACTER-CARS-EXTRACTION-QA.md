# Lightyear Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Lightyear Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `2ae665b19a51b6ad539e3429cc55b4e5aecce395`
- Source manifest SHA-256: `210E91D4983CA129DCC246841652DF288C96035EAC9E925FF83615E795F38AC5`
- Source size (bytes): 369028
- Fandom revision ID: 590764
- Product tables extracted: 3
- Product rows extracted: 12
- Embedded table image references: 22
- Links retained from product cells: 47
- CSV parts: 1
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-LIGHTYEAR-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
