# SpongeBob SquarePants Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/SpongeBob SquarePants Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `99e5d1aa85a35956f6a393798e9de45a31179886`
- Source manifest SHA-256: `ED05C8AEC5823D80E4FACC640D799A57BCF0DD652CD8219098200971291CE147`
- Source size (bytes): 373240
- Fandom revision ID: 687095
- Product tables extracted: 7
- Product rows extracted: 25
- Embedded table image references: 50
- Links retained from product cells: 100
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-SPONGEBOB-SQUAREPANTS-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
