# Mainline 1991: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1991/List of 1991 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `54833c333f484b819f761e97ce59b642ec1a740d`
- File size: 420,133 bytes (Git tree size)
- Manifest SHA-256: `3e6b7ebddfa19858139a7d42f0e422151221b5b558f6994e0680597450fa15f4`
- Fandom revision: 797729

Machine-readable export: [MAINLINE-1991.csv](MAINLINE-1991.csv). It preserves table boundaries, row positions, raw headers and all source cells. New Castings/Reissues use 12 columns; California Customs uses nine.

## Extraction method

Extracted all three product tables and 62 rows. Values are mapped by source header name. California Customs is a distinct list without Collector #, not a continuation of the annual Col # sequence.

## QA results

| Check | Result |
|---|---:|
| Product tables | 3 |
| Source rows | 62 |
| New Castings | 27 |
| Reissues | 24 |
| California Customs | 11 |
| Distinct nonblank Col # | 39 |
| Distinct nonblank Toy # | 46 |
| Blank Col # in New Castings/Reissues | 10 |
| Blank Toy # across tables | 9 |
| Duplicate Col # values | 129 (2 rows), 148 (2 rows) |
| Repeated Toy # values | 1470 (2 rows), 1897 (2 rows), 2097 (2 rows), 3209 (2 rows), 7607 (3 rows), 9749 (2 rows) |

## Notable cases

- Buick Stocker, Holden Commodore, Mercedes-Benz SL, Peugeot 405 (two listings), Porsche 930, Renault 5 Turbo (two listings), and Speed Shark have blank Col # in New Castings; the Buick is labelled Roses Department Store Promo, while some rows are International.
- Speed Shark (Heroes on Hot Wheels) has blank Toy #.
- Reissues has eight blank Toy # rows: VW Bug, T-Bird Stocker, Fire Eater, '32 Ford Delivery, '37 Bugatti, Auburn 852, Fat Fendered '40, and '57 T-Bird. The '57 T-Bird row has blank Col # and note "International card only".
- Col #129 (Suzuki Quadracer) and #148 (Porsche 930) each appear twice as repeated rows in New Castings.
- Col #149? No: do not infer any relationship from matching Col #/Toy # alone. The source has Toy #7607 repeated across Porsche 930 entries, Toy #9749 for two Renault 5 Turbo entries, and cross-table repeats in California Customs.
- California Customs has no Col # column; it lists 11 rows. Several Toy # values repeat within/across other sections: 1470, 1897, 2097.
- Preserve leading zeroes in identifiers such as Toy #0773, Col #072 and Col #028.

## Table inventory

- Table 1, New Castings [ ]: 27 rows; 12 columns (Col # | Car name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 2, Reissues [ ]: 24 rows; 12 columns (Col # | Car name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 3, California Customs [ ]: 11 rows; 9 columns (Car Name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Photo)

## Interpretation notes

- Blank Col # is not a zero or a missing annual sequence number unless confirmed; some records are promos or International listings.
- California Customs has a separate scope with no Collector # field.
- Toy # may be shared by multiple records or castings in the source; do not use it as a globally unique release key.
- Preserve leading zeroes and all source-specific identifiers as text.
- Fandom is a secondary source; confirm ambiguous identifiers and missing values with packaging/catalogues before normalization.
