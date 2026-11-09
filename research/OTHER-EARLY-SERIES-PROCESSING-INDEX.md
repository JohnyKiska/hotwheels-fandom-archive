# Other Early Series processing index

Scope: archived Fandom pages in `Other Early Series/` on `main`. Folder membership is source provenance and does not establish a canonical product hierarchy.

Inventory: 5 HTML files, 2,217,704 bytes total. 5 of 5 pages extracted and QA-reviewed.

| Source file | Git blob SHA | Size (bytes) | Manifest SHA-256 | Processing status |
|---|---|---:|---|---|
| `Action Cycles _ Hot Wheels Wiki _ Fandom.html` | `889f2017f06a1edde67368ecf209b1ed33463fba` | 380310 | `94E1E73F6FF52189912A56A9310175E7E331D3BEAE74C1263C28C0DB0CD09E8A` | Extracted + QA |
| `Action Racers _ Hot Wheels Wiki _ Fandom.html` | `2a204aee5df7394d298dd2891b8e2bb38f3b3ed5` | 623368 | `3289E12DDDF4C778B29B6231BB7B203DBE7EF926F990E98BE145D1D4FA154B45` | Extracted + QA |
| `Attack Pack _ Hot Wheels Wiki _ Fandom.html` | `305c914e6e2d7add82bf41ff003119cbe8ca0c3f` | 464313 | `2B7E88C50E07E640CD1444DDF83EE9083B45EE4B2E86D43B69AE74D5FF6FBA0F` | Extracted + QA |
| `Hot Wheels Railroad _ Hot Wheels Wiki _ Fandom.html` | `366d954a1fa747c5d19b8bd6460351826fa0a7f8` | 357350 | `BB963E057728779024516D2A4F7BF925B62C40DD9748E568BB41E3E9B7CEC85E` | Extracted + QA |
| `Key Force _ Hot Wheels Wiki _ Fandom.html` | `f838690b181f2951429c631a237ca4565661e535` | 392363 | `7C6AC1FEA7FBF6E63B653F3A536704AC119757CE40DDD5CADABED69CEC389640` | Extracted + QA |

## Processing rules

1. Extract product tables in source order. Preserve source section, table and row positions, headers, raw row HTML, raw cell HTML/text, links and embedded image metadata.
2. Keep distinct source tables and rows separate; do not merge by Toy #, model name, year, or apparent casting identity.
3. Preserve source spelling and anomalies. This is a source-preserving extraction, not canonical normalization or deduplication.
4. Exclude header-only rows, including legacy bold-cell headers. Retain ambiguous/no-header tables for review.
5. Gallery entries are separate from embedded product-table images and are not independently extracted in this pass.
6. Create one CSV and one QA Markdown file per source page.

## Batch 1: all 5 pages

- Product tables scanned: 18
- Product rows extracted: 187
- Embedded table image references: 231
- Links retained from product cells: 735
- CSV/QA artifacts created and verified: 10

| Source page | Tables scanned | Product rows | Images | Links |
|---|---:|---:|---:|---:|
| Action Cycles | 1 | 26 | 26 | 26 |
| Action Racers | 2 | 67 | 67 | 109 |
| Attack Pack | 9 | 48 | 91 | 459 |
| Hot Wheels Railroad | 3 | 31 | 31 | 98 |
| Key Force | 3 | 15 | 16 | 43 |

## Review notes

- The five pages had an earlier structural research pass recorded in `research/FINDINGS.md`; this batch adds row-level source-preserving extraction and per-page QA.
- Action Racers and Hot Wheels Railroad contain multi-type/component-oriented material; keep their source structures distinct for later modeling.
- Attack Pack has nine separate product tables. Preserve all table boundaries and the source order; do not infer that repeated-looking names or entries are duplicates.
- Gallery extraction remains a separate follow-up task.

## Completion

All 5 of 5 archived Other Early Series pages have CSV extraction and per-page QA records.
