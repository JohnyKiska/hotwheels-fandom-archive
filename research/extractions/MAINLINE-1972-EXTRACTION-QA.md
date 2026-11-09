# Mainline 1972 Source Extraction QA

## Source and provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1972/List of 1972 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `af5fbc4e3f942b8a071e9a8a2d8515dbaedc7424`
- Git tree / Contents API size: 355,407 bytes
- Manifest SHA-256: `a9f2daeb776dc8bcd53b618feaabccf5618a8c04e84b0c20ceb61142b3f1294b`
- Fandom revision: 562713

## Important source-structure exception

The archived 1972 page contains no annual product table. The only HTML table is the yearly-navigation table. Product/model content is presented as one image gallery under the heading **New Castings**. This is a faithful gallery inventory, not a reconstructed annual product table.

## Gallery extraction

- HTML tables found: 1 (yearly-navigation only; excluded from product records)
- Product tables extracted: 0
- Gallery sections extracted: 1
- Gallery entries retained: 7
- New Castings: 7 entries
- Unique nonblank gallery captions: 7
- Blank captions: 0
- Toy # / Collector # / Series # fields: not present in gallery markup
- Color, tampo, base/window/interior and wheel attributes: not provided as structured gallery fields
- Photo filename captured: 7 entries
- Image alt labels captured: 7 entries
- File links and model-page links retained in Raw source cells: 7 entries

## Extracted gallery entries

| Position | Caption | Image filename |
|---:|---|---|
| 1 | Ferrari 512S | Ferrari512S.jpg |
| 2 | Funny Money | Funnymoney.jpg |
| 3 | Mercedes-Benz C-111 | Mercedesbenzc111.jpg |
| 4 | Open Fire | Openfire.jpg |
| 5 | Rear Engine Mongoose | Rearenginemongoose.jpg |
| 6 | Rear Engine Snake | Rearenginesnake.jpg |
| 7 | Side Kick | Sidekick.jpg |

## Interpretation cautions

- `New Castings` is preserved verbatim as the page section heading. It is not treated as a complete release taxonomy.
- Gallery captions, image alt labels, filenames, file links and model-page links are retained separately in the raw source metadata.
- Gallery membership alone does not establish Toy #, package, release variant, color, or exact release date.
- No rows were merged or deduplicated. Captions are unique in this source gallery.
- The page's gallery-only structure is a useful historical source signal; it must not be silently converted into a conventional annual release table.

## Output

- `research/extractions/MAINLINE-1972.csv`
- `research/extractions/MAINLINE-1972-EXTRACTION-QA.md`

All seven gallery entries are preserved in source order, with section provenance and original image/link metadata.
