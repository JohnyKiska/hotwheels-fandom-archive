# DreamWorks Character Cars extraction QA

- Source: `Modern Special Series/Character Cars/DreamWorks Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e1602d0b0dfd35c5f9d8db37721d5c1e6549eedc`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 372989
- Fandom revision ID: 713100
- Product tables: 4
- Product rows: 13
- Inline images in product rows: 26
- Links in product rows: 52

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
