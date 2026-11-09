# Marvel Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Marvel Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `85aa6572f0f636a6af26c400a6a0617d7d1ea5e2`
- Source manifest SHA-256: `A65BDA74B60B511104DF722E2D45E644B0A730A96D1F0CFC116D6A9D0659D114`
- Source size (bytes): 775918
- Fandom revision ID: 702958
- Product tables extracted: 27
- Product rows extracted: 246
- Embedded table image references: 456
- Links retained from product cells: 955
- CSV parts: 2
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-MARVEL-CHARACTER-CARS.csv`
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-MARVEL-CHARACTER-CARS-PART-02.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
