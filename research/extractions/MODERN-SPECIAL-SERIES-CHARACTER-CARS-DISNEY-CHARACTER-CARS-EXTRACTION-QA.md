# Disney Character Cars extraction QA

- Source: `Modern Special Series/Character Cars/Disney Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `76428a8f14b805bdfaa2d7790e3decae76dfd675`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 681281
- Fandom revision ID: 792725
- Product tables: 22
- Product rows: 165
- Inline images in product rows: 313
- Links in product rows: 651

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
