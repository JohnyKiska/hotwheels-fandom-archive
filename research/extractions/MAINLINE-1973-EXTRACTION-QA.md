# Mainline 1973 Source Extraction QA

## Source and provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1973/List of 1973 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5f4b523a1310078758a3103175d593767cb4af13`
- Git tree / Contents API size: 396,978 bytes
- Manifest SHA-256: `5f0ef6a23b8507fb8ba65f2464fa76f01819ca4b5dc1f681baf4e5d090a9c3c0`
- Fandom revision: 561956

## Important source-structure exception

Unlike 1974–1977, the archived 1973 page contains **no annual product table**. The only HTML table is the yearly-navigation table. Product/model content is presented as three image galleries under distinct headings. Therefore this extraction is a faithful gallery inventory, not a reconstructed annual table. The gallery headings are retained as source scopes and are not normalized into an assumed release taxonomy.

## Gallery extraction

- HTML tables found: 1 (yearly-navigation only; excluded from product records)
- Product tables extracted: 0
- Gallery sections extracted: 3
- Gallery entries retained: 34
- New Release: 3 entries
- Hot Wheels Series: 21 entries
- Shell Promo: 10 entries
- Unique nonblank gallery captions: 34
- Blank captions: 0
- Toy # / Collector # / Series # fields: not present in gallery markup
- Color, tampo, base/window/interior and wheel attributes: not provided as structured gallery fields
- Photo metadata: image filename captured for all 34 entries

## Interpretation cautions

- `New Release`, `Hot Wheels Series`, and `Shell Promo` are preserved verbatim as page section headings. In particular, `Shell Promo` remains a separate source scope.
- Gallery captions are retained as displayed. Image filenames, alt labels, file links and model-page links are retained in Raw source cells.
- A model-page link may point to a canonical casting article whose title differs from the gallery caption. Both are retained separately; no name substitution or casting identity adjudication is performed.
- Gallery membership alone does not establish Toy #, package, release variant, color, or exact release date.
- No rows were merged or deduplicated across sections.

## Output

- `research/extractions/MAINLINE-1973.csv`
- `research/extractions/MAINLINE-1973-EXTRACTION-QA.md`

All gallery entries are preserved in source order, with section provenance and original image/link metadata.
