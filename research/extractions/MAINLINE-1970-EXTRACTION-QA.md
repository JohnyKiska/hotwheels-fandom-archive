# Mainline 1970 Source Extraction QA

## Source and provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1970/List of 1970 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `935169de87712fe34faea661f85ac18e084fa006`
- Git tree / Contents API size: 406,597 bytes
- Manifest SHA-256: `f96064b5ca6f10d943210536a270d36cc7f25dbe658d7bd089bab6f22818b81d`
- Fandom revision: 716799

## Important source-structure exception

The archived 1970 page contains no annual product table. Its only HTML table is the yearly-navigation table. Product/model content is presented in six image galleries under distinct headings. This is a faithful gallery inventory, not a reconstructed annual product table.

## Gallery extraction

- HTML tables found: 1 (yearly-navigation only; excluded from product records)
- Product tables extracted: 0
- Gallery sections extracted: 6
- Gallery entries retained: 37
- Club Kit: 3 entries
- Grand Prix: 2 entries
- Heavyweights: 6 entries
- Hot Wheels: 19 entries
- Sky Show Set Only: 2 entries
- Spoilers: 5 entries
- Unique nonblank gallery captions: 37
- Blank captions: 0
- Duplicate captions: 0
- Image filenames captured: 37
- Image alt labels captured: 37
- File/image links retained: 37
- Model-page links retained where present: 37
- Toy # / Collector # / Series # fields: not present as structured gallery fields
- Color, tampo, base/window/interior and wheel attributes: not provided as structured gallery fields

## Extracted gallery entries

| Section | Position | Caption | Image filename |
|---|---:|---|---|
| Club Kit | 1 | Boss Hoss Silver Special | Bosshoss.jpg |
| Club Kit | 2 | Heavy Chevy Club Kit | Heavychevychrome.jpg |
| Club Kit | 3 | King 'Kuda Club Kit | Kingkudachrome.jpg |
| Grand Prix | 1 | Ferrari 312P | Ferrari312p.jpg |
| Grand Prix | 2 | Porsche 917 | Porsche917.jpg |
| Heavyweights | 1 | Ambulance (1970) | Ambulance1970.jpg |
| Heavyweights | 2 | Cement Mixer | Cementmixer1970.jpg |
| Heavyweights | 3 | Dump Truck | 1970dumptruck.jpg |
| Heavyweights | 4 | Fire Engine | Fireengine.jpg |
| Heavyweights | 5 | Moving Van | Movingvan.jpg |
| Heavyweights | 6 | Tow Truck | Towtruck1970.jpg |
| Hot Wheels | 1 | Carabo | Carabo.jpg |
| Hot Wheels | 2 | Classic Nomad | Classicnomad 1b.jpg |
| Hot Wheels | 3 | The Demon | Thedemon.jpg |
| Hot Wheels | 4 | Fire Chief Cruiser | Firechiefcrusier.jpg |
| Hot Wheels | 5 | Jack Rabbit Special | Jackrabbitspecial.jpg |
| Hot Wheels | 6 | Mantis | Mantis (2).JPG |
| Hot Wheels | 7 | Mighty Maverick | Mightymaverick.jpg |
| Hot Wheels | 8 | Mod Quad | Modquad.jpg |
| Hot Wheels | 9 | Paddy Wagon | Paddywagon.jpg |
| Hot Wheels | 10 | Peepin' Bomb | Peepinbomb.jpg |
| Hot Wheels | 11 | Power Pad | Powerpad.jpg |
| Hot Wheels | 12 | Red Baron | Redbaron.jpg |
| Hot Wheels | 13 | Sand Crab | Sandcrab.jpg |
| Hot Wheels | 14 | Seasider | Seasider.jpg |
| Hot Wheels | 15 | Swingin' Wing | Swinginwing.jpg |
| Hot Wheels | 16 | Snake | Snakefunnycar.jpg |
| Hot Wheels | 17 | Mongoose | Mongoosefunnycar.jpg |
| Hot Wheels | 18 | Tri Baby | Tribaby.jpg |
| Hot Wheels | 19 | Whip Creamer | Whipcreamer.jpg |
| Sky Show Set Only | 1 | Sky Show Deora | Skyshowdeora.jpg |
| Sky Show Set Only | 2 | Sky Show Fleetside | Flyin colors sky show orange.jpg |
| Spoilers | 1 | Heavy Chevy | Heavychevy.jpg |
| Spoilers | 2 | King 'Kuda | Kingkuda.jpg |
| Spoilers | 3 | Light My Firebird | Lightmyfirebird.jpg |
| Spoilers | 4 | Nitty Gritty Kitty | Nittygrittykitty.jpg |
| Spoilers | 5 | TNT Bird | Tntbird.jpg |

## Interpretation cautions

- All six headings are preserved verbatim as source scopes. They are not collapsed into one assumed release taxonomy.
- Gallery membership alone does not establish Toy #, package, release variant, color, or exact release date.
- Captions, image alt labels, filenames, image/file links, gallery anchors and model-page links are retained separately in raw source metadata.
- No rows were merged or deduplicated. Similar names in different sections, if any, remain distinct source rows.
- The page's gallery-only structure must not be silently converted into a conventional annual release table.

## Output

- `research/extractions/MAINLINE-1970.csv`
- `research/extractions/MAINLINE-1970-EXTRACTION-QA.md`

All 37 gallery entries are preserved in source order with section provenance and original image/link metadata.
