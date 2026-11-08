# Data Model Requirements

Это исследовательские требования и направления проектирования, а не утверждённая схема БД.

## Идентичность и классификация

- Не использовать название серии или папку Fandom как единственный признак идентичности продукта.
- Разделять Product, Vehicle/Casting, Variant, Release, Assortment, Series, Series Era, Collection, Theme Group и Packaging.
- Поддерживать связи многие-ко-многим между продуктами, сериями, коллекциями, тематическими группами и ассортиментами.
- Хранить исходную классификацию источника отдельно от нормализованной классификации каталога.
- Поддерживать алиасы, региональные названия, переименования и исторические возрождения серий.

## Номера и даты

- Toy Number не считать глобально уникальным идентификатором.
- Разделять Toy Number, Collector Number, Series Position и другие типы обозначений.
- Хранить номер с контекстом источника, рынка, года, серии/ассортимента и конкретного выпуска.
- Разделять даты/периоды серии, выпуска продукта, варианта и упаковки.
- Сохранять исходные значения дат и номеров, не подменяя их догадочной нормализацией.

## Варианты и происхождение

- Представлять цвет кузова, тампо, колёса, базу, окна, салон и конструктивные особенности как различимые характеристики варианта.
- Учитывать изменения tooling/casting и происхождение форм, включая приобретённые или лицензированные инструменты.
- Не считать одинаковое имя доказательством одинакового casting; поддерживать подтверждённые и спорные связи.
- Поддерживать производителя, брендовые отношения и региональные версии.

## Составные продукты и механики

- Поддерживать продукты, которые не являются автомобилями: фигурки, самолёты, поезда, аксессуары, треки, игровые наборы и комплекты.
- Представлять состав комплекта и отношения компонентов (например, тягач и прицеп).
- Поддерживать совместимость треков, систем и аксессуаров.
- Учитывать механизмы и функции: моторизованный привод, пружинный привод, инерционный механизм, изменение цвета, трансформирующиеся элементы и другие особенности.
- Различать статусы Planned, Prototype, Released, Cancelled и Unconfirmed.

## Происхождение данных и повторный импорт

- Хранить источник, URL/путь, дату получения, таблицу, исходные заголовки и исходные значения строк.
- Сохранять исходную строку даже при неудаче распознавания или нормализации.
- Обеспечить возможность повторной обработки архивных данных без повторного скачивания страниц.
- Фиксировать статус уверенности и обоснование нормализованных связей.
- Не терять конфликтующие значения из разных источников.

## Технические термины и неоднозначность

- Один термин может обозначать серию и одновременно техническую характеристику (пример для проверки: Ultra Hots и тип колёс UH).
- Не объединять сущности только по совпадению названий.
- Схема должна допускать новые категории, эксклюзивности, рынки и типы выпусков через данные/админку, а не требовать переписывания кода для каждого нового значения.

## Следующий шаг

До изменения схемы БД проверить требования на реальных строках из ранних и современных коллекций, особенно на повторяющихся номерах, пересечениях серий, нескольких типах продуктов и поздних переизданиях.


## Дополнения по ранним специальным сериям

- **Assortment vs. product.** Action Packs, Color FX 2-Car Sets, Planet Micro sets и Sizzlers race sets показывают, что набор/упаковка должен быть самостоятельным ассортиментным объектом с составом компонентов; не каждая строка таблицы соответствует отдельному автомобилю.
- **Mechanism generations.** Color-change, spring-powered, electric motor, impact/crash mechanism, pop-up body features и light/sound должны моделироваться как отдельные механизмы/функции с возможностью нескольких механизмов на продукт.
- **Tooling lineage.** Поддержать отношения исходного casting, modified casting, retool и casting-derived-from (например, Scorchers → Shift Kickers; Mebetoys → Gran Toros adaptations; Corgi tooling in Action Packs).
- **Brand/manufacturer distinction.** Производитель, владелец бренда, разработчик дизайна и бренд на упаковке — разные роли. Не считать изделие Hot Wheels только потому, что оно произведено Mattel или совместимо с HW track.
- **Regional identity.** Региональные имена могут быть aliases одной системы (Hot Wheels U.S.A. и локальные названия), но похожее название в другом десятилетии может обозначать отдельную линейку (Hot Wheels World 1997–2005).
- **Scale exceptions.** Масштаб продукта хранить индивидуально: Planet Micro содержит исключения, а playset может включать предметы разных масштабов.
- **Unreleased records.** Хранить запланированные и прототипные модели с отдельным lifecycle status и без создания фиктивного Released event.
- **Packaging variants.** Различия карточки/лейбла могут существовать при неизменном продукте (пример Action Packs Sojourner Rover); упаковочные изменения не должны автоматически порождать новый casting.


## Дополнения по Other Early Series

- **Multi-type product families.** Attack Pack показывает, что одна тематическая линейка может включать наземные машины, самолёты, инопланетные объекты и динозаврообразные гибриды; family membership не должна предполагать единый Product Type.
- **Transformable products.** Поддержать состояния/формы трансформируемого объекта, механизм активации и уникальные инструменты/ключи с ограниченной совместимостью.
- **Large-scale motorized toys.** Action Cycles и Action Racers требуют масштабов за пределами 1:64 и механизмов clockwork/pull-back; масштаб и механизм назначаются конкретному продукту/варианту.
- **Rail systems.** Для Hot Wheels Railroad хранить рельсы, стрелки, переходы, локомотивы, вагоны и наборы как отдельные продукты; совместимость с HO track и fork-style coupler должны быть явными связями.
- **Name reuse.** Повторное использование названия спустя десятилетия (Attack Pack 1992–1994 и 2026) не является достаточным доказательством одной Series Identity; нужна отдельная связь Name Reuse/Inspired By.
- **Manufacturer and brand.** ARCO Toys, Mattel и Hot Wheels brand role должны быть отдельными атрибутами/отношениями.


## Дополнения по Modern Special Series (первый проход)

- **Umbrella assortment hierarchy.** Ввести уровни franchise/family → series identity → era/year → mix/subseries → individual release → packaging/case assortment. Примеры: Car Culture annual mixes, Character Cars IP-based assortments, AcceleRacers team subsets.
- **Licensed IP.** Хранить лицензиара, франшизу, персонажа, фильм/медиа источник и тематическое оформление независимо от casting identity и HW product brand.
- **Release vs. casting reuse.** Один casting может иметь разные Toy #, цвета, колёса, IP deco, retail channels и packaging. Отношения "same casting", "same decoration", "identical release" и "similar tooling" должны быть разными.
- **Set composition.** Team Transport, 2-packs, premium 5-packs, comic bundles, Character Cars playsets и Color Reveal barrels требуют component/quantity relationships и собственного package/set SKU.
- **Chase and distribution.** Chase status, case allocation, filler cars, retailer exclusivity, convention exclusivity и factory-set exclusivity — разные данные distribution/assortment, не один флаг exclusive.
- **Color-change states.** Механизм изменения цвета хранить как технологию с несколькими температурными состояниями; Color Reveal дополнительно имеет растворимое внешнее покрытие и отдельное first-use transition.
- **Digital features.** AcceleRacers base codes и online unlocks требуют поля/сущности digital code, destination/service, validity period и entitlement, не смешанные с Toy #.
- **Packaging.** Acrylic cases, ribbed blister, upside-down card, Color Reveal barrel, card artwork and packaging code должны быть отдельными packaging variants.
- **Materials and chassis.** Plastic body, metal body, die-cast chassis, anodized finish и spectraflame finish фиксируются раздельно на уровне варианта/релиза.
- **Anniversary/name reuse.** Anniversary-themed reissues (например AcceleRacers 2025) должны связываться с исходной franchise/line через tribute/commemorative relationship, но не автоматически объединяться с исходной эpoхой.


## Дополнения по Pro Racing, цифровым и тематическим коллекционным линиям

- **Competition identity.** Для гоночных релизов хранить сезон, чемпионат/серии, команду, номер машины, пилота, спонсора, race livery и casting отдельно. Один casting может быть несколькими командами/ливреями.
- **Basic vs Premium construction.** Материал базы/кузова, колёса, детализация и назначение (play/track vs display) могут отличаться у визуально родственных выпусков; не наследовать construction от casting.
- **Promotional distribution.** Baggie promos, commemorative cards, MLB/team promotions, retailer exclusives и factory sets требуют distribution channel и package type.
- **Physical-digital products.** Для Hot Wheels id нужны NFC chip, app/service, portal, smart-track, game entitlement и lifecycle/deprecation. Digital identity не равна Toy #.
- **Designer attribution.** Designer garage, designer, graphics artist и licensor/brand owner — разные роли и отношения.
- **Packaging/source errors.** Сохранять ошибочные напечатанные series counts, исправленные надписи и notes как source evidence, не перезаписывая фактическое значение без provenance.
- **Theme polymorphism.** Theme может ссылаться на media franchise, fictional character, consumer brand, musician, sports team, historical artwork или product brand; нужна типизированная Theme/IP taxonomy.
- **Retailer exclusivity by era.** Exclusivity scope должен относиться к конкретному release/package/market/year, а не глобально к series identity.


## Дополнения по Hot Wheels Classics (2005–2009)

- **Series position vs Toy Number.** Series # (например 6/30) и Toy # (например J2762) являются разными идентификаторами. Один Series # может иметь несколько релизов/вариантов, а один Toy # повторяется для разных цветов/колёс; ни одно из этих полей не является универсальным PK.
- **Release variants.** Поддержать вариации body color/finish (включая Spectraflame), wheel type и wheel-size, interior color, tampo/logo orientation, grille/base details и дополнительные аксессуары (button) как независимые признаки варианта.
- **Packaging and distribution.** Foil seal, card artwork, Button card, Walgreens 3-pack, Comic-Con exclusive, RLC Rewards и set-exclusive должны быть связаны с конкретной упаковкой/релизом и каналом распространения, а не задаваться одним флагом всей серии.
- **Chase designation.** Chase — статус конкретного релиза/варианта и/или distribution case, а не характеристика casting. Не переносить его на все варианты модели.
- **Set composition.** Track sets и 3-packs являются самостоятельными assortment/set records с компонентами и количествами; track pieces/joiners и cars должны быть разными Product Types и Product Components.
- **Source schema variability.** Импортёр должен поддерживать разные наборы колонок по таблицам и хранить raw source rows/cells. Пустая/отсутствующая колонка не означает, что характеристика отсутствует у продукта.
- **Source notes and confidence.** Notes вроде "rear bigger wheels", "same size wheels", "from Ice Blue to dark" и logo orientation должны сохраняться как provenance evidence даже после структурирования в отдельные поля.


### Flying Customs (2006–2013)
- **Assortment waves.** Mix 1–6 и годовые выпуски должны моделироваться как отдельные assortment/wave assignments, не как Series Position.
- **Manufacturing provenance.** Сохранять country of manufacture на уровне конкретного релиза/варианта; допустимы неизвестные/пустые значения без вывода страны по соседним строкам.
- **Multiple base codes.** Поддержать связь релиза с несколькими исходными base/case codes и хранить исходную последовательность кодов.
- **Tooling events.** Разделить New tool! и New die-cast chassis! как разные типы изменений tooling/chassis, с исходной заметкой и привязкой к релизу.
- **Wheel specification.** Wheel type может быть указано отдельно от Mix, а сокращения UH/GHO/SHO/BW/CT требуют справочника алиасов с сохранением raw token.


### Hot Wheels Cool Classics (2013–2014)
- **Card artwork variants.** Поддержать несколько вариантов оформления карточки для одного и того же автомобильного релиза (Custom Otto blue/red и gold/pink) без создания отдельных casting/vehicle records.
- **Series position vs Toy #.** Сохранять позицию 1/30–30/30 отдельно от Toy #; Toy # не является сортировочным ключом и может идти в ином порядке.
- **Line-level specifications.** Общие утверждения о metal base, wheel type и country of manufacture хранить как line/year-level source assertions с provenance, пока источник не подтверждает их для каждой конкретной строки.
- **Packaging provenance.** Фон карточки, artwork и их варианты должны моделироваться на уровне Packaging/Release, с возможностью связать несколько artwork variants с одной моделью.


### Crashers / Mega Wrecks / Bumper Busters (2007–2008)

- **Mechanism as product feature.** Поддержать тип механизма (например, spring-activated), триггер/условие активации (collision/impact), действие (body flips away; multi-stage damage) и направление/тип движения (back/side/front) раздельно. Не сводить crash type к текстовому тегу окраски.
- **Moving parts and product states.** Нужны связи между продуктом, подвижными/отделяемыми компонентами и визуальными состояниями (normal/crashed), включая возможность нескольких стадий трансформации/повреждения.
- **Product form and scale.** Отличать обычный die-cast vehicle, пластиковую crash-action toy vehicle, увеличенную игрушку с lights & sounds и крупную play vehicle с multi-stage crash action. Масштаб и габариты должны быть nullable и подтверждаться источником.
- **Product family vs line identity.** Позволить связывать Crashers 2007, Mega Wrecks 2008 и Bumper Busters отношениями related_to / based_on, не навязывая им одну Series Identity.
- **Pack composition.** Bonus Vehicle 2-Packs и Crashers 3-Pack должны быть отдельными package/set records с собственным Toy #/SKU и Product Components; один комплект может включать обычную Hot Wheels модель и Crasher или несколько Crasher products.
- **Source raw values.** Хранить raw wheel strings (C5SP, C6SP, CWSP, Red C5SP и т. п.) и raw Toy # values, включая «?», повторные номера и возможные опечатки. Нормализацию делать отдельно с provenance и статусом проверки.
- **Year attribution.** Год страницы, год категории, год отдельного выпуска и год продуктовой линии не взаимозаменяемы; Mega Wrecks прямо обозначены на странице как 2008, а основной Crashers page охватывает категории 2007 и 2008.


### Dragstrip Demons (2009–2010)
- **Series position vs release identity.** Хранить Series # отдельно от Toy # и Release ID. Поддержать отсутствующие/отменённые позиции, повторяющиеся Series # и несколько вариантов одного номера.
- **Wheel variants.** Один Toy #/Series # может иметь альтернативные wheel configurations (пример N8964, RR5SP и RRMag); wheel variant не должен автоматически создавать новый casting.
- **Cancelled/planned releases.** Нужны статусы planned, cancelled/not produced, released и source notes для нереализованных позиций; не создавать полноценный Release как состоявшийся продукт без evidence.
- **Historical vehicle attribution.** Хранить реальную машину, пилота, команду, спонсора и race livery отдельными связями с provenance и confidence; модель Hot Wheels и корректность исторической атрибуции не одно и то же.
- **Series lineage and name reuse.** Поддержать successor/tribute/revival/name-reuse relations между Dragstrip Demons 2009–2010, Vintage Racing 2011 и Car Culture 2018, не объединяя их автоматически в одну Series Identity.
- **Source row fidelity.** Сохранять raw Series #, Toy #, Notes, N/A и повторяющиеся значения без автоматической коррекции.


### Vintage Racing (2011)
- **Series lineage.** Поддержать явные отношения successor/replaced_by между разными Series Identity; не объединять линии автоматически, даже если источник прямо говорит, что одна заменила другую.
- **Base/case codes.** Поле Notes может содержать несколько Base code(s) на один релиз. Хранить список raw codes с исходным порядком, не превращая код в Toy # или Series Position.
- **Packaging misprints.** Ошибочный номер, напечатанный на карточке (например, #22 вместо позиции 15/30), должен храниться как Packaging/Print Error с provenance и scope, не перезаписывая фактическую позицию продукта.
- **Line-level manufacturing claim.** Страну производства, заявленную на уровне всей линии, хранить как source assertion с охватом 2011 Vintage Racing; не копировать как индивидуально проверенное поле для каждой модели без evidence.


### Dragstrip Demons (Car Culture, 2018)
- **Segment vs series identity.** Model Car Culture as the parent line/series and Dragstrip Demons as a named segment/subseries with its own five release positions, Toy # values and wheel configurations. Do not merge it with the 2009–2010 Dragstrip Demons series based only on name/logo reuse.
- **Wheel assemblies.** Support multiple wheel types per release and preserve their raw order/string. Do not assume a compound wheel note means alternative variants; axle-level assignment may need verification.
- **Themed successor/revival links.** Provide typed relations such as revival_of, tribute_to, successor_to or name_reuse_of, with evidence and confidence.

### Vintage Racing Club (2024)
- **Mix as assortment dimension.** Support separate mix-local position numbering (Mix 1 1/6–6/6; Mix 2 1/5–5/5), not one forced 1–11 sequence.
- **Series identity separation.** Do not equate Vintage Racing Club 2024 with Vintage Racing 2011 based on lexical similarity. Store explicit relationship only when supported.
- **Release-level attributes.** Store casting name, color, tampo/deco description, wheel type, opening features, metal-base notes and multiple base codes per release with source provenance. Line-level theme claims such as “pre-1974” and “silver label” remain source assertions, not inferred attributes on every vehicle.
- **Raw source preservation.** Preserve punctuation anomalies and raw Notes (including “Base code(s); S43”) alongside normalized values.


## Formula One Collection: motorsport identity and driver relationships
- **Separate entities:** represent Hot Wheels Product/Casting/Release separately from the real-world racing vehicle, chassis/model, constructor/team, driver, season and racing number. Do not collapse these into one “car name” string.
- **Season-scoped participation:** model Driver ↔ Team and Driver ↔ Racing Vehicle/Entry relationships with season (and, where available, race/event or date range). A driver can change teams/cars; a team can field multiple drivers in the same season.
- **Release representation link:** each Hot Wheels release may represent a specific real-world vehicle/driver entry, a team livery without a specific driver, or a multi-vehicle set. Make this representation relation optional and typed; do not force a driver onto team-branded products.
- **Racing number:** store the real-world competition number separately from Hot Wheels Toy # / SKU. Preserve its season/context because numbers can change between drivers and years.
- **Chassis identity confidence:** store the source's raw vehicle/team label and a separately normalized chassis/model reference only when supported. Rows that state only team + racing number must not inherit a chassis by inference.
- **Team naming history:** preserve original season-specific team names and model naming strings; provide optional canonical team identity plus time-bounded aliases/sponsorship names. Do not overwrite source labels such as Visa Cash App RB or Atlassian Williams Racing.
- **Assortment product types:** support individual driver-specific cars, team-branded products without driver attribution, display/booklet products, podium sets and other multipacks. A set must link to its included product instances/castings and preserve the source's listed quantities/order where available.
- **Release attributes and provenance:** retain Toy #, wheel type, stand codes (including multiple codes), raw Casting Name, Driver and source row/order as release-level data. Preserve year-specific source paths and revisions.
- **No forced identity merge:** two releases with the same team and racing number in different years are not automatically the same real-world chassis; similarly, a repeated driver name does not establish the same team/vehicle relation across seasons.


## Pro Racing: motorsport entries, teams, drivers and multi-format assortments
- **Do not force a single racing discipline:** support NASCAR stock cars, Indy/CART open-wheel cars, Formula 1 cars, pace cars, trucks and other racing-related castings under a broad racing context with discipline/category attributes.
- **Separate product from racing entry:** a Hot Wheels casting/release is not the real race car. Link a release optionally to a real-world Racing Vehicle/Entry with confidence and source evidence.
- **Team and sponsor are distinct:** preserve the raw source field (often a compound string) and model Team/Constructor, Sponsor, Livery/Deco, Event and Driver separately. Sponsor name alone does not identify a driver.
- **Driver attribution is optional and evidence-based:** 2003 Luxury Rides explicitly supplies driver names, while most yearly tables do not. Support direct source attribution, partial/unresolved name fragments and absent driver attribution. Do not infer driver from racing number or team.
- **Season and entry context:** model Driver ↔ Team ↔ Racing Entry as time-scoped relationships; the same number can be associated with different drivers/teams across years or even within one year. Racing number is not a stable global identity.
- **Table/program provenance:** retain source page, year, table order/title, raw column labels, row order and program/category label (e.g. Race Day, Luxury Rides, Pit Board, Treasure Hunt, STOCKERZ, Wrenchin' & Racing, Justice League). A page may aggregate many unrelated product formats.
- **Multiple product formats:** support cars, trucks, Tool Box products, Pit Board/display pieces, sets, promos, trading-card inclusions and other non-vehicle merchandise. Do not assume every table row is a car casting.
- **Release identity and variant layers:** Toy #, Item Number, racing number, wheel code, base/material, interior, country, livery, facing direction, grille/spoiler, autograph/decal, card/packaging and set exclusivity must remain distinct fields/relations.
- **Release status:** distinguish confirmed released, unreleased/never released, prototype, preview, promo-only, uncertain and source-noted duplicate. Do not include unreleased entries in released-product counts.
- **Cross-listing and set links:** preserve explicit notes such as “same as [year/program]”, “only available in [set]”, or included trading cards. Do not create a new casting from each cross-listing.
- **Open-wheel identity:** support chassis model and season-specific team/driver entries (e.g. Reynard 97L, Lola T97, McLaren MP4-14/MP4-13, GP-2009) independently from the Hot Wheels casting label. Preserve uncertain model/driver labels as raw text until verified.
- **Normalization discipline:** wheel abbreviations and suffixes in team numbers require codebooks/evidence; retain raw strings and source spellings before normalization.


## Racing Selects and Team Transporter
- **Structured racing attribution:** support separate Racing Number, Casting, Color/Livery, Team, Sponsor and Driver. Driver may be explicit, corrected, inherited from a merged/continuation row, or unknown. Preserve both original/printed attribution and later correction with provenance.
- **Non-unique racing number:** racing numbers may appear on different castings, historical vehicles and unrelated products. Never use racing number as a unique key.
- **Continuation/merged table rows:** importer must preserve source row order, blank cells, merged-cell inheritance and continuation rows. Store raw row data before deriving inherited values.
- **Transporter as product and bundle:** model hauler casting/release and car casting/release independently; represent the packaged Team Transporter as a set/bundle with explicit component membership and quantities where known.
- **Truck casting identification:** allow casting attributes/identification notes such as exhaust stack position, cab shape, headlight shape and wind-deflector window imprint. These are not release attributes.
- **Variant and packaging separation:** distinguish truck casting, livery/sponsor decals, car component, box/packaging variation, wheel/headlight variation and set composition.
- **Separate line identities:** similar truck-plus-car format does not establish that 1998–2006 Pro Racing Team Transporter and 2018+ Car Culture Team Transport are the same Series/Collection identity. Link them through a typed thematic/format relationship only if evidence supports it.


## Car Culture Team Transport (2018–2026): multi-component bundles and annual mixes

- **Bundle is a first-class product format.** Model a Team Transport product/set separately from each included vehicle, hauler and trailer release. Do not treat the bundle as a single casting.
- **Variable component cardinality.** Support two-, three- and potentially higher-component bundles. Examples in source tables include truck + trailer + car. Preserve component order, role (hauler, trailer, car/vehicle, other) when explicitly known, quantity and raw source row.
- **Table row grouping.** Source tables often put Toy # and Series # on the first component row and leave them blank on following component rows. Preserve source row order, blank cells and group membership before normalization; do not interpret each blank-number component as an independent SKU.
- **Annual mix is an assortment dimension.** Store year and Mix label separately from the continuous Team Transport Series #. Retailer/event exclusives may be listed outside mixes and carry Series # = N/A.
- **Separate identifiers.** Toy # (bundle SKU) and Team Transport Series # (numbered position) are distinct fields. Retain raw Series # string, including 2024's `#62` formatting and N/A values.
- **Component-level attributes.** Casting name, body color, wheel type, base codes, and notes such as `New Casting`, `New Die-Cast Chassis` and `Modified casting` belong to individual component rows unless source explicitly assigns them to the whole product.
- **Wheel assemblies.** Preserve compound wheel strings verbatim. A string containing two wheel codes may describe multiple axle/component configurations, not a choice of variants.
- **Source assertions and normalization.** Preserve raw color, capitalization, punctuation and source typos (e.g. `Metelflake Silver`); normalized values should be additional fields with evidence, never destructive replacements.
- **Series identity boundaries.** Do not merge Car Culture Team Transport (2018+) with Pro Racing Team Transporter (1998–2006) based only on a shared truck + car bundle format. A typed format/theme relation may be stored independently of Series identity.
- **Provenance.** Retain source page/year/revision, table/mix, row order, original column values and group boundaries for re-import and audit.


## Car Culture umbrella: annual segments, 2-Packs and Factory Sets

- **Umbrella and segment separation:** represent Car Culture as a parent program/category, with annual themed segments as child assortment entities. Do not treat segment names as fixed enums or require one canonical segment list across years.
- **Segment-local numbering:** Series # such as `1/5`–`5/5` is scoped to its themed segment. Retain raw value and parsed numerator/denominator separately. `0/5` needs a typed classification from source context (Chase, RLC 6th Car Set, or unknown), not a hard-coded meaning.
- **Chase as release classification:** model Chase as a release/variant designation separate from ordinary Series Position. Preserve source note and year/segment.
- **2-Pack product format:** model Toy # as a 2-Pack product and link two individual vehicle releases/components, each with its own casting, color, wheel, base code and notes. Preserve source row order and blank cells that indicate grouping.
- **Team Transport product format:** retain multi-component bundle requirements (hauler/trailer/car) separately from 2-Packs; both are bundles but have different roles and component semantics.
- **Factory Set format:** model Factory Set as a bundle/aggregation of named annual segments and Team Transport Mixes, with its own Toy # and Set #. Contents may reference a Team Transport Legends Tour Exclusive; preserve each included assortment relationship and source order.
- **Container Sets vs Factory Sets:** do not assume annual `Container Sets` tables (2022–2024) are identical to the separate 2022–2026 Factory Set page. Keep source taxonomy labels and explicit relation unresolved until confirmed.
- **Flexible assortment composition:** Factory Sets and 2-Packs demonstrate that one product can contain other products/assortments or multiple vehicle releases. Support typed set components, nested bundles/assortments and variable cardinality.
- **Identifier domains:** distinguish Toy #, segment-local Series #, Factory Set Set #, Team Transport Mix/Series #, and component casting/release IDs. None is a universal key.
- **Source-asserted equivalence:** preserve `Identical to`, `Similar to`, `Updated tooling`, `New Casting`, `New Die-cast Chassis` as raw assertions linked to the relevant row/component. Do not convert directly into canonical identity or tooling lineage without corroboration.
- **Provenance:** store year page, Fandom revision, section heading, table index, row order, original cell strings and source grouping boundaries.


## Cross-catalog identity and source-asserted relationships

- **Candidate matching, not identity merging:** support candidate links generated from normalized casting names, but keep them separate from confirmed casting identity. A match must retain the compared source rows and matching method.
- **Typed source assertions:** represent notes such as Identical to [Toy #], Similar to [Toy #], Same as [year], Modified Casting, New Casting and New Die-Cast Chassis as typed assertions/relationships attached to the exact release or bundle component. Preserve raw note, source page, row, and target identifier when present.
- **Cross-catalog identifier namespaces:** Toy # is not a globally unique key across Mainline, Premium, 2-Packs, Boulevard, Pop Culture, Team Transport or other product programs. Store source/program/year context with every external identifier.
- **Separate release from casting:** the same named casting can recur in multiple years and product programs with different Toy #, colors, wheels, base codes, chassis notes and distribution. Model each release separately and link to a casting only when supported.
- **Relationship confidence:** distinguish exact source phrase from normalized interpretation and independently verified identity. Identical to must not be silently upgraded to a canonical same-casting or same-tooling assertion.
- **Mainline comparison anchor:** 2024 Mainline list is one comparison dataset, not a complete Mainline authority. Matching should be repeatable across years as additional annual lists are imported.
