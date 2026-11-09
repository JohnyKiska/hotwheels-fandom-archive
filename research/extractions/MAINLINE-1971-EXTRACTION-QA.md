# Mainline 1971 Source Extraction QA

## Source and provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1971/List of 1971 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `4a9b8b98d60a1e90647d3dd54ac14cc0e7918c15`
- Git tree / Contents API size: 404,249 bytes
- Manifest SHA-256: `2646c4d7b715c0996fcc9f0dfd5171e177f85c05a619647b270cb994a7ca7d21`
- Fandom revision: 629286

## Important source-structure exception

The archived 1971 page contains no annual product table. Its only HTML table is the yearly-navigation table. Product/model and catalog content is presented in five image galleries under distinct headings. This export is a faithful gallery inventory, not a reconstructed annual product table.

## Gallery extraction

- HTML tables found: 1 (yearly-navigation only; excluded from product records)
- Product tables extracted: 0
- Gallery sections extracted: 5
- Gallery entries retained: 39
- Hot Wheels Series: 21 entries
- Heavyweights: 7 entries
- Mongoose vs Snake: 4 entries
- Spoilers: 3 entries
- Gallery: 4 entries
- Unique nonblank gallery captions: 37
- Blank captions: 2
- Image filenames captured: 39
- Image alt labels captured: 37
- File/image links retained: 39
- Model-page links retained where present: 35
- Toy # / Collector # / Series # fields: not present as structured gallery fields
- Color, tampo, base/window/interior and wheel attributes: not provided as structured gallery fields

## Extracted gallery entries

| Section | Position | Caption | Image filename |
|---|---:|---|---|
| Hot Wheels Series | 1 | AMX/2 | Amx2.jpg |
| Hot Wheels Series | 2 | Bugeye | Bugeye.jpg |
| Hot Wheels Series | 3 | Bye-Focal | Byefocal.jpg |
| Hot Wheels Series | 4 | Classic Cord | Classiccord.jpg |
| Hot Wheels Series | 5 | Cockney Cab | Cockneycab.jpg |
| Hot Wheels Series | 6 | Crew Car | Pitcrew.jpg |
| Hot Wheels Series | 7 | Grass Hopper | Grasshopper.jpg |
| Hot Wheels Series | 8 | Hairy Hauler | Hairyhauler.jpg |
| Hot Wheels Series | 9 | The Hood | Thehood.jpg |
| Hot Wheels Series | 10 | Ice 'T' | Icet.jpg |
| Hot Wheels Series | 11 | Jet Threat | Jetthreat.jpg |
| Hot Wheels Series | 12 | Mutt Mobile | Muttmobile.jpg |
| Hot Wheels Series | 13 | Noodle Head | Noodlehead.jpg |
| Hot Wheels Series | 14 | Olds 442 | Olds442.jpg |
| Hot Wheels Series | 15 | Rocket Bye Baby | Rocketbyebaby.jpg |
| Hot Wheels Series | 16 | Short Order | Shortorder.jpg |
| Hot Wheels Series | 17 | Six Shooter | Sixshooter.jpg |
| Hot Wheels Series | 18 | Special Delivery | Specialdelivery.jpg |
| Hot Wheels Series | 19 | Strip Teaser | Stripteaser.jpg |
| Hot Wheels Series | 20 | T-4-2 | T-4-2.jpg |
| Hot Wheels Series | 21 | What-4 | What-4.jpg |
| Heavyweights | 1 | Fuel Tanker | Fueltanker.jpg |
| Heavyweights | 2 | Racer Rig | 81008 023-1-.jpg |
| Heavyweights | 3 | S'Cool Bus | 'coolbus.jpg |
| Heavyweights | 4 | Scooper | Scooper.jpg |
| Heavyweights | 5 | Snorkel | Snorkel.jpg |
| Heavyweights | 6 | Team Trailer | Teamtrailer.jpg |
| Heavyweights | 7 | Waste Wagon | Wastewagon.jpg |
| Mongoose vs Snake | 1 | Mongoose II | Mongoose2.jpg |
| Mongoose vs Snake | 2 | Snake II | Snake2.jpg |
| Mongoose vs Snake | 3 | Mongoose Rail Dragster | Mongooseraildragster.jpg |
| Mongoose vs Snake | 4 | Snake Rail Dragster | Snakeraildragster.jpg |
| Spoilers | 1 | Boss Hoss | Bosshoss1971.jpg |
| Spoilers | 2 | Evil Weevil | Evilweevil.jpg |
| Spoilers | 3 | Sugar Caddy | Sugarcaddy.jpg |
| Gallery | 1 | From the Wheels & Wings '71 catalog | Wheels Wings 71 catalog (5).jpg |
| Gallery | 2 |  | Wheels Wings 71 catalog (6).jpg |
| Gallery | 3 |  | Wheels Wings 71 catalog (7).jpg |
| Gallery | 4 | ...and extra Action Accessories | Wheels Wings 71 catalog (8).jpg |

## Interpretation cautions

- All five headings are preserved verbatim as source scopes. They are not collapsed into one assumed release taxonomy.
- The `Gallery` section contains Wheels & Wings '71 catalog imagery, not additional model-name records. Two catalog images have blank captions; their blank captions are preserved rather than inferred from filenames.
- Captions, image alt labels, filenames, image/file links, gallery anchors and model-page links are retained separately in raw source metadata.
- Gallery membership alone does not establish Toy #, package, release variant, color, or exact release date.
- No rows were merged or deduplicated across sections. Repeated names, if present, remain separate source rows.

## Output

- `research/extractions/MAINLINE-1971.csv`
- `research/extractions/MAINLINE-1971-EXTRACTION-QA.md`

All 39 gallery entries are preserved in source order with section provenance and original image/link metadata.
