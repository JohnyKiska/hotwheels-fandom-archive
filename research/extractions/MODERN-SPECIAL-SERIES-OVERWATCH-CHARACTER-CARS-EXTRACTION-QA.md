# Overwatch Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Overwatch Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `58dd862846e24c575d14a4ee283ce71d0f735339`
- Source manifest SHA-256: `EC8E531F5438E9F4BF282DE048C159E55472BC83AC98B2A51735D834531198E0`
- Source size (bytes): 363567
- Fandom revision ID: 814295
- Product tables extracted: 2
- Product rows extracted: 11
- Embedded table image references: 22
- Links retained from product cells: 44
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-OVERWATCH-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
