# King Kuda extraction QA

- Source: `Early Collections/King Kuda _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5a5572d63d083f36a105c7b810728a7d02134c6d`
- Manifest SHA-256: `E8D78A5DA662670E38C7EB158A176E1E348FCFD414894BFA5F8E6B6C02EFED5D`
- Source size from inventory: 480,117 bytes
- Fandom revision ID: 795222
- HTML content length returned by blob fetch: 480105 characters (not used as source byte size).

## Structure

Four product tables, 44 product rows:
- Table 1, section **Original Versions [ ]**: 9 rows; 12 source columns (Year; Series; Color; Stickers; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
- Table 2, section **100% Versions [ ]**: 1 rows; 12 source columns (Year; Series; Color; Stickers; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
- Table 3, section **Retooled Versions [ ]**: 23 rows; 13 source columns (Col #; Year; Series; Color; Tampo; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
- Table 4, section **Code 3 [ ]**: 11 rows; 9 source columns (Year; Series; Body Color; Tampo; Wheel Type; Country; Quantity; Notes; Photo).
- Separate Gallery section: 0 extracted gallery references.
- Total CSV records: 44.

## QA observations

- Toy # values present: 33; distinct values: 22.
- Repeated Toy # groups: 2; 6190 (8 rows), L0738 (5 rows)
- Year values present: 44; distinct source values: 1970, 1998, 2002, 2006, 2007, 2008, 2010, 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025.
- Product rows retain table index, source section, source row order, original source headers, original cell values, parsed field values, raw row HTML, and per-cell image metadata.
- Blank Toy # and other blank cells remain blank. Repeated values are not deduplicated.
- Table schemas are not identical: Original Versions and 100% Versions use a `Stickers` column; Retooled Versions and Code 3 use `Tampo`. Code 3 has a separate schema with `Body Color` and `Quantity`.
- Image metadata is retained at the source-cell level, including filename, alt text, image URL and file-page link where present.
- No inference or normalization of product/release/package identity was applied.

## Output

- CSV: `research/extractions/EARLY-COLLECTIONS-KING-KUDA.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-KING-KUDA-EXTRACTION-QA.md`
