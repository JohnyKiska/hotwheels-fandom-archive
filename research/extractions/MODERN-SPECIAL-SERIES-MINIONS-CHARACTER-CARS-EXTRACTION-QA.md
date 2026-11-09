# Minions Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Minions Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `af61bccc5d0616a9cdf35244b5c4c598a454a659`
- Source manifest SHA-256: `A2638AD0D73FC98E749303F84B784F3F80210265F1B75A6798F666615993344C`
- Source size (bytes): 384672
- Fandom revision ID: 687208
- Product tables extracted: 4
- Product rows extracted: 19
- Embedded table image references: 36
- Links retained from product cells: 75
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-MINIONS-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
