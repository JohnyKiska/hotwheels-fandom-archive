# Archive Processing Audit: Mainline (2026-11-08)

## Scope and method

This audit compares the committed Git trees of the two archive repositories with the current research index and findings. It distinguishes source availability from page review, row extraction, QA, and database-ready normalization.

Repositories and immutable tree snapshots inspected:

- Mainline archive: `JohnyKiska/hotwheels`, branch `archive/historical-html-1968-2026`, commit `2f43ad43324c6a16c786dad4b34fceac7693e5d6`, tree `6e1b4df82f50e4bfb7ab7186164b96422e4387b9`.
- Fandom archive: `JohnyKiska/hotwheels-fandom-archive`, branch `main`, commit `620654d5c1698c3114c880e915589780781d02f7`, tree `4a480a2909d76753a8b07a94347607a2fec200e5`.
- Mainline manifest: `ALLHW/MANIFEST.csv`, blob `1a5933422177fa94fb09b1e9357e3a41c37094d6`.

The inventory is based on the recursive Git tree and manifest, not on assumptions from local folder names.

## 1. Source inventory: Mainline

The `ALLHW/` directory contains:

- 59 year directories, 1968 through 2026 inclusive, with no missing year directory.
- 60 HTML pages: one annual page for every year plus a second 2010 International page.
- `MANIFEST.csv` contains 60 data records (61 lines including header), matching the 60 HTML pages.
- The 2010 ordinary and International pages are separate source datasets and must not be merged without comparison.

The Fandom archive repository separately contains 530 HTML/HTM files and 2 CSV files (532 files total), matching the previously recorded inventory. This is a separate collection from the 60-page Mainline `ALLHW/` dataset.

## 2. Mainline processing status

Status labels:

- **Extracted + QA**: full table extraction and explicit row/identifier checks documented.
- **Partial anchor**: used as a comparison source or reviewed selectively, but no complete annual extraction/QA is documented.
- **Not yet audited**: source exists, but current research documentation contains no evidence of a systematic annual-page extraction and QA.
- **Special handling required**: separate source variant must be compared independently.

| Year/source | Archive status | Research status | Audit conclusion |
|---|---|---|---|
| 1968 | Present | Extracted 16 rows from 1 product table (1968 Hot Wheels) and 26 separate gallery entries, including 23 catalogue-page images. 16 unique Toy # and model names; gallery captions/filenames/alt labels and links preserved; no structured release attributes. | Extracted + QA; product table and gallery retained separately |
| 1969 | Present | Extracted 24 rows across 2 product tables: 16 in 1969 Hot Wheels and 8 in Exclusive Grand Prix; 1 separate gallery entry. 24 unique Toy # and 24 unique model names; cross-listed series membership preserved; no structured release attributes. | Extracted + QA; two table scopes and gallery retained separately |
| 1970 | Present | No annual product table; extracted 37 gallery entries across Club Kit (3), Grand Prix (2), Heavyweights (6), Hot Wheels (19), Sky Show Set Only (2), and Spoilers (5). Captions, image filenames, alt labels and links preserved; no structured Toy # or release attributes. | Gallery inventory extracted + QA; not a structured annual product-table extraction |
| 1971 | Present | No annual product table; extracted 39 gallery entries across Hot Wheels Series (21), Heavyweights (7), Mongoose vs Snake (4), Spoilers (3), and Gallery (4). Image filenames, alt labels and links preserved; two catalog-gallery captions blank; structured release identifiers/attributes absent. | Gallery inventory extracted + QA; not a structured annual product-table extraction |
| 1972 | Present | No annual product table; extracted 7 gallery entries under New Castings. Image filenames, alt labels, file links and model-page links preserved; Toy # and structured release attributes absent. | Gallery inventory extracted + QA; not a structured annual product-table extraction |
| 1973 | Present | Archived page has no annual product table; extracted 34 gallery entries across New Release (3), Hot Wheels Series (21), and Shell Promo (10). Image filenames, alt labels, file links, and model-page links preserved; Toy # and other structured release attributes absent. | Gallery inventory extracted + QA; not a structured annual product-table extraction |
| 1974 | Present | Extracted 25 rows from 1 product table; 25 unique nonblank Toy #; no repeated Toy # or casting-name groups. Six-column source schema; Wheel Type and Photo metadata recovered from image alt labels / filenames; 24 rows assigned to 1974 Flying Colors and 1 to Mountain Mining Set; no Collector # or Series #. | Extracted + QA |
| 1975 | Present | Extracted 31 rows from 1 product table; 31 unique nonblank Toy #; no repeated Toy # or casting-name groups. Six-column source schema; Wheel Type and Photo metadata recovered from image alt labels / filenames; no Collector # or Series #. | Extracted + QA |
| 1976 | Present | Extracted 41 rows from 1 product table; 39 unique nonblank Toy #, 1 blank Toy #; 1 repeated Toy # group and 1 repeated casting-name group. Six-column source schema; no Collector # or Series #; source Notes retained. | Extracted + QA |
| 1977 | Present | Extracted 103 rows from 1 product table; 69 unique nonblank Toy #, 1 blank Toy #; 25 repeated Toy # groups and 29 repeated casting-name groups. Six-column source schema; no Collector # or Series #; Photo / Color values retained as color labels. | Extracted + QA |
| 1978 | Present | Extracted 54 rows from 3 product tables; 53 unique nonblank Toy #, 0 blank Toy #; 1 repeated Toy # groups and 1 repeated model-name groups. No Collector # or Series #; source schemas preserved. | Extracted + QA |
| 1979 | Present | Extracted 51 rows from 6 product tables; 46 unique nonblank Toy #, 4 blank Toy #; 1 repeated Toy # groups and 9 repeated model-name groups. Source schemas vary (9–10 columns); no Collector # or Series #. | Extracted + QA |
| 1980 | Present | 49 rows across 2 product tables; 42 unique nonblank Toy #; 3 blank Toy #; 4 repeated Toy # groups; 3 repeated casting-name groups | Extracted + QA |
| 1981 | Present | 27 rows across New Castings, Repaints, Scene Machines and Heroes; 23 unique nonblank Toy #; 1 blank Toy #; repeated Toy # and names preserved; no Collector # or Series #; Heroes has Original Casting/Year/Series Rename schema | Extracted + QA; source-specific schema and identifier collision flagged |
| 1982 | Present | 90 rows across New Castings, Reissues, Megaforce Series, HiRakers and Workhorses; 74 unique nonblank Toy #; 9 blank Toy #; repeated identifiers and names preserved; no Collector # or Series # | Extracted + QA; table schema differences and identifier collisions flagged |
| 1983 | Present | 67 rows across New Castings, Real Riders, Reissues, Extras Series and HiRakers; 51 unique nonblank Toy #; 7 blank Toy #; repeated identifiers and names preserved; no Collector # or Series # | Extracted + QA; source-table differences and identifier collisions flagged |
| 1984 | Present | 35 rows across New Castings, Real Riders, Ultra Hots and Reissues; 12-column and 11-column schemas; repeated Toy # 7293 in two Flame Runner variants; blank Toy # values retained | Extracted + QA; repeated identifiers and historical notes flagged |
| 1985 | Present | 38 rows across New Castings, Real Riders, Ultra Hots and Reissues; no Collector # or Series # columns; 12-column and 11-column schemas; blank Toy # values and repeated casting names preserved | Extracted + QA; source-scope variants and historical notes flagged |
| 1986 | Present | 26 rows across New Castings, Reissues and Real Riders; 20 unique Toy #; country and set-only qualifiers preserved | Extracted + QA; repeated Toy # and scope collisions flagged |
| 1987 | Present | 23 rows across New Castings, Reissues and Real Riders; 20 unique Toy #; no Collector # field | Extracted + QA; repeated Toy # variants flagged |
| 1988 | Present | 27 rows across New Castings and Reissues; 25 unique Toy #; no Collector # field; two Toy # values have two color variants each | Extracted + QA |
| 1989 | Present | One five-column annual table; 76 rows, Col. #001–076 and Series #1/76–76/76; no Toy # field | Extracted + QA |
| 1990 | Present | 87 rows across New Castings, Reissues, The Simpsons and California Customs; only New Castings has Collector # | Extracted + QA; repeated Toy # and blank Toy # rows flagged |
| 1991 | Present | 62 rows across New Castings, Reissues and California Customs; California Customs has separate no-Collector-# scope | Extracted + QA; blank and repeated identifiers flagged |
| 1992 | Present | 24 rows across New Castings, Reissues and Gleam Team; two source schemas; two Gleam Team Toy # values blank | Extracted + QA |
| 1993 | Present | 72 rows across five tables with distinct schemas; New Castings/Reissues, Tattoo Machines, Demolition Man and 25th Anniversary Series retain separate identifiers | Extracted + QA; duplicate/conflicting IDs and blanks flagged |
| 1994 | Present | 14 rows across two 12-column tables (New Models and Reissues); preserves detailed color, tampo, base/window/interior, wheel and Toy # fields | Extracted + QA; missing and suspicious fields flagged |
| 1995 | Present | 97 rows across 15 tables; 97 unique Toy # and Collector #; 12 Treasure Hunts; 1995 Hot Wheels has 7-column schema with Color and Rims | Extracted + QA |
| 1996 | Present | 141 rows across 17 product tables; 136 unique Toy # and Collector # values; two exact duplicate rows in 1996 Hot Wheels; 64-row five-column table omits Series # | Extracted + QA; duplicate rows and cross-scope Toy # collisions flagged |
| 1997 | Present | Numbered list: 119 rows, numeric Collector #147–642 (non-dense); Bonus Cars 4 rows (#001–004); seven other series tables: 28 rows with Collector # = N/A | Extracted + QA |
| 1998 | Present | 185 numbered-list rows, 184 unique Collector # values across 633–908; one repeated #780/Toy #19949 row; separate Bonus Cars 4 rows | Extracted + QA |
| 1999 | Present | 196 numbered-list rows with Collector #649–1121 (non-dense); separate Final Run (12 rows, Collector # blank) and Bonus Cars (4 rows, Toy # blank) | Extracted + QA |
| 2000 | Present | 249 rows across 17 tables; 245 distinct nonblank Toy #; Virtual Collection and Bonus Cars require separate identifier scopes; five numeric Collector # values absent | Extracted + QA |
| 2001 | Present | Mainline: 240 rows, Collector # 001–240; separate Final Run: 12 rows; Store Exclusives: 4 rows with identifiers blank in source | Extracted + QA |
| 2002 | Present | Annual Mainline: 240 rows, Collector # 001–240; separate Final Run table: 3 rows with its own Series # namespace; 2002 Hot Wheels uses five-column schema | Extracted + QA |
| 2003 | Present | 222 rows across 22 tables; Collector # 001–220 continuous; one 5-column table omits Series #; #035 has three color rows | Extracted + QA |
| 2004 | Present | 268 rows across 16 tables; Collector # 001–212 continuous plus separate 000 Mail-In; four tables use five-column schema without Series # | Extracted + QA |
| 2005 | Present | 288 rows across 19 tables; Collector # 001–187 continuous; 2005 Open Stock (86 rows) has a five-column schema without Series # | Extracted + QA |
| 2006 | Present | 363 rows across 17 tables; Collector # 001–223 continuous; 2006 Open Stock has 141 rows in a distinct five-column schema without Series # | Extracted + QA |
| 2007 | Present | 315 rows across 18 tables, 180 numeric Collector # positions (001–180); 193 unique Toy #; all 315 Series # cells contain zero-width Unicode | Extracted + QA |
| 2008 | Present | 358 rows across 18 tables, 196 numeric Collector # positions (001–196); 208 unique Toy #, repeated across color variants | Extracted + QA |
| 2009 | Present | Mainline: 342 rows across 14 tables, 190 numeric Collector #; Toy # repeats among color entries; 12 Redline/Goodyear exclusive rows are exact repeats | Extracted + QA |
| 2010 USA | Present | Extracted + QA: 440 source rows across 28 tables, 252 unique Toy #, 240 Collector #; includes Goodyear/BF Goodrich sections | Extracted + QA; cross-page adjudication pending |
| 2010 International | Present | Extracted + QA: 228 source rows across 24 tables, 226 unique Toy #, 214 Collector # | Extracted + QA; cross-page adjudication pending |
| 2011 | Present | Mainline: 429 rows across 21 tables, numeric Collector # 001–244; 20 additional Windshield Banner/Redline exclusive rows are exact repeats of Mainline rows | Extracted + QA |
| 2012 | Present | Mainline: 387 rows across 23 tables, numeric Collector # 001–247; two cross-listed exclusives tables add 20 rows; Year of the Dragon Edition adds 1 No # row | Extracted + QA |
| 2013 | Present | Mainline: 433 rows across 30 series tables, 250 numeric Collector #; Scavenger Hunts: 6 rows in separate Kroger-exclusive table, Collector # = No #; Mainline schema has no Series # column | Extracted + QA |
| 2014 | Present | Mainline: 433 rows across 32 series tables, 250 numeric Collector #; Scavenger Hunt: 4 rows in separate Kroger-exclusive table; one Mainline table lacks Series # column | Extracted + QA |
| 2015 | Present | Mainline: 433 rows across 34 series tables, 250 numeric Collector #; Scavenger Hunt: 4 rows in separate 6-column table, Collector # = No #; Mainline schema has no Series # column | Extracted + QA |
| 2016 | Present | Mainline: 433 rows across 31 series tables, 250 numeric Collector #; 8 Special Edition rows in 2 additional tables, Collector # = No #; 397 Series # cells contain zero-width Unicode | Extracted + QA |
| 2017 | Present | Mainline #1–365: 365 rows; additional separately headed sections: 85 rows across 9 sections, all Collector # = No # | Extracted + QA |
| 2018 | Present | Mainline #1–365: 365 rows; additional separately headed sections: 104 rows across 10 assortments/exclusives/chase tables, all Collector # = No # | Extracted + QA |
| 2019 | Present | Mainline: 447 rows, 447 unique Toy #, 250 numeric Collector #; separate unnumbered Special Editions: 2 rows with Collector # = No # | Extracted + QA |
| 2020 | Present | Mainline: 447 rows, 447 unique Toy #, 250 numeric Collector #; separate Hot Wheels id Chase Series: 8 rows with Collector # = No #; 2 broken Photo filename placeholders | Extracted + QA |
| 2021 | Present | Mainline: 447 rows, 447 unique Toy #, 250 numeric Collector #; separate Hot Wheels id: Chase Series table: 8 rows with Collector # = No # | Extracted + QA |
| 2022 | Present | Full table extracted and QA checked: 447 rows, 447 unique Toy #, 250 Collector #, 142 rows marked (2nd Color), 15 TH + 15 STH | Extracted + QA |
| 2023 | Present | Full table extracted and QA checked: 445 rows, 445 unique Toy #, 250 Collector #, 141 rows marked (2nd Color), 15 TH + 15 STH | Extracted + QA |
| 2024 | Present | Full table re-extracted and QA checked: 441 rows, 441 unique Toy #, 250 Collector #, 132 rows marked (2nd Color), 15 TH + 15 STH; 49 prior Car Culture name-match candidates remain unadjudicated | Extracted + QA |
| 2025 | Present | Full extraction and QA documented: 440 rows, 440 unique Toy #, 250 Collector #, 146 rows marked (2nd Color); Premium comparisons completed | Extracted + QA |
| 2026 | Present | Full table extracted and QA checked: 440 rows, 440 unique Toy #, 250 Collector #, 137 rows marked (2nd Color), 15 TH + 15 STH | Extracted + QA |

**Important qualification:** “Not yet audited” means the current research documentation does not demonstrate a complete annual extraction and QA. It does not mean nobody has ever opened or inspected the page. Research of individual castings/series elsewhere in the archive does not count as extraction of the corresponding annual Mainline list.

### 2025 verified extraction

Source: `ALLHW/2025/List of 2025 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`

- Git blob SHA: `b155324bd3fca3281ed91fd7a8fa992e04f1662f`
- File size: 824,886 bytes
- Manifest SHA-256: `bbdac9d328130734328c1bb9b8a01fc738055dd596f0b7dfcf286ae5b142672c`
- Extracted rows: 440
- Unique Toy #: 440
- Unique Collector #: 250
- Rows marked `(2nd Color)`: 146

Detailed extraction QA and Mainline/Premium candidate comparisons are recorded in `research/comparisons/MAINLINE-PREMIUM-2025.md`.

### 2024 extraction status

The 2024 annual list has now been re-extracted from the canonical archive branch and passed structural QA. Results, provenance, and the machine-readable row export are recorded in `research/extractions/MAINLINE-2024-EXTRACTION-QA.md` and `research/extractions/MAINLINE-2024.csv`. The prior 49 Car Culture exact-name matches remain candidate links only; they still require row-level adjudication for casting/tooling identity.

## 3. Mainline work remaining

Priority order:

1. Annual Mainline source review and extraction for 1968–2026 is complete. 1970, 1971, 1972 and 1973 are gallery-only and need cross-source enrichment if structured release data is required. The 1997–2026 annual sources have been extracted/QA-checked; 2010 ordinary and International lists are separate, independently processed datasets.
2. Adjudicate the 2010 USA/International comparison: investigate 21 shared-Toy# model-name discrepancies, 13 International-only and 39 USA-only Toy # values, and the 18 USA tire-exclusive section rows.
3. Resolve year-specific anomalies already recorded for 1997–2009 (sparse Collector # ranges, repeated Toy #/Collector # values, separate program scopes, blank identifiers and schema differences).
4. Adjudicate the existing 49 Car Culture ↔ Mainline 2024 name-match candidates against the canonical 2024 extraction. Preserve the comparison as a separate run; name matches are not casting/tooling proof.
5. Adjudicate 2026 source notes and compare against adjacent annual lists; the 2026 annual table extraction and structural QA are complete.
6. Build year-scoped cross-program comparisons only after the relevant annual Mainline sources have verified extraction. Do not infer a match in another year from the 2024/2025 samples.

For every annual page, record source path, branch, Git blob SHA, manifest SHA-256, Fandom revision/date if available, extraction method/version, table boundaries, row counts, unique identifier counts, duplicate groups, and unresolved anomalies.

### 2010 dual-page extraction status

Both 2010 pages have been independently extracted and QA-checked. The exports preserve table index, section heading, row position, all six source columns, and the raw Collector-column header. The cross-page analysis is documented in `research/comparisons/MAINLINE-2010-USA-INTERNATIONAL.md`. Shared Toy # values are candidates only; Collector # values differ between the page scopes and must not be merged.

## 4. Data-model and QA cautions

- Mainline Toy # and Collector # are different identifier namespaces. Collector # is not a unique release key: regular and STH rows may share it.
- Color variants can have distinct Toy # while sharing Collector #; preserve raw labels such as `(2nd Color)`.
- Keep annual list row identity separate from casting identity and from the physical release/product identity.
- Treat regional/international lists as separate source scopes until compared.
- Do not treat the annual page's row count as the number of unique castings.
- Keep source assertions and uncertainty explicit; exact name matches do not prove casting/tooling identity.

## 5. Archive-wide inventory checkpoint

The Fandom archive tree currently contains 530 HTML/HTM files and 2 CSV files. This audit does not yet assign a final processing status to every Fandom HTML page. That is the next inventory phase, after Mainline. The planned next scope is Early Collections, Early Special Series, Other Early Series, then the remaining modern categories. Folder taxonomy is an archival organization, not a verified product hierarchy.


## 6. Early Collections processing checkpoint

The Early Collections archive folder has been inventoried: 33 HTML/HTM pages totaling 12,834,928 bytes. The per-file inventory, Git blob SHAs, sizes, and processing states are tracked in `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`. The folder label is treated as archival provenance, not a verified product hierarchy.

The first page, Action Command, has been fully extracted and structurally QA-checked:
- Source: `Early Collections/Action Command _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `aac8bef248329166dd47ca7387d31dd6a89c3b1d`
- Manifest SHA-256: `85E2322618CE94656A090644CD477C0613E2931791FEC17479155CD2DF2B4F85`
- 2 source tables and 38 product rows: Original Card (8), 1987-1989 Card (30).
- Export: `research/extractions/EARLY-COLLECTIONS-ACTION-COMMAND.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-ACTION-COMMAND-EXTRACTION-QA.md`
- Repeated Toy # groups are preserved as separate rows; no automatic identity or release merging was performed.

Next: continue with the remaining Early Collections pages in inventory order, recording each page's source structure and QA before drawing any cross-page conclusions.


### Boss Hoss extraction checkpoint

- Source: `Early Collections/Boss Hoss _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `3a7cb7b9e5e4e65c0a9e6a0d671fc6422014119f`
- Manifest SHA-256: `A84EF7E02BB4A05426369C3F09089B113C4DB3B01CFDCE2F1FD447DB7A5266B0`
- 2 product tables, 33 product rows: Original Versions (23), Retooled Versions (10).
- 22 gallery items were extracted as separate source records.
- The original table's Toy # 6499 occurs in 23 distinct rows. All variants remain separate; no deduplication was performed.
- Export: `research/extractions/EARLY-COLLECTIONS-BOSS-HOSS.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-BOSS-HOSS-EXTRACTION-QA.md`
- Processing index: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`


### Classics extraction checkpoint

- Source: `Early Collections/Classics _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `81cdb2bcc7ce2505b2ce3b11f2a533475401e8a7`
- Manifest SHA-256: `5507F2B9D4E6443ABF7F36D2E63F7EA0FD23D5FEC50A3CD899B5324848867084`
- 1 product table, 25 product rows, 9 source columns; years 1987–1989.
- 14 distinct model names and 17 distinct Toy # values. Eight Toy # groups repeat across separate rows; all variants retained.
- Loose and carded photo filenames and alt labels extracted separately. No separate gallery section was detected.
- Export: `research/extractions/EARLY-COLLECTIONS-CLASSICS.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-CLASSICS-EXTRACTION-QA.md`


### Classy Customs extraction checkpoint

- Source: `Early Collections/Classy Customs _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e6abb91ef7ee6140ac65220a5aaef8b33a07f72a`
- Manifest SHA-256: `07E1C1AF03D7D807AD4CD5BB1B0C00F2BC638F79F4BDCC3C1BAE80B9662CACF7`
- 1 product table, 12 product rows, 9 source columns, plus 2 separate gallery entries. Fandom revision 767675.
- 12 distinct Toy # values and 12 distinct Collector # values. Source page contains no Year column; none was inferred.
- Loose/card images and patch-card front/back gallery references retained separately.
- Export: `research/extractions/EARLY-COLLECTIONS-CLASSY-CUSTOMS.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-CLASSY-CUSTOMS-EXTRACTION-QA.md`


### Drag Strippers extraction checkpoint

- Source: `Early Collections/Drag Strippers _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `4a562feebe3ee01403ae956cae9ba6757081f205`
- Manifest SHA-256: `A752A325B728240B9F62AD5139638C51965E6CE8747EFC4D6593B5E7B21E9125`
- Fandom revision 767718; 1 product table, 17 product rows, 9 source columns, plus 2 gallery entries.
- 15 distinct Toy # values, 15 distinct Collector # values and 15 vehicle names. Toy # 2508 / Collector # 34 and Toy # 9646 / Collector # 30 each occur twice; all variant rows retained.
- No Year column exists. Final Vetty Funny carded-image source entry `Image Not Available.jpg` preserved as source data.
- Export: `research/extractions/EARLY-COLLECTIONS-DRAG-STRIPPERS.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-DRAG-STRIPPERS-EXTRACTION-QA.md`


### Evil Weevil extraction checkpoint

- Source: `Early Collections/Evil Weevil _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `1f58c9c929ca5529421d7e689e5fadcf1ce487ec`
- Manifest SHA-256: `A2EDF78C5FD36806E25888CC4B2FF5E4C509AF8D4C51F5F5E6051BC7A4F54C91`
- Fandom revision 772324; 2 product tables: Original Versions (8 rows, 12 columns) and Retooled Versions (5 rows, 12 columns); 24 separate gallery entries.
- 13 product rows total; six distinct Toy # values. Toy # 6471 occurs in eight original-version rows and is retained as eight distinct source records.
- Original Versions `Stickers` and Retooled Versions `Tampo` are preserved as separate fields. Years are 1971, 2004, 2005, 2006, 2008 and 2009.
- Export: `research/extractions/EARLY-COLLECTIONS-EVIL-WEEVIL.csv`
- QA: `research/extractions/EARLY-COLLECTIONS-EVIL-WEEVIL-EXTRACTION-QA.md`


### Extras extraction checkpoint

- Source: `Early Collections/Extras _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `e2a591a06e8ae39a455dc264e8cb8c6543c6536b`; manifest SHA-256 `D348DC5A136C715B5C5DE7DE3289ECDCAE3DEEE91DE49523B4FF8005F4F65A66`; Fandom revision 765024.
- One product table, 9 rows and 11 source columns. Loose and carded photo references were retained separately.
- Repeated Toy # groups: [["4342",2],["5905",2]]. All source rows remain distinct.
- Export: `research/extractions/EARLY-COLLECTIONS-EXTRAS.csv`; QA: `research/extractions/EARLY-COLLECTIONS-EXTRAS-EXTRACTION-QA.md`.


### Flying Colors extraction checkpoint

- Source: `Early Collections/Flying_Colors.htm`; Git blob SHA `7416dad03fc92b77384fc132e0001366744148ac`; manifest SHA-256 `40EA1A76B9A5C2890E2D6439D2033651EE819CC02C00BA5CB51B9D7E6241EFB2`; Fandom revision 795936.
- Five annual product tables (1974–1978), 212 rows. The separate Track Sets heading has no product table and was not merged into annual rows.
- Source schemas differ across years; original headers and row values are preserved. Loose and carded photo references are extracted separately.
- Export: `research/extractions/EARLY-COLLECTIONS-FLYING-COLORS.csv`; QA: `research/extractions/EARLY-COLLECTIONS-FLYING-COLORS-EXTRACTION-QA.md`.


### Flying Colors extraction refinement

- The CSV now retains cell-level image metadata, including wheel-type images that appear in the Wheel Type column rather than as text. Loose and carded photo metadata remain separate.
- The Track Sets section contains a separate Thundershift 500 reference, exported as a non-product `section_reference` row.
- Five annual tables remain 212 product rows for 1974–1978. No product rows were merged.


### Grand Prix extraction checkpoint

- Source: `Early Collections/Grand Prix _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `d23ef8f6f24209353e1c8e9af4c8861fd5d7c25a`; manifest SHA-256 `EEF2D22944167C610616C489E96A80D6261426CDC377E264CCBE99B09061C621`; Fandom revision 787981.
- The page contains a visual image/caption grid under The Cars rather than a conventional product-data table: 11 vehicle captions and 11 associated image references. One separate Gallery item is retained.
- Captions and paired image metadata are exported in source order. No Toy #, casting, release or package facts were inferred.
- Export: `research/extractions/EARLY-COLLECTIONS-GRAND-PRIX.csv`; QA: `research/extractions/EARLY-COLLECTIONS-GRAND-PRIX-EXTRACTION-QA.md`.


### Heavy Chevy extraction checkpoint

- Source: `Early Collections/Heavy Chevy _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `1b710580762e9947170e92376c9410c4c8683d92`; manifest SHA-256 `8A478082427112ABDCAAF759187D4D4D799973E821ED61DB3F50F96A3A0A1A76`; Fandom revision 808320.
- Four product tables (Versions, 100% Versions, Retooled Versions, Code 3), 44 product rows, and 33 separate Gallery references.
- Table schemas, source order, raw cell values, cell-level image metadata and gallery image references are retained. No repeated Toy # rows were merged.
- Export: `research/extractions/EARLY-COLLECTIONS-HEAVY-CHEVY.csv`; QA: `research/extractions/EARLY-COLLECTIONS-HEAVY-CHEVY-EXTRACTION-QA.md`.


### Heavyweights extraction checkpoint

- Source: `Early Collections/Heavyweights _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `03da68718f75d6951cb802b9c3aa11e949a0d89f`; manifest SHA-256 `69DC67CEF81E13FD6D5D11BE08F6B1AA07F49DA0EBE768D77C103A72B031F8F9`; Fandom revision 767901.
- The page has no conventional product table; 13 gallery references were extracted. Six appear under Castings In Series without an explicit year heading; seven appear under 1971.
- Image metadata, links and source order are retained. No missing product facts or years were inferred.
- Export: `research/extractions/EARLY-COLLECTIONS-HEAVYWEIGHTS.csv`; QA: `research/extractions/EARLY-COLLECTIONS-HEAVYWEIGHTS-EXTRACTION-QA.md`.


### HiRakers extraction checkpoint

- Source blob SHA `15ce02f85796913b6b1cd9f27b66348f9416e18e`; manifest SHA-256 `071EB7131AACB81DEE42E1AFF777F64D523B1C516810A751885B1AA82CAD5D9A`; Fandom revision 798213.
- Extracted 16 product rows from one 10-column table and 2 separate gallery references. Years: 1980, 1981, 1982, 1983, 1984.
- Repeated Toy # records, raw cells, image metadata and links preserved without deduplication.
- Export: `research/extractions/EARLY-COLLECTIONS-HIRAKERS.csv`; QA: `research/extractions/EARLY-COLLECTIONS-HIRAKERS-EXTRACTION-QA.md`.


### Hot Wheels 30th Anniversary 4-Car Set extraction checkpoint

- Source blob SHA `b278df831c1539c16f123cf442511afe4892015e`; manifest SHA-256 `1A7A32445EFD2DD2A1C54EF53D7ACFFB4B7549C92C59B41666162B6A464B3623`; Fandom revision 805834.
- Extracted four vehicle rows from one 11-column table. A source cell labeled Year contains 19322 and spans all four rows; kept verbatim and explicitly not interpreted as a calendar year. Toy # is separately 19322 in each row.
- Raw source cells, rowspan semantics, model links and photo metadata retained without deduplication.
- Export: `research/extractions/EARLY-COLLECTIONS-30TH-ANNIVERSARY-4-CAR-SET.csv`; QA: `research/extractions/EARLY-COLLECTIONS-30TH-ANNIVERSARY-4-CAR-SET-EXTRACTION-QA.md`.


### King Kuda extraction checkpoint

- Source: `Early Collections/King Kuda _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `5a5572d63d083f36a105c7b810728a7d02134c6d`; manifest SHA-256 `E8D78A5DA662670E38C7EB158A176E1E348FCFD414894BFA5F8E6B6C02EFED5D`; Fandom revision 795222.
- Extracted 44 product rows across four tables (Original Versions 9, 100% Versions 1, Retooled Versions 23, Code 3 11) and 55 separate Gallery references.
- The table schemas differ; Stickers, Tampo, Body Color and Quantity remain source-specific fields. 33 populated Toy # cells have 22 distinct values; repeated Toy # groups 6190 (8 rows) and L0738 (5 rows) were retained without deduplication.
- Source order, raw headers/cells, row HTML, per-cell image metadata and gallery file references are retained.
- Export: `research/extractions/EARLY-COLLECTIONS-KING-KUDA.csv`; QA: `research/extractions/EARLY-COLLECTIONS-KING-KUDA-EXTRACTION-QA.md`.


### Light My Firebird extraction checkpoint

- Source: `Early Collections/Light My Firebird _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `49971146f54ec92309098b45b9d807ab13d94ff4`; manifest SHA-256 `2FC6D29B2DA88A39FB0238B613C787726AC3B8854A21DEB64AF156481CB82412`; Fandom revision 801165.
- Extracted 20 product rows from three tables (Original Versions 10, 100% Versions 6, Retooled Versions 4), plus 13 separate Gallery references.
- 20 populated Toy # cells have 9 distinct values. Repeated groups 6408 (10 rows), 22055 (2), and 56579 (2) were retained separately.
- Source schemas, raw row data, image metadata, gallery captions and file links preserved.
- Export: `research/extractions/EARLY-COLLECTIONS-LIGHT-MY-FIREBIRD.csv`; QA: `research/extractions/EARLY-COLLECTIONS-LIGHT-MY-FIREBIRD-EXTRACTION-QA.md`.


### Megaforce Series extraction checkpoint

- Source: `Early Collections/Megaforce_Series.htm`; Git blob SHA `ddf69edec1c115ae4079644863a6f461814d6f98`; manifest SHA-256 `690A77F696BFA4E38BA07B8022117EA3F727EE7AFFA1266D780D2F8D65C5006D`; Fandom revision 714197.
- Extracted 7 product rows from one 8-column table. Toy # 5270 appears twice for Personnel Carrier variants and both rows are preserved separately.
- Photo Loose and Photo Carded image metadata, original headers, raw cells, cell HTML and model links are retained. No separate standard Fandom gallery items were present.
- Export: `research/extractions/EARLY-COLLECTIONS-MEGAFORCE-SERIES.csv`; QA: `research/extractions/EARLY-COLLECTIONS-MEGAFORCE-SERIES-EXTRACTION-QA.md`.


### Nitty Gritty Kitty extraction checkpoint

- Source: `Early Collections/Nitty Gritty Kitty _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `fe1c9f1b2220692cd1c0f08cac45d1e698742831`; manifest SHA-256 `763DEED3E9D77A620457B20C02E82066BE2B5496831BAEF6776BADC73604EA1C`; Fandom revision 813920.
- Extracted 18 product rows across 3 tables, plus 24 Gallery items. Combined CSV records: 42.
- Preserved table-specific source schemas, source order, raw cells, links and per-cell image metadata; Gallery captions, image filenames and file links are separate records.
- Export: `research/extractions/EARLY-COLLECTIONS-NITTY-GRITTY-KITTY.csv`; QA: `research/extractions/EARLY-COLLECTIONS-NITTY-GRITTY-KITTY-EXTRACTION-QA.md`.


### Oldies But Goodies extraction checkpoint

- Source: `Early Collections/Oldies But Goodies _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `d8bac5f967b3a4dd0b0baf79c8708414318fac53`; manifest SHA-256 `B8CA045892B79F667D6333B3F65DC19C1150A246C075DC5C3002AF0AEB5A28CA`; Fandom revision 767721.
- Extracted 8 product rows from one 9-column source table and 2 separate Gallery records, for 10 CSV records. All eight Toy # values are populated and distinct.
- Preserved source headers/cells, raw cell HTML, links, cell-level image metadata, and the separate patch/card gallery references. No rows were deduplicated and no identity relationships inferred.
- Export: `research/extractions/EARLY-COLLECTIONS-OLDIES-BUT-GOODIES.csv`; QA: `research/extractions/EARLY-COLLECTIONS-OLDIES-BUT-GOODIES-EXTRACTION-QA.md`.


### Real Riders extraction checkpoint

- Source: `Early Collections/Real Riders _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `f5da19e889612b3922c10500d86640aa2b17071f`; manifest SHA-256 `599AB0B87CF730E3F5158F7417819B206302C59C5DA3B51DCB61BE2C39E09891`; Fandom revision 813974.
- The page has no product tables and no standard Wikia gallery. Extracted 5 article-text records, 13 linked references, 1 prototype-tire illustration, and all 12 slideshow images (31 records total).
- Images and links are preserved as source references, not converted into release records. No casting, release, package or wheel variant identities were inferred.
- Export: `research/extractions/EARLY-COLLECTIONS-REAL-RIDERS.csv`; QA: `research/extractions/EARLY-COLLECTIONS-REAL-RIDERS-EXTRACTION-QA.md`.


### Rescue Team extraction checkpoint

- Source: `Early Collections/Rescue Team _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `e131d541f95be40ae587be0c90596a18faaf62c9`; manifest SHA-256 `E3181E548EBF2A393DF6191CC983C6C6FF23431572633BFA1BF339F0C499588C`; Fandom revision 767735.
- Extracted 6 product rows from one 9-column table and 2 separate Gallery references (8 CSV records total).
- All six Toy # values are populated and unique: 7665, 7650, 2639, 9640, 2019, 7661. Six distinct vehicle-name labels; Toy # and Collector # retained as separate fields.
- Source headers, raw cells, cell HTML, model links, loose/carded image metadata, gallery captions and file links preserved. No product rows merged and no product identities inferred from images.
- Export: `research/extractions/EARLY-COLLECTIONS-RESCUE-TEAM.csv`; QA: `research/extractions/EARLY-COLLECTIONS-RESCUE-TEAM-EXTRACTION-QA.md`.


### Speed Demons extraction checkpoint

- Source: `Early Collections/Speed Demons _ Hot Wheels Wiki _ Fandom.html`; Git blob SHA `bf6c7dca8fae920b5c79db2c787fd3f70460b900`; manifest SHA-256 `6AB1727440FE886C5BAD79754FB86AFF03AE691F9C1E61851544F0C4E5746898`; Fandom revision 726384.
- Extracted 22 product rows across two tables: 1986 Original Card (6 rows, 9 columns) and 1987–1989 Card (16 rows, 10 columns). The later table has an additional Year column.
- All 22 Toy # cells are populated; 11 distinct Toy # values and 11 distinct model-name labels. Repeated Toy # and model-name groups were preserved as source rows, not deduplicated.
- No standard Wikia gallery items; loose/carded imagery is embedded in product-table cells. Raw headers/cells, cell HTML, links, and image metadata retained.
- Export: `research/extractions/EARLY-COLLECTIONS-SPEED-DEMONS.csv`; QA: `research/extractions/EARLY-COLLECTIONS-SPEED-DEMONS-EXTRACTION-QA.md`.


### Early Collections update: Speed Fleet
- Processing status: 22 of 33 pages extracted and QA-reviewed.
- Speed Fleet: 76 product rows from two card-specific tables; 152 embedded image references; no standard gallery items. Source rows and repeated identifiers preserved.
- Outputs: `research/extractions/EARLY-COLLECTIONS-SPEED-FLEET.csv` and `research/extractions/EARLY-COLLECTIONS-SPEED-FLEET-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


### Early Collections update: Speed Machines (1983)
- Processing status: 23 of 33 pages extracted and QA-reviewed.
- Speed Machines (1983): 27 product rows in one 6-column Versions table, plus 1 separate Gallery record. The source table has no Toy # or Year columns; original source structure retained.
- Outputs: `research/extractions/EARLY-COLLECTIONS-SPEED-MACHINES-1983.csv` and `research/extractions/EARLY-COLLECTIONS-SPEED-MACHINES-1983-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


### Early Collections update: Speedway Specials
- Processing status: 24 of 33 pages extracted and QA-reviewed.
- Speedway Specials: 17 product rows from one 9-column table, plus 2 separate Gallery items (19 CSV records). The table has no Year column; article prose identifies the Patch Card mail-away theme as produced in 1978 and 1979.
- 14 distinct Toy # values; repeated Toy # groups 17, 21 and 38 and repeated model labels remain separate source rows. 34 table-cell image references and 2 unique Gallery image assets retained.
- Outputs: `research/extractions/EARLY-COLLECTIONS-SPEEDWAY-SPECIALS.csv` and `research/extractions/EARLY-COLLECTIONS-SPEEDWAY-SPECIALS-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


### Early Collections update: Sugar Caddy
- Processing status: 25 of 33 pages extracted and QA-reviewed.
- Sugar Caddy: 16 product rows across three source tables (Original Versions 12, CIPSA Versions 3, Retooled Versions 1) with different schemas; plus 4 separate Gallery records (20 CSV records total).
- Toy # is present in 13 rows; 6418 repeats 12 times and P2141 appears once. CIPSA has no Toy # or Year columns. 17 embedded image references and 4 gallery assets retained.
- Outputs: `research/extractions/EARLY-COLLECTIONS-SUGAR-CADDY.csv` and `research/extractions/EARLY-COLLECTIONS-SUGAR-CADDY-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


### Early Collections update: Super Chromes (1976)
- Processing status: 26 of 33 pages extracted and QA-reviewed.
- Super Chromes: 46 product rows across three year-specific tables (1976: 25; 1977: 19; 1978: 2), plus 4 separate Gallery records (50 CSV records total).
- All 46 rows have Toy #; 13 distinct values. Repeated Toy # values remain separate source records; 9505 appears 12 times. 46 embedded image references and 4 gallery assets retained.
- Outputs: `research/extractions/EARLY-COLLECTIONS-SUPER-CHROMES-1976.csv` and `research/extractions/EARLY-COLLECTIONS-SUPER-CHROMES-1976-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


### Early Collections update: Super Streeters
- Processing status: 27 of 33 pages extracted and QA-reviewed.
- Super Streeters: 13 product rows from one 9-column table, plus 8 separate Gallery records (21 CSV records). No Year column; Photo Loose/Carded cells are blank.
- 11 distinct Toy # values (9241 repeated 3 times), 10 distinct Collector # values (59 repeated 3 times, 36 twice). Repeated model names preserved. Eight separate gallery entries retained.
- Outputs: `research/extractions/EARLY-COLLECTIONS-SUPER-STREETERS.csv` and `research/extractions/EARLY-COLLECTIONS-SUPER-STREETERS-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


### Early Collections update: TNT-Bird
- Processing status: 28 of 33 pages extracted and QA-reviewed.
- TNT-Bird: 11 Original Versions rows and 3 Re-Tooled Versions rows across two separate 12-column tables, plus 8 separate Gallery records (22 CSV records). Both tables retain year, series, color/trim, wheel, Toy #, country, notes and photo fields.
- Repeated source tables remain separate; article-level metadata headings are not misrepresented as product data. Eight gallery assets and file links retained.
- Outputs: `research/extractions/EARLY-COLLECTIONS-TNT-BIRD.csv` and `research/extractions/EARLY-COLLECTIONS-TNT-BIRD-EXTRACTION-QA.md`; detailed progress: `research/EARLY-COLLECTIONS-PROCESSING-INDEX.md`.


## 6. Early Collections extraction progress

The archived `Early Collections/` inventory contains 33 HTML/HTM source pages. As of this audit update, 29 of 33 pages have been extracted and QA-reviewed. The Heavies is included in the completed set.

- The Heavies: 1 product table, 7 product rows, 9 source columns; all 7 Toy # and all 7 Collector # values populated and unique; 2 separate Gallery items; 14 embedded image references retained in the Photo Loose and Photo Carded cells (two per product row); image metadata is retained separately.
- Output: `research/extractions/EARLY-COLLECTIONS-THE-HEAVIES.csv`.
- QA: `research/extractions/EARLY-COLLECTIONS-THE-HEAVIES-EXTRACTION-QA.md`.
- Remaining unprocessed Early Collections pages: 5. Continue using the processing index for the next source and preserve source organization as provenance, not canonical product taxonomy.


## 7. Early Collections extraction progress update

The archived `Early Collections/` inventory contains 33 HTML/HTM pages. 32 of 33 pages have now been extracted and QA-reviewed.

### The Hot Ones (1981)
- One archived source page, Fandom revision 811612.
- Three product tables: Vehicles (90 rows), Patch Card 3-Pack (3 rows), Stamper 3-Pack (4 rows), total 97 product rows.
- Vehicles: 90 populated Toy # cells, 38 distinct values; 27 repeated Toy # groups are preserved as individual source rows, including country-specific entries.
- 20 separate Gallery items and 189 embedded product-table image references.
- Total extraction output: 117 CSV records.
- Output: `research/extractions/EARLY-COLLECTIONS-THE-HOT-ONES-1981.csv`.
- QA: `research/extractions/EARLY-COLLECTIONS-THE-HOT-ONES-1981-EXTRACTION-QA.md`.
- One Early Collections page remains unprocessed. Continue from the processing index; preserve each source table and gallery as separate evidence.


### Trailbusters
- Processing status: 31 of 33 Early Collections pages extracted and QA-reviewed.
- Source: `Early Collections/Trailbusters _ Hot Wheels Wiki _ Fandom.html`; Fandom revision 763267; source size 395,265 bytes.
- One unheaded 9-column product table, 49 rows. 18 distinct Toy # values; 17 repeated Toy # groups preserved separately. 97 embedded image references retained in Photo Loose/Carded cells; no separate standard Gallery items detected.
- Output: `research/extractions/EARLY-COLLECTIONS-TRAILBUSTERS.csv` (49 records).
- QA: `research/extractions/EARLY-COLLECTIONS-TRAILBUSTERS-EXTRACTION-QA.md`.
- Two Early Collections pages remain unprocessed: Ultra Hots Series (1984) and Workhorses.


### Ultra Hots Series (1984)
- Processing status: 32 of 33 Early Collections pages extracted and QA-reviewed.
- Six source product tables (1984, 1985, 1986, Stamper 3-Pack, 4-Pack, Gift Pack), 26 product rows total. 44 embedded image references retained at cell level; no separate standard Gallery items detected.
- Table schemas remain distinct; source-specific pack fields and variable row cell counts are preserved without inferred padding.
- Output: `research/extractions/EARLY-COLLECTIONS-ULTRA-HOTS-SERIES-1984.csv` (26 records).
- QA: `research/extractions/EARLY-COLLECTIONS-ULTRA-HOTS-SERIES-1984-EXTRACTION-QA.md`.
- One Early Collections page remains unprocessed: Workhorses.


### Workhorses
- Processing status: 33 of 33 Early Collections pages extracted and QA-reviewed. This completes the archived Early Collections page set.
- Source: `Early Collections/Workhorses _ Hot Wheels Wiki _ Fandom.html`; Fandom revision 767851; source size 485,493 bytes.
- Two source product tables: Original Card (37 rows) and 87-89 Card (49 rows), 86 product rows total.
- 86 populated Toy # cells across 40 distinct values; 27 repeated Toy # groups preserved individually. 34 distinct model-name labels.
- 172 embedded image references retained in source cells; no separate standard Gallery items detected. Original table schemas and raw row/cell evidence retained.
- Output: `research/extractions/EARLY-COLLECTIONS-WORKHORSES.csv` (86 records).
- QA: `research/extractions/EARLY-COLLECTIONS-WORKHORSES-EXTRACTION-QA.md`.
- Early Collections archive extraction is now complete: 33/33 pages.


## 8. Modern Special Series archive inventory

- Initial inventory completed: 223 archived HTML pages, 92,291,750 bytes total (88.02 MiB).
- Sources are distributed across 151 immediate source folders, including several large multi-year families. Folder names are retained as provenance and are not canonical product taxonomy.
- Seventeen of 223 pages have now been extracted and QA-reviewed. Processing proceeds in batches with per-page extraction and QA.
- Detailed inventory: `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.


### Modern Special Series: 100% Hot Wheels 1:43 Scale
- First page extracted and QA-reviewed: one product table, 13 rows, 6 columns, 26 embedded image references.
- Output: `research/extractions/MODERN-SPECIAL-SERIES-100-PERCENT-HOT-WHEELS-1-43-SCALE.csv`; QA: `research/extractions/MODERN-SPECIAL-SERIES-100-PERCENT-HOT-WHEELS-1-43-SCALE-EXTRACTION-QA.md`.
- Modern Special Series index: `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.


### Modern Special Series: 100% Hot Wheels 40th Anniversary
- Page extracted and QA-reviewed: 10 product tables, 39 product rows, 58 embedded image references.
- Named Single Cars and 2-Car Set sections retained as separate source tables; navigation tables excluded.
- Outputs: `research/extractions/MODERN-SPECIAL-SERIES-100-PERCENT-HOT-WHEELS-40TH-ANNIVERSARY.csv` and `research/extractions/MODERN-SPECIAL-SERIES-100-PERCENT-HOT-WHEELS-40TH-ANNIVERSARY-EXTRACTION-QA.md`.


### Modern Special Series batch: 100% Preferred and 1999-2002
- Five additional pages extracted and QA-reviewed, bringing Modern Special Series progress to 7 of 223 pages.
- 100% Preferred: 17 product tables, 127 rows, 254 embedded image references, and 23 separate Gallery items. 67 distinct Toy # values; repeated values and repeated casting labels remain separate source rows.
- 1999 Cool Collectibles: 1 table, 16 rows, 16 image references; 8 distinct Toy # values.
- 2000 Cool Collectibles: 1 table, 61 rows, 122 image references; 32 distinct Toy # values.
- 2001 100% Hot Wheels: 1 table, 49 rows, 49 image references; 37 distinct Toy # values.
- 2002 100% Hot Wheels: 1 table, 32 rows, 33 image references; Collector # and Toy # retained separately.
- All ten CSV and QA outputs were re-fetched from GitHub and verified for non-empty content and expected structure.
- Detailed source-level counts and links are recorded in `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.

### Modern Special Series batch: 2003-2006 and 1:43 Scale
- Five additional pages extracted and QA-reviewed, bringing Modern Special Series progress to 12 of 223 pages.
- 2003 100% Hot Wheels: 1 table, 33 rows, 33 image references.
- 2004 Showcase Hot Wheels: 9 tables, 70 rows, 140 image references, 33 separate Gallery items.
- 2005 Showcase Hot Wheels: 4 tables, 22 rows, 22 image references.
- 2006 Kalifornia Kustoms: 1 table, 12 rows, 24 image references, 4 separate Gallery items.
- Hot Wheels Collectibles 1:43 Scale: 3 tables, 23 rows, 46 image references.
- All ten CSV and QA outputs were re-fetched from GitHub and verified for non-empty content and expected structure.
- The complete `100% Hot Wheels` source folder is now extracted and QA-reviewed: 12 of 12 pages.
- Detailed source-level counts and output paths are recorded in `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.


### Modern Special Series batch: 2027 Racing Culture, 24/Seven, and AcceleRacers
- Five additional pages extracted; total progress is now 17 of 223 pages.
- 2027 Racing Culture: 4 tables, 12 rows, 20 embedded image references. One table has no detected headers and is flagged for semantic review.
- 24/Seven: 2 tables, 33 rows, 32 embedded image references, 44 separate Gallery items. One unheaded table retained for review.
- AcceleRacers (figure series): 4 tables, 20 rows, 20 embedded image references, 8 Gallery items.
- AcceleRacers Coin Bank: 1 table, 4 rows, 1 embedded image reference; table is unheaded and flagged for semantic review.
- AcceleRacers Collectible Card Game: 2 tables, 279 rows (4 Releases and 275 Cards), 554 embedded image references, 2 Gallery items.
- CSV and QA files were created for all five pages. Each page-level QA records source path, Git blob SHA, manifest SHA-256, source size, table boundaries, and extracted counts.
- Detailed source-level records: `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.


### Modern Special Series batch: AcceleRacers 2005/2006/2025, Airy 8, Anteater
- Five more pages extracted and QA-reviewed; progress is now 22 of 223 pages.
- AcceleRacers 2005: 5 tables, 51 rows, 91 embedded image references, 13 Gallery items.
- AcceleRacers 2006: 7 extracted tables, 33 rows, 66 embedded image references; one small table fell below the two-data-row extraction threshold and is flagged for review.
- AcceleRacers 2025: 2 tables, 7 rows, 10 embedded image references, 3 Gallery items; one table under a Gallery heading is preserved as source table data pending semantic review.
- Airy 8: 1 table, 16 rows, 15 embedded image references, 6 Gallery items.
- Anteater: 1 table, 9 rows, 9 embedded image references.
- All ten CSV and QA files were re-fetched from GitHub and verified non-empty.
- Detailed source-level counts and output paths are recorded in `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.


### Modern Special Series batch: Auto Affinity, Bassline, Boulevard 2012/2013/2020
- Five pages extracted and QA-reviewed; total progress is now 27 of 223.
- Auto Affinity: 10 tables, 73 rows, 146 embedded image references; CSV in three parts.
- Bassline (Crashers): one valid single-row Versions table (11 columns), one embedded image reference, one Gallery item. The single data row was retained after correcting an initial overly strict two-row filter.
- 2012 Boulevard: 8 tables, 78 rows, 151 embedded image references, 2 Gallery items; CSV in three parts. One unheaded table is retained.
- 2013 Boulevard: 5 tables, 22 rows, 40 embedded image references; one unheaded table retained.
- 2020 Boulevard: 5 tables, 24 rows, 44 embedded image references; one unheaded table retained.
- All CSV and QA outputs were re-fetched and verified non-empty. The corrected Bassline CSV and QA were also compared against the complete expected contents.
- Detailed source-level records: `research/MODERN-SPECIAL-SERIES-PROCESSING-INDEX.md`.
