# 2025 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2025 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `22308b1c1dc35bd04d947be744bf3d8198af06c7`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 363193
- Fandom revision ID: 814873
- Product tables: 3
- Product rows: 30
- Inline images in product rows: 54
- Links in product rows: 129

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
