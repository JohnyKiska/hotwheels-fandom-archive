# Speed Fleet extraction QA

- Source: `Early Collections/Speed Fleet _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `69ab0490c53bcde8ee008ec0c620619a49bf302a`
- Manifest SHA-256: `B748220CC3F40B55F8FF3D9FFF2769D505422FA673DF02AAAA8170C8EDBED00A`
- Source size from MANIFEST: 445,962 bytes; fetched HTML content length: 445,952 characters.
- Fandom revision ID: 799650.

## Extraction
- Conventional product tables: 2.
- Table 1, section **Speed Fleet Blue Card [ ]**: 40 product rows; 9 columns (Toy #, Model Name, Color, Year, Wheel Type, Country, Notes, Photo Loose, Photo Carded).
- Table 2, section **Speed Fleet Rainbow Card [ ]**: 36 product rows; 9 columns (Toy #, Model Name, Color, Year, Wheel Type, Country, Notes, Photo Loose, Photo Carded).
- Total product rows: 76.
- Standard Wikia gallery items: 0.
- Images embedded in table cells: 152 total references (76 in Photo Loose cells; 76 in Photo Carded cells). Lazy-loaded image URLs and filenames retained.
- Linked references inside table cells: 304.

## Identifier and field QA
- Populated Toy # values: 76; distinct values: 56.
- Repeated Toy # groups: `1456` (2 rows), `1458` (2 rows), `1484` (2 rows), `1491` (2 rows), `1494` (2 rows), `1789` (2 rows), `1796` (2 rows), `2014` (2 rows), `2546` (2 rows), `3794` (2 rows), `4384` (2 rows), `4631` (2 rows), `4699` (2 rows), `4916` (2 rows), `5026` (2 rows), `5121` (2 rows), `5138` (2 rows), `5902` (2 rows), `7670` (2 rows), `7671` (2 rows).
- Distinct model-name labels: 46; repeated model-name groups: `Firebird Funny Car` (4 rows); `Lamborghini Countach` (4 rows); `Sol-Aire CX4` (4 rows); `Thunderburner` (3 rows); `XT-3` (3 rows); `'80's Corvette` (2 rows); `Alien` (2 rows); `Blown Camaro Z-28` (2 rows); `Custom Corvette` (2 rows); `Ferrari Testarossa` (2 rows); `Fiero 2M4` (2 rows); `GT Racer` (2 rows); `Hot Bird` (2 rows); `Nissan 300ZX` (2 rows); `Pontiac Banshee` (2 rows); `Porsche 959` (2 rows); `Shadow Jet` (2 rows); `Thunderbird Stocker` (2 rows); `Tricar X8` (2 rows); `V.W. Bug` (2 rows); `Jet Sweep X5` (2 rows); `Thunderstreak` (2 rows).
- Year values: 1989: 27; 1987: 25; 1988: 15; 1986: 6; 1990: 3.
- Empty cells by source column: Photo Loose: 76; Photo Carded: 76; Notes: 47.
- No rows were merged or deduplicated. Table order, source row order, source headers, raw cell HTML, normalized cell text, links, image filenames and image URLs are retained.

## Output
- `research/extractions/EARLY-COLLECTIONS-SPEED-FLEET.csv`
