# Toy Story Character Cars Extraction QA

- Source: `Modern Special Series/Character Cars/Toy Story Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `d2097ae3a5c79657ce84a4daad58c90d838d526d`
- Source manifest SHA-256: `795266E1898C68639DBA92AAB3CCB746FC825E76865CCC3DB7D01A3486C611C4`
- Source size (bytes): 423899
- Fandom revision ID: 709115
- Product tables extracted: 3
- Product rows extracted: 31
- Embedded table image references: 57
- Links retained from product cells: 123
- CSV: `research/extractions/MODERN-SPECIAL-SERIES-TOY-STORY-CHARACTER-CARS.csv`

## Extraction checks

- Product rows are retained in source order.
- Navigation/year-index tables are excluded.
- Rows without data cells (`<td>`) are excluded as header rows.
- Original table and row positions, table headers, raw row HTML, cell HTML/text, links, and image attributes are retained.
- Separate Gallery items have not been independently extracted in this pass; gallery extraction remains a follow-up task.
- This is a source-preserving extraction, not a normalization or deduplication pass.
