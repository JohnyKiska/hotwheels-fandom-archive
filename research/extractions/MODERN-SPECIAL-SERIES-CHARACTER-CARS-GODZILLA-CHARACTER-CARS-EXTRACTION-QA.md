# Godzilla Character Cars extraction QA

- Source: `Modern Special Series/Character Cars/Godzilla Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `cad502a944c63a7bc9104060dcd7b7485c57469a`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 349645
- Fandom revision ID: 616562
- Product tables: 2
- Product rows: 2
- Inline images in product rows: 4
- Links in product rows: 9

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
