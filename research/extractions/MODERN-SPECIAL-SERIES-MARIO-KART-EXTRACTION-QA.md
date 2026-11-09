# Extraction QA: Mario Kart

- Source: `Modern Special Series/Mario Kart _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `eb9785087aee100e488b0c6d40b3cd62fe2d75d4`
- Manifest SHA-256: `DA042A51628AC304FB9596E6280EC4CF1C3E90CCAD70F089AE627B7413D81BF6`
- Source size: 685,858 bytes
- Fandom revision: 811416
- Retained product tables: 11
- Product rows: 198
- Embedded table image references: 307
- Links in product cells: 861
- CSV schema: 21 columns

CSV artifacts (ordered parts):
- `MODERN-SPECIAL-SERIES-MARIO-KART-PART-01.csv`: 100 rows
- `MODERN-SPECIAL-SERIES-MARIO-KART-PART-02.csv`: 98 rows

QA: table/row ordering, headers, raw cell HTML, row HTML, text values, link attributes, and image attributes are retained. Gallery-only items were not independently extracted. No product identity normalization or deduplication was applied.