# Good Luck Trolls Character Cars extraction QA

- Source: `Modern Special Series/Character Cars/Good Luck Trolls Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `abb57d9390cab73dc3697b4ba882c865987132c6`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 348041
- Fandom revision ID: 525496
- Product tables: 1
- Product rows: 1
- Inline images in product rows: 2
- Links in product rows: 4

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
