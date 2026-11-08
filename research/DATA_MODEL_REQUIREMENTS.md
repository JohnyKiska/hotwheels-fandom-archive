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
