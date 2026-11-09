# 2020 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2020 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `bc2e213310fb4d0f48d367b2a5030d4ec137de36`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 357185
- Fandom revision ID: 781210
- Product tables: 4
- Product rows: 28
- Inline images in product rows: 47
- Links in product rows: 102

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
