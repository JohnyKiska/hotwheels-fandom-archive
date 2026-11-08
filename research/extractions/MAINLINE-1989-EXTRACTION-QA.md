# Mainline 1989: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1989/List of 1989 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `0d35f3e3c8d82ea30f7e0ddf411bfacee45033a1`
- File size: 407,231 bytes (Git tree size)
- Manifest SHA-256: `ab0b0f58ff477246df412192f3df1961a0322f8277f20e790f59ac5879144a3e`
- Fandom revision: 754017

Machine-readable export: [MAINLINE-1989.csv](MAINLINE-1989.csv). The complete source row, order and five-column schema are retained.

## Extraction method

Extracted the single annual table with 76 rows and five source columns: Col. #, Model Name, Series, Series #, Photo.

## QA results

| Check | Result |
|---|---:|
| Product tables | 1 |
| Source rows | 76 |
| Unique Col. # | 76 |
| First / last Col. # | 001 / 076 |
| Missing Col. # values in 001–076 | 0 |
| Unique Series # | 76 |
| First / last Series # | 1/76 / 76/76 |
| Toy # column present | No |
| Photo cells empty | 76 / 76 |

## Interpretation notes

- This 1989 annual page uses Col. # and Series # but has no Toy # field. Do not treat absent Toy # as missing values.
- Col. # and Series # are text identifiers and should be retained as text.
- The page contains one simple annual Mainline table; there are no separate series sections in the extracted table.
- Fandom is a secondary source; do not infer casting/tooling identity from model names alone.
