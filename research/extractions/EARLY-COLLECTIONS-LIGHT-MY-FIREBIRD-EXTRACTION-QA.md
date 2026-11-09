# Light My Firebird extraction QA

- Source: `Early Collections/Light My Firebird _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `49971146f54ec92309098b45b9d807ab13d94ff4`
- Manifest SHA-256: `2FC6D29B2DA88A39FB0238B613C787726AC3B8854A21DEB64AF156481CB82412`
- Source size from inventory: 385,941 bytes
- Fandom revision ID: 801165

## Structure

Three product tables, 20 product rows:
- **Original Versions [ ]**: 10 rows, 12 source columns (Year; Series; Color; Stickers; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
- **100% Versions [ ]**: 6 rows, 12 source columns (Year; Series; Color; Tampo; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
- **Retooled Versions [ ]**: 4 rows, 12 source columns (Year; Series; Color; Tampo; Base Color / / / Type; Window Color; Interior Color; Wheel Type; Toy #; Country; Notes; Photo).
- Separate Gallery section: 13 image references.
- Total CSV records: 33.

## QA observations

- Populated Toy # cells: 20; distinct values: 9.
- Repeated Toy # groups: 3; 6408 (10 rows), 22055 (2 rows), 56579 (2 rows)
- Distinct source Year values: 1970, 1998, 2000, 2002, 2003, 2006, 2011, 2016.
- Original Versions uses `Stickers`; 100% Versions and Retooled Versions use `Tampo`. Original source schemas are retained separately.
- Product rows preserve source section, table and row order, original headers and cell values, parsed field values, raw row HTML and per-cell image metadata.
- Gallery records preserve source order, captions, image filenames, alt text, image URLs and file-page links where present.
- Blank cells and repeated identifiers are retained; no deduplication or inferred product identity applied.

## Output

- CSV: `research/extractions/EARLY-COLLECTIONS-LIGHT-MY-FIREBIRD.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-LIGHT-MY-FIREBIRD-EXTRACTION-QA.md`
