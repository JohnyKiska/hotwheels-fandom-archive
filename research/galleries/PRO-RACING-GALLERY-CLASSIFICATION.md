# Pro Racing Gallery evidence classification, first pass

Date: 2026-11-10

## Scope

First-pass classification of all 100 existing Pro Racing-related Gallery records in `research/galleries/GALLERY-EXTRACTION.csv`. Classification uses source page, filename, image alt/title and caption. It is not confirmation that every image depicts a production release. No image file was visually inspected in this pass; uncertain identity and association remain unresolved.

## Classification totals

| Evidence class | Records |
|---|---:|
| Card artwork / card variation | 9 |
| Packaging, sets and packaging comparisons | 41 |
| Advertising / promotional material | 4 |
| Prototype / pre-production / sample | 35 |
| Damaged packaging evidence | 2 |
| Resin driver figure evidence | 2 |
| Website assets | 5 |
| Signed hauler / product-variant evidence | 1 |
| Unclassified lot image | 1 |
| **Total** | **100** |

## Record-level mapping

Record numbers are existing `item_index` values within each source page's Gallery container.

### 1998 Pro Racing — 4
- Item 1: international generic #44 card artwork; source caption contrasts it with US team-number-specific card art.
- Items 2–4: PLAYERS INC Special Edition Set China 20985: overall/front, back of box and bottom of box. One set with multiple package views.

### 1999 Pro Racing — 12
- Items 1–2: damaged packaging comparison, light/white tape versus dark tape.
- Items 3–7: Petty Racing / Target 3-pack, multiple views of one package/set.
- Item 8: sealed Toy Story premium 2-pack.
- Items 9–10: Lucky Charms cereal-box promotion, front/back.
- Items 11–12: 50th Anniversary of Petty Racing 4-pack, front/back.

### 2000 Pro Racing — 12
- Item 1: advertising insert.
- Item 2: insert page showing prototypes; caption says some Deluxe Series examples may belong to Pro Racing or Hot Wheels Racing Selects, so line attribution is uncertain.
- Items 3–5: Toy Story 2 Thailand 27958 package/set views (front, back, bottom).
- Items 6–12: Scorchin' Scooter Collector Series Set 27961, multiple package/set views of one set.

### 2002 Pro Racing — 1
- Item 1: pre-production samples from the 2002 Mattel catalog. Caption identifies a Dodge Charger R/T as an example that was not released. Do not infer a production release.

### Basic Pro Racing Series — 13
- Items 1–8: #5 and #44 card variations; international / Pro Carreras card faces and backs.
- Items 9–13: rarity and packaging comparison evidence: 1999 rare six-car group, blister-back differences, and 2000 Pro Racing / Qantas / Grand Prix card backs. These are comparison evidence, not five independent products.

### Hot Wheels Racing Selects — 1
- Item 1: lot photograph with no informative caption. Unclassified; do not infer contents or release membership from filename.

### Team Transporter — 2
- Item 1: Ashley Force hauler / dragster image, source label “H1712 vers”; exact match to a table row still needs verification.
- Item 2: NASCAR Duracell promotional image; not automatically a standard release.

### Pro Racing 1:43 Scale — 55
- Items 1–9: Ferrari, Ford and Williams package prototypes attributed to Brian-Anna.com.
- Items 10–11: resin driver figure images attributed to Larry Wood's collection. Caption says the figure “might” be from this series; association uncertain.
- Items 12–16: 2002 McLaren F1 and signed 2000 Jaguar FEP prototype evidence, including no UPC / blank base / base views.
- Items 17–19: 2004 King of the Desert sample views.
- Items 20–21: 2003 Ferrari F1 sample, front/back.
- Item 22: Ferrari F1 Chrome Constructors Champions 4-pack.
- Items 23–25: 2001 World Champion and Compaq sample evidence.
- Items 26–28: 2004 Bahrain / Sakhir Ferrari sample views.
- Items 29–31: 2003 World Champions Ferrari sample; captions include figure detail and additional views.
- Item 32: Ferrari 150 GP Wins sample.
- Item 33: Racing Helmet EP sample.
- Items 34–38: Ferrari F12000 website assets; digital imagery, not confirmed physical product photos.
- Items 39–52: Ferrari F1 World Champions six-car set evidence, including overall/display views and annual champion/side views for 1999–2004. These are not 14 distinct releases.
- Items 53–55: 1999 Ferrari prototype views; proposed identity includes a question mark and remains uncertain.

## Data-model implications

1. Gallery item is an image-evidence record, not a product entity.
2. Multiple Gallery items may document one set, package, prototype or object from different angles. Subject/evidence clustering must be separate from image records.
3. Evidence classes should be controlled but allow uncertainty: card artwork, packaging, set view, advertising/promo, prototype, pre-production sample, website asset, comparison and unclassified.
4. Preserve exact caption, alt, filename, file-page URL, image URL and source page/item index. Do not overwrite source text with normalized interpretation.
5. “Might be from this series” and “some examples might be from...” remain uncertain associations, not confirmed release links.
6. The Ferrari six-car World Champions set is one candidate set subject with multiple image records and annual sub-view labels, not 14 products.

## QA

- Expected records: 100.
- First-pass evidence-type classification: 100.
- Unclassified evidence type: 1 (Racing Selects lot image).
- Uncertain associations retained: 2000 insert prototypes, Larry Wood resin driver figure, 1999 Ferrari prototype identity, and Ashley Force hauler exact row match.
- Existing Gallery master was not modified.
