# 2021 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2021 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `a7558bff165e04f0643d0d468378db2b1d701bfe`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 319541
- Fandom revision ID: 781193
- Product tables: 2
- Product rows: 8
- Inline images in product rows: 15
- Links in product rows: 40

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
