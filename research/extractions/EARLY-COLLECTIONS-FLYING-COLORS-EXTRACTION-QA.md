# Flying Colors extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`, branch `main`
- Source: `Early Collections/Flying_Colors.htm`
- Git blob SHA: `7416dad03fc92b77384fc132e0001366744148ac`
- Manifest size: 779,454 bytes
- Manifest SHA-256: `40EA1A76B9A5C2890E2D6439D2033651EE819CC02C00BA5CB51B9D7E6241EFB2`
- Fandom revision ID: 795936
- Extraction date: 2026-11-09

## Extraction results
- 1974: 44 rows, 8 source columns.
- 1975: 42 rows, 7 source columns.
- 1976: 33 rows, 7 source columns.
- 1977: 77 rows, 7 source columns.
- 1978: 16 rows, 7 source columns.
- Product rows total: 212
- Distinct Toy # values: 91
- Repeated Toy # groups: [["2019",2],["2021",2],["6963",3],["6964",2],["6965",2],["6967",2],["6968",2],["6972",5],["6973",3],["6976",6],["6978",3],["6980",3],["7616",4],["7617",3],["7619",2],["7620",2],["7621",3],["7622",2],["7630",3],["7644",3],["7647",2],["7648",3],["7649",6],["7650",3],["7651",2],["7653",2],["7654",2],["7655",2],["7658",2],["7659",3],["7660",4],["7661",5],["7662",2],["7664",3],["7665",3],["7666",2],["7670",3],["7671",2],["7966",2],["8235",2],["8240",2],["8258",7],["8259",5],["8260",2],["8261",4],["8273",4],["9037",3],["9088",2],["9089",2],["9090",2],["9118",2],["9119",2],["9120",3],["9183",3],["9184",3],["9185",3],["9186",2],["9240",2],["9241",2],["9242",2],["9638",2],["9639",2],["9640",2],["9641",2],["9642",4],["9643",2],["9644",2],["9646",2],["9647",2],["9649",2]]
- Wheel Type image refs: 211
- Loose photo refs: 212
- Carded photo refs: 212
- Separate Track Sets reference: Thundershift 500 (stored as a separate `section_reference` row, not a product-table record); its metadata occupies the final `Raw source cells` field and the row matches the 22-column CSV schema.

## Preservation notes
- The five product tables map in source order to headings 1974, 1975, 1976, 1977 and 1978.
- Source schemas vary by year. Original headers and raw cell values are retained.
- Wheel Type is often represented by an image rather than text. Image filename, alt and link are therefore captured separately; cell-level image metadata is also retained in Raw source cells.
- Loose and carded photo filename, alt and file links are stored independently.
- Repeated Toy # values remain separate source rows. No deduplication or casting identity resolution was performed.
- Track Sets is a distinct section containing Thundershift 500; it is not merged into annual product rows.

## QA
- 212 product rows extracted from five year tables, plus one separate section reference.
- 211 wheel-type image refs, 212 loose and 212 carded photo refs captured.
- Source order retained within each table; empty values preserved.

## Output
- `research/extractions/EARLY-COLLECTIONS-FLYING-COLORS.csv`
