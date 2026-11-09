# Rescue Team extraction QA

## Source
- File: `Early Collections/Rescue Team _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e131d541f95be40ae587be0c90596a18faaf62c9`
- Manifest SHA-256: `E3181E548EBF2A393DF6191CC983C6C6FF23431572633BFA1BF339F0C499588C`
- Source size: 331,442 bytes (manifest); extracted HTML: 331,432 characters.
- Fandom revision ID: 767735.

## Extraction
- 1 product table, 6 product rows.
- Source table headers (9): `Toy #`, `Collector #`, `Vehicle Name`, `Color`, `Tampo`, `Wheel Type`, `Notes`, `Photo Loose`, `Photo Carded`.
- 2 separate gallery items.
- 8 total CSV records (product rows and gallery items).
- Table source order and raw cell HTML retained; link and image metadata are stored per cell.
- Gallery caption, filename, file link, image URL and anchor retained separately.

## QA observations
- Toy # populated: 6/6; blank: 0.
- Distinct populated Toy #: 6.
- Repeated Toy #: [].
- Distinct vehicle-name labels: 6.
- Repeated vehicle-name labels: [].
- Collector # and Toy # are preserved as separate source fields.
- Photo Loose and Photo Carded are retained as raw cell HTML and parsed image metadata; no image is treated as a separate release record.
- No rows merged and no missing product attributes inferred.

## Output
- CSV: `research/extractions/EARLY-COLLECTIONS-RESCUE-TEAM.csv`
