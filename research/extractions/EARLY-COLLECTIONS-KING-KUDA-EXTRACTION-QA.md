# King Kuda extraction QA

- Source: `Early Collections/King Kuda _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5a5572d63d083f36a105c7b810728a7d02134c6d`
- Manifest SHA-256: `E8D78A5DA662670E38C7EB158A176E1E348FCFD414894BFA5F8E6B6C02EFED5D`
- Source size from inventory: 480,117 bytes
- Fandom revision ID: 795222
- Four product tables, 44 product rows:
  - Original Versions [ ]: 9 rows, 12 source columns (Year; Series; Color; Stickers; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
  - 100% Versions [ ]: 1 rows, 12 source columns (Year; Series; Color; Stickers; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
  - Retooled Versions [ ]: 23 rows, 13 source columns (Col #; Year; Series; Color; Tampo; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
  - Code 3 [ ]: 11 rows, 9 source columns (Year; Series; Body Color; Tampo; Wheel Type; Country; Quantity; Notes; Photo).
- Separate Gallery section: 0 gallery entries.
- Total CSV records: 44.

## QA observations

- Toy # values present: 33; distinct values: 22.
- Repeated Toy # groups: 2; 6190 (8 rows), L0738 (5 rows)
- Year values present: 44; distinct source values: 1970, 1998, 2002, 2006, 2007, 2008, 2010, 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025.
- Product rows preserve source section, table and row order, source headers, raw values, parsed field values, raw row HTML and cell-level image metadata.
- Blank cells and repeated identifiers are retained; no deduplication or product identity inference applied.
- Original Versions and 100% Versions use `Stickers`; Retooled Versions and Code 3 use `Tampo`. Code 3 has a distinct schema with `Body Color` and `Quantity`.
- Gallery entries preserve image filename, alt, image URL and file-page link where present.

## Output

- CSV: `research/extractions/EARLY-COLLECTIONS-KING-KUDA.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-KING-KUDA-EXTRACTION-QA.md`
