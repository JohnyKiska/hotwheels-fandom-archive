# Data Model Validation

Статус: IN PROGRESS  
Начало: 2026-11-10  
Назначение: проверить требования к будущей модели данных на реальных извлечённых строках до утверждения схемы БД.

## Принципы

- Не менять исходные CSV и не выполнять разрушительную нормализацию.
- Разделять Product, Casting, Variant, Release, Assortment/Set и Packaging.
- Сохранять исходные заголовки, ячейки, порядок строк, пустые ячейки и контекст rowspan.
- Не считать Toy #, Series #, Collector # и racing number взаимозаменяемыми или глобально уникальными.
- Каждое нормализованное значение должно иметь provenance и уровень уверенности.
- Не превращать гипотезы в факты без независимого подтверждения.

## Начальная выборка (2026-11-10)

### 1. Early Collections / Boss Hoss

Источник: `research/extractions/EARLY-COLLECTIONS-BOSS-HOSS.csv`

Наблюдения:
- Одна модель встречается в нескольких годах, сериях и цветовых вариантах.
- Toy # 6499 повторяется у нескольких строк с разными годами/цветами.
- В строке одновременно присутствуют атрибуты варианта (Color, Sticker, Tampo, Base, Window, Interior, Wheel Type) и контекст выпуска (Year, Series, Country).
- Поле Photo относится к исходному представлению/свидетельству, а не к идентичности продукта.

Требования, подтверждённые примером:
- Toy # не является PK.
- Casting identity нельзя выводить только из строки релиза.
- Variant и Release должны быть различимы.
- Год, серия и страна производства должны храниться с контекстом исходной записи.

### 2. Early Collections / 30th Anniversary 4-Car Set

Источник: `research/extractions/EARLY-COLLECTIONS-30TH-ANNIVERSARY-4-CAR-SET.csv`

Наблюдения:
- Несколько моделей входят в один набор и имеют общий Toy # 19322.
- Год 19322 находится в ячейке с rowspan и наследуется последующими строками; в исходных строках этих ячеек нет.
- У каждой компонентной модели есть собственные цвет, тампо, база, окна, салон и колёса.
- Значения и HTML исходных ячеек сохранены отдельно от распознанных значений.

Требования, подтверждённые примером:
- Набор/Assortment является самостоятельной сущностью с компонентами.
- Нужны связи Set → component product/release с порядком и количеством.
- Исходные пустые ячейки и rowspan context необходимо сохранять.
- Toy # набора нельзя автоматически присваивать каждой модели как её индивидуальный SKU.

### 3. Notable Modern Themed Assortments / Ultra Hots Series (2022)

Источник: `research/extractions/NOTABLE-MODERN-THEMED-ASSORTMENTS-ULTRA-HOTS-SERIES-2022.csv`

Наблюдения:
- Табличная строка содержит Series #, Toy #, Casting Name, Color, Tampo, Wheel Type, Notes и ссылки на фотографии.
- Toy # (например HDG61) и Series # (например 1/8) имеют разную семантику.
- Примечание может содержать несколько base codes (например R02, R04).
- Цвет включает финиш Spectraflame, а тампо описывает несколько отдельных графических признаков.
- CSV сохраняет исходные HTML, source cells, image metadata и ссылки.

Требования, подтверждённые примером:
- Series Position и Toy # должны быть разными типизированными идентификаторами.
- Один релиз может иметь несколько кодов базы и несколько атрибутов декора.
- Ссылки/изображения и raw source evidence должны оставаться привязанными к исходной записи.
- Нормализованные цвет/декор не должны затирать исходный текст.

## Первичные выводы

1. Плоская таблица «одна строка = одна модель» не описывает корректно все найденные данные.
2. Минимально необходимы раздельные уровни Product/Casting, Variant, Release и Assortment/Set.
3. Provenance должен быть полноценной частью модели, а не только URL на странице.
4. Идентификаторы должны иметь тип и контекст; универсального поля `number` недостаточно.
5. До утверждения схемы требуется проверить ранние, современные, лицензированные, моторизованные и многокомпонентные продукты.

## Следующие проверки

- Ранний пример с неоднозначными Toy # и несколькими таблицами/годами.
- Современный лицензированный продукт с Character/IP attribution.
- Team Transport или другой многокомпонентный набор с несколькими компонентами.
- Продукт с механизмом/функцией и несколькими состояниями.
- Racing release с отдельными Toy #, Series #, racing number, team и driver.
- Проверка конфликтов и повторных имён между эпохами.

## Ограничение текущего этапа

Это предварительная валидация требований на небольшой репрезентативной выборке, не утверждённая схема БД и не окончательная нормализация каталога.


## Проверочная партия 2: Other Early Series (2026-11-10)

Проверены пять source-preserving CSV и соответствующие QA:

- `research/extractions/OTHER-EARLY-SERIES-ACTION-CYCLES.csv` — 26 строк, 1 таблица.
- `research/extractions/OTHER-EARLY-SERIES-ACTION-RACERS.csv` — 67 строк, 2 таблицы.
- `research/extractions/OTHER-EARLY-SERIES-ATTACK-PACK.csv` — 48 строк, 9 таблиц (включая отдельную yearly-list/navigation-like таблицу, не смешивать с товарными строками).
- `research/extractions/OTHER-EARLY-SERIES-HOT-WHEELS-RAILROAD.csv` — 31 строка, 3 таблицы.
- `research/extractions/OTHER-EARLY-SERIES-KEY-FORCE.csv` — 15 строк, 3 таблицы.

### 4. Action Cycles

В таблице Toy # 8345 повторяется для Bike 1 в нескольких цветовых записях (в том числе Orange Metallic, Blue и Green). Заголовки: Toy #, Name, Series, Color, Photo.

Подтверждение:
- Одинаковый Toy # может обозначать несколько строковых цветовых вариантов одной модели в рамках одной исходной страницы.
- Нельзя ни считать Toy # глобальным идентификатором варианта, ни автоматически сливать строки в одну запись.
- Color и Series остаются source attributes; Photo — evidence конкретной строки.

### 5. Action Racers

В первой таблице (65 строк) Toy # 2415 встречается как минимум в двух разных строках с разными названиями: BMW M3 и Ferrari 328 GTS. Вторая таблица содержит ещё 2 строки. QA фиксирует 2 таблицы, 67 строк, 109 ссылок.

Подтверждение:
- Toy # может коллидировать даже внутри одной таблицы/одной тематической страницы у разных названий.
- Любой candidate key должен включать источник и scope (как минимум страницу/таблицу/строку), а Toy # сохраняется как typed source identifier без предположения об уникальности.
- Name-to-casting links полезны как source assertions, но ссылка Fandom не должна автоматически становиться окончательным casting identity.

### 6. Attack Pack

В семи товарных таблицах 47 строк (таблица 9 отдельно отражает yearly lists и не является обычной товарной таблицей). Основные заголовки включают Toy #, Year, Casting Name, Allegiance, Country, Photo; в одной из таблиц Allegiance и/или Country отсутствуют в самой схеме. Например, Slashcat (Toy # 0692, 1992) имеет Allegiance = Heroic Cat Pack и Country = Global.

Подтверждение:
- Allegiance — отдельное исходное отношение/атрибут тематической принадлежности; не переименовывать автоматически в Series, Team или Manufacturer.
- Значения Allegiance могут иметь собственные ссылки/изображения (в примере категория Heroic Cat Pack), значит сущность/термин принадлежности может быть отдельно разрешён позже.
- Разные таблицы одной страницы имеют различающиеся наборы колонок; nullable поля и table-level schema обязательны.
- Table 9 с 324 ссылками должна оставаться отдельным source artifact, не интерпретироваться как 324 товарных записи.

### 7. Hot Wheels Railroad

QA: 3 таблицы, 31 строка, 31 embedded image, 98 ссылок. Первая таблица (14 строк) описывает rolling stock: Year, Model Name, Color, Railroad/Company Represented, Base Color / Type, Country, Number, Photo. Например, Santa Fe F40PH Diesel (1983) связан с Atchison, Topeka and Santa Fe Railway и имеет Number 5590. Вторая таблица (5 строк) содержит Bundle name и Car 1–Car 3; третья (12 строк) — Name, Cars included и Notes.

Подтверждение:
- Railroad/Company Represented — внешняя организация/бренд-прототип, а не Hot Wheels Series и не производитель игрушки.
- Number (например 5590) — отдельное типизированное поле, его нельзя автоматически считать Toy # или racing number.
- Bundle name, Car 1–Car 3 и Cars included подтверждают необходимость моделировать набор как отдельный продукт/offer с упорядоченными компонентами; компонентные модели остаются самостоятельными сущностями.
- У набора могут быть состав и заметки в виде текстового перечня, требующие component-resolution с provenance и confidence, а не безусловного парсинга.

### 8. Key Force

QA: 3 таблицы, 15 строк, 16 embedded image references, 43 ссылки. Первые две таблицы используют Toy #, Year, Casting Name, Allegiance, Photo; третья таблица не содержит Allegiance. Например, Toy # 3727 / Keymmander Police Car и Toy # 3704 / Jet Threat Rocket Bike имеют Allegiance = Keymasters.

Подтверждение:
- Тематическая/сюжетная принадлежность может отсутствовать в части таблиц, поэтому её нельзя делать обязательной на уровне Product.
- Toy #, Year и Casting Name остаются разными полями с разными ролями.
- Табличная структура и заголовки должны сохраняться для интерпретации пропущенных колонок.

## Обновлённые выводы после партии 2

6. Toy # collisions не являются только исторической аномалией: Action Racers показывает разные модели под одним Toy # в одной таблице. Source-row identity обязана быть независимой от Toy #.
7. Один и тот же Toy # может повторяться и для цветовых записей одного имени (Action Cycles), и для разных имён (Action Racers). Нужны отдельные сущности SourceRecord, SourceIdentifier и Candidate Product/Casting match.
8. Термины Allegiance, Railroad/Company Represented и Number семантически различны; нельзя сводить все «группы» и «номера» к универсальным Series/Team/Code.
9. Наборы и rolling-stock bundles требуют relation table для компонентов с порядком, ролью и исходной формулировкой.
10. Отсутствующие колонки зависят от таблицы, а не обязательно означают пустое значение в единой универсальной схеме.

## Обновлённая очередь проверки

- Современный лицензированный Character Cars продукт: отделить IP/franchise, character, vehicle/casting и license attribution.
- Car Culture Team Transport: проверить роль hauler, trailer, car и set-level SKU.
- Key Force / Action Cycles: отдельный follow-up по функции/механизму на основании описаний и страниц моделей; CSV сами по себе не доказывают механику.
- Pro Racing: typed racing number, driver, team, sponsor и series scope.
- Сверка кандидатов межкаталожных casting matches с доказательствами, не только совпадением названия.


## Проверочная партия 3: Character Cars (2026-11-10)

Проверены пять лицензированных/character-based страниц, их QA и исходные CSV (включая split parts для крупных страниц):

| Источник | Таблиц | Строк | Изображений в таблицах | Ссылок |
|---|---:|---:|---:|---:|
| Minecraft Character Cars | 4 | 24 | 48 | 96 |
| Marvel Character Cars | 27 | 246 | 456 | 955 |
| Star Wars Character Cars | 33 | 317 | 582 | 1 213 |
| Sonic the Hedgehog Character Cars | 2 | 4 | 8 | 16 |
| Jurassic World Character Cars | 7 | 25 | 44 | 95 |
| **Всего** | **73** | **616** | **1 138** | **2 375** |

Источники:
- `research/extractions/MODERN-SPECIAL-SERIES-MINECRAFT-CHARACTER-CARS.csv`
- `research/extractions/MODERN-SPECIAL-SERIES-MARVEL-CHARACTER-CARS.csv` и `...-PART-02.csv`
- `research/extractions/MODERN-SPECIAL-SERIES-STAR-WARS-CHARACTER-CARS.csv` и `...-PART-02.csv`
- `research/extractions/MODERN-SPECIAL-SERIES-SONIC-THE-HEDGEHOG-CHARACTER-CARS.csv`
- `research/extractions/MODERN-SPECIAL-SERIES-JURASSIC-WORLD-CHARACTER-CARS.csv`

### 9. Общая структура Character Cars

В типичной таблице используются Series #, Toy #, Casting Name, Body Color, Wheel Type, Notes, Photo Loose и Photo Carded. Например:
- Minecraft 2017: Series # 1/6, Toy # DXT22, Casting Name Creeper.
- Marvel 2014: Series # 1, Toy # BDM74, Casting Name Iron Man.
- Star Wars 2014: Series # 01, Toy # CGW36, Casting Name Darth Vader.
- Jurassic World 2018: Series # 1/5, Toy # FLJ04, Casting Name Tyrannosaurus Rex.

Подтверждение:
- Casting Name в этой продуктовой категории может быть именем персонажа/существа, а не названием обычного автомобильного кузова. Не следует насильно помещать его в поле `vehicle_model_name`.
- Нужны отдельные типы/сущности для IP или franchise, character/creature, character-based toy design/casting и коммерческого release.
- Связь между персонажем и дизайном машины должна быть явно типизированной (например, character-inspired design), а не подменять идентичность самого персонажа или реального автомобиля.
- Лицензионная принадлежность страницы/серии не доказывает, что каждая строка имеет одинакового правообладателя на всех рынках и во все годы; сохранять source scope и evidence.

### 10. Series Position и Toy #

В Minecraft и Jurassic World позиции представлены как дроби (1/6, 1/5); Star Wars использует, например, 01; Marvel — числовые значения; Sonic в таблицах 2022 года вообще не имеет Series #. При этом Toy # остаётся отдельным алфавитно-цифровым идентификатором (DXT22, BDM74, CGW36, GRM47, FLJ04).

Подтверждение:
- Series Position необязателен и имеет локальный scope: год/таблица/assortment.
- Сохранять исходное форматирование номера позиции (например 01 vs 1) и raw value; нормализованное числовое значение не должно уничтожать display form.
- Toy # должен быть отдельным typed identifier, независимым от Series Position.

### 11. Images and package evidence

Стандартные таблицы разделяют Photo Loose и Photo Carded. В Sonic для loose image присутствует явный placeholder `Image Not Available`, в то время как carded photo доступно.

Подтверждение:
- Изображение должно иметь роль/тип (loose product, carded/package front, set/package evidence, placeholder), а не просто общий массив фотографий.
- Отсутствующая фотография и изображение-заглушка — разные состояния; не считать placeholder подтверждением внешнего вида продукта.
- Фото упаковки является evidence packaging/release, а не заменой фото loose item.
- Image metadata, file link, alt text и связь с конкретной source row должны сохраняться.

### 12. Notes, wheels and base codes

В примерах Notes содержит текст `Base code(s):` и один или несколько кодов; Wheel Type сочетает описательный текст и ссылки на wheel-code pages (например Black DD8, Gold OH5SP, Chrome Red & Black PR5, RA6, Chrome Orange BLOR).

Подтверждение:
- Wheel configuration должна поддерживать сочетание finish/color и code, а не один свободный текстовый атрибут.
- Base codes могут быть множественными и относиться к примечаниям исходной строки; хранить их как отдельные extracted assertions с provenance, не теряя исходный текст Notes.
- Ссылка на страницу кода — доказательство того, что источник ссылается на этот код, но не независимое подтверждение фактической конфигурации каждого физического экземпляра.

### 13. Jurassic World: mixed product and set scope

QA фиксирует 7 таблиц и разные секции: годовые Character Cars, Complete Collection, Jurassic World Dominion 5-Car Collector Set и Playsets. Значит, одна страница Character Cars содержит не только отдельные character-car rows, но и строки агрегированных наборов/игровых комплектов.

Подтверждение:
- Не считать каждую строку страницы экземпляром одного и того же типа Product.
- Нужны product subtype/category и relationships for set membership/components.
- Complete Collection / 5-Car Collector Set могут описывать агрегаты, а Playsets — отдельные комплекты с дополнительными компонентами; компонентный состав должен быть сохранён в исходной формулировке до подтверждённого resolution.

## Обновлённые выводы после партии 3

11. Лицензированные Character Cars требуют моделировать как минимум Franchise/IP, Character, Character-inspired design/casting, Release, Series Position и Packaging/Image Evidence как разные понятия.
12. Название персонажа в Casting Name не всегда является casting автомобиля в обычном смысле; модель данных должна поддерживать non-vehicle/character-shaped designs и их связи.
13. Series Position может отсутствовать или иметь разные display formats в пределах одного тематического направления.
14. Loose image и carded image несут разные типы доказательств; placeholder image нельзя считать реальным изображением модели.
15. Одна Fandom-страница может объединять отдельные машины, коллекционные наборы и playsets. Тип строки и связи компонентов должны определяться по таблице/строке, а не по заголовку страницы.

## Обновлённая очередь проверки

- Car Culture Team Transport: отдельно проверить vehicle, hauler/trailer, bundle SKU и роли компонентов.
- Pro Racing: typed racing number, driver, team, sponsor и series scope.
- Сопоставить Character Cars с другими Hot Wheels releases, не объединяя персонажа и автомобильный casting по совпадению названия.
- Проверить лицензии/IP и ownership assertions на конкретных строках и упаковках, где источник это явно подтверждает.


## Проверочная партия 4: Car Culture Team Transport (2018–2022)

Проверены годовые extraction QA и CSV за 2018–2022 годы:

| Год | Таблиц | Строк | Embedded images |
|---|---:|---:|---:|
| 2018 | 3 | 14 | 18 |
| 2019 | 6 | 22 | 30 |
| 2020 | 4 | 22 | 30 |
| 2021 | 6 | 29 | 40 |
| 2022 | 6 | 29 | 40 |
| **Всего** | **25** | **116** | **158** |

Источники: `research/extractions/MODERN-SPECIAL-SERIES-{2018..2022}-CAR-CULTURE-TEAM-TRANSPORT.csv` и соответствующие `-EXTRACTION-QA.md`.

### 14. Bundle identity vs component castings

В годовых таблицах используются Toy #, Series #, Casting, Body Color, Wheel Type, Notes, Photo Loose и Photo Carded. В строках встречается HTML `rowspan="2"` для Toy #, Series # и/или изображения упаковки. Например, в 2018 Mix 1 Toy # FLF61 и Series # 1 повторяются контекстом rowspan для двух компонентных строк. В 2022 изображение упаковки явно показывает Ford C-800 and Galaxie.

Подтверждение:
- Toy # и Series # могут идентифицировать bundle/release, а не каждый входящий в него casting по отдельности.
- Нужна сущность Bundle/Set Release и таблица BundleComponent с порядком, ролью компонента и ссылкой на отдельный casting/product release.
- Rowspan — не просто форматирование: он передаёт наследуемый контекст, который должен быть восстановлен в derived interpretation, при этом исходная пустая ячейка и HTML атрибут должны оставаться сохранёнными.
- Нельзя создавать два самостоятельных SKU только потому, что extraction содержит две строки Castings под одним rowspan Toy #.

### 15. Mix, exclusives and source table boundaries

По годам встречаются Mix 1–4 и отдельные эксклюзивные секции (например Supreme Exclusive в 2019, Walmart Legends Tour Exclusive в 2021–2022). Некоторые дополнительные таблицы содержат строки, но QA не обнаруживает в них заголовков (например таблицы с двумя строками после основных таблиц).

Подтверждение:
- Mix/Exclusive — scoped assortment/market-release context, а не автоматически отдельный глобальный product family.
- Источник может содержать строки без заголовков, и QA корректно сохраняет их с флагом. Для интерпретации требуется raw HTML/context, а не отбрасывание.
- Нужны market/exclusivity attributes с source provenance; нельзя выводить конкретного retailer/territory из одного только section name без подтверждения.

### 16. Component-level attributes and package evidence

В каждой компонентной строке отдельно указаны Casting, Body Color, Wheel Type и Notes; Notes может содержать несколько base codes и метки New Casting. Carded photo часто объединена rowspan и относится к общему комплекту, тогда как loose photos различаются по компонентам. В 2021 для некоторых rows используется placeholder Image Not Available.

Подтверждение:
- Bundle package image относится к bundle-level evidence; loose images относятся к component-level evidence.
- Base codes, wheel configuration, body color и casting notes должны относиться к компоненту, если источник выводит их в component row.
- Изображения-заглушки сохраняются как placeholders, не как реальные product photos.
- New Casting — исходное утверждение о casting lifecycle, его следует хранить как source assertion с датой/контекстом, а не как необратимый boolean на всей сущности casting.

## Обновлённые выводы после партии 4

16. Team Transport подтверждает, что один Toy #/Series Position может описывать release-bundle, внутри которого несколько самостоятельных casting components.
17. Нужна двухуровневая система provenance: bundle-level evidence (например carded packaging) и component-level evidence (loose photo, color, wheel, base code).
18. Rowspan и headerless source tables нельзя сводить к простым пустым значениям; требуется source-preserving record плюс отдельно вычисленный inherited context.
19. Mix и retailer exclusives — контекст выпуска/распределения; не обязательно самостоятельная идентичность casting или product family.


## Проверочная партия 5: Car Culture Team Transport (2023–2026)

Проверены годовые extraction QA и все CSV parts за 2023–2026 годы. В 2025 году отдельно учтены обе части CSV, содержащие Gallery items.

| Год | Таблиц | Строк товарных таблиц | Embedded images | Отдельные Gallery items |
|---|---:|---:|---:|---:|
| 2023 | 7 | 31 | 43 | 0 |
| 2024 | 6 | 30 | 41 | 0 |
| 2025 | 6 | 31 | 42 | 9 |
| 2026 | 6 | 30 | 41 | 0 |
| **Всего** | **25** | **122** | **167** | **9** |

Итого в товарных таблицах: 122 строки, 25 таблиц и 167 embedded image references. Дополнительно: 9 самостоятельных Gallery records за 2025 год. В основном CSV 2025 года находятся 4 Gallery records, ещё 5 записей находятся в PART-02 CSV. QA сообщает 9 Gallery items суммарно. 2023 включает секцию Fast & Furious и Walmart Legends Tour Exclusive; в 2024–2026 присутствуют Walmart Legends Tour Exclusive. Исходные CSV и QA не изменялись.

### 20. Bundle-level identifiers remain separate from component rows

Во всех четырёх годах повторяется схема Team Transport: Toy # и Series # могут быть указаны один раз на несколько component rows через HTML rowspan. Например, в 2023 Toy # HKF39 / Series #50 объединяет Aero Lift и '23 Ford Mustang RTR Spec 5; в 2024 HRV43 / #62 объединяет Second Story Lorry и Fiat 131 Abarth; в 2025 JBM29 / #74 объединяет 2023 Land Rover Defender 110 и HW Rally Trailer; в 2026 JHX87 / #86 объединяет Fleet Street и '20 Toyota GR Supra.

Подтверждение:
- Bundle/SKU identity и component casting identity должны быть разными сущностями/уровнями.
- Исходные пустые ячейки и rowspan сохраняются; унаследованные значения можно хранить как derived context, но нельзя подменять ими raw source.
- Компонентные роли (hauler, trailer, passenger/race car и др.) должны быть отдельными relationship attributes с provenance, а не выводиться только из порядка или названия.

### 21. Mix and themed/retailer sections are release context

Mix 1–4 сохраняются как локальные assortment groups. В 2023 дополнительно есть Fast & Furious и Walmart Legends Tour Exclusive; Walmart Legends Tour Exclusive встречается также в 2024–2026.

Подтверждение:
- Section label относится к source/release context и не становится автоматически глобальной Series, Franchise или Manufacturer.
- Для Fast & Furious требуется отдельное подтверждение тематической/лицензионной связи на уровне release/component; заголовка секции недостаточно для юридических утверждений.
- Walmart Legends Tour Exclusive фиксируется как source assertion об эксклюзивном контексте; retailer, territory и distribution scope не следует домысливать сверх данных источника.

### 22. Component-level attributes and lifecycle notes

В строках компонентов сохраняются Casting, Body Color, Wheel Type и Notes; Notes включают несколько Base codes и утверждения вроде New Casting (2025 Land Rover Defender) и New Die-Cast Chassis (2025 Jaguar Mk1).

Подтверждение:
- Base codes, body color и wheel type относятся к component row, если именно там они представлены.
- New Casting и New Die-Cast Chassis являются разными source assertions; их нельзя сводить к одному флагу или считать постоянным свойством без временного/источникового контекста.
- Исходный Notes text и связанные ссылки на Wheel Type/base-code pages должны сохраняться вместе с нормализованными интерпретациями.

### 23. Gallery records and embedded product images are separate evidence streams

В 2025 году QA подтверждает 9 отдельных Gallery items, извлечённых в двух CSV parts, отдельно от 42 embedded product-table image references.

Подтверждение:
- Gallery item не следует автоматически считать loose/carded product photo: это самостоятельный тип source evidence с собственными caption, alt, filename, file link и image metadata.
- При извлечении реального адреса изображения нельзя полагаться только на img src: в некоторых строках src может быть техническим data: placeholder, тогда как настоящий файл указан в оборачивающем link href.
- Image evidence должна хранить исходный HTML/metadata и роль/контекст, а не только один URL.

## Обновлённые выводы после партии 5

20. Team Transport 2023–2026 подтверждает устойчивую bundle/component модель, наблюдавшуюся в 2018–2022; это не исключение отдельных лет.
21. Section labels Mix, Fast & Furious и Walmart Legends Tour Exclusive требуют scoped release/source context, а не автоматического создания глобальных сущностей Series/IP/Manufacturer.
22. Component notes различают New Casting и New Die-Cast Chassis; исходные утверждения должны быть типизированы и привязаны к источнику/времени.
23. Gallery records и embedded product images — разные evidence streams; 2025 год подтверждает необходимость отдельного Gallery record type и корректного чтения image link href при техническом data URI в img src.


## Проверочная партия 6: Pro Racing (1997–2000)

Проверены годовые QA и CSV за 1997–2000 годы. В 1998 CSV превышает 1 MB: обычный Contents fetch вернул пустое содержимое, поэтому полный текст был прочитан по Git blob SHA и разобран повторно; количество строк совпало с QA.

| Год | Таблиц | Строк | Embedded images | Ссылок |
|---|---:|---:|---:|---:|
| 1997 | 6 | 83 | 156 | 356 |
| 1998 | 14 | 205 | 400 | 848 |
| 1999 | 18 | 185 | 343 | 752 |
| 2000 | 19 | 155 | 304 | 639 |
| **Всего** | **57** | **628** | **1 203** | **2 595** |

QA для всех четырёх лет подтверждает сохранение исходного порядка, границ таблиц, headers, raw row/cell HTML, ссылок и image attributes. Отдельные Gallery items не извлекались в этих годовых проходах; строки Gallery/navigation-like tables, если они присутствуют в CSV, не следует принимать за отдельные товарные фото.

### 24. Racing identity is a structured context, not one flat Team/Number field

В NASCAR-подобных таблицах 1997–2000 используется поле `Team / Number`, содержащее смешанные строки вроде `Morgan-McClure Motorsports #4`, `Hendrick Motorsports #5`, `Petty Enterprises #43`, а иногда только `#8` или `#9`. Отдельно присутствует `Primary Sponsor` (например Kodak, Kellogg's, STP, Valvoline). В 1998 таблицы Indy/open-wheel для Reynard 97I и Swift 007.i используют другую схему: `Team n°`, `Team`, `Year #`, `Series`, `Photo Loose`, `Photo Packaged`.

Подтверждение:
- Нельзя сводить Team, racing number, Primary Sponsor, Year # и Series в одно универсальное поле.
- Сохранять исходные названия полей и строки; нормализованное разделение команды/номера/спонсора допустимо только как derived interpretation с provenance.
- `Team` в 1998 open-wheel таблице (например Target, Walker, Alumax) не следует автоматически считать тем же типом значения, что `Team / Number` в NASCAR-таблицах.
- Гоночный номер является контекстным атрибутом участия/ливреи, а не Toy # и не Series Position.

### 25. Toy # reuse, variants and cross-assortment listings

В 1997 один Toy # повторяется между Collector 1st Edition, Short Track 1st Edition и Superspeedway 1st Edition, иногда с одинаковой машиной и отдельными source notes о направлении автомобиля/решётке/спойлере. Например, Toy #17407–17414 встречаются в нескольких assortment sections. В 1998 также есть повторы Toy # между разными секциями и записями; в 1999 Toy #25001–25004 имеют пары `Dark Tape` / `Light/ White Tape`, а Toy #22570 содержит варианты упаковки/оттенка. В 2000 Toy #28351 используется у двух записей Chevrolet Monte Carlo / Sabco Racing #42 с BellSouth и BellSouth Mobility (`Alternate Livery`).

Подтверждение:
- Toy # не является глобальным PK для casting или release и не гарантирует уникальность строки.
- Различать repeated source listing, assortment membership, packaging variation, livery/tampo variation и отдельный casting только по совокупности source evidence.
- Не сливать строки при совпадении Toy #; сохранять каждую запись и её section/table/source row.
- Разные Notes могут описывать варианты упаковки, направление/детали кузова или ливрею; это не один общий свободный текст без типа evidence.

### 26. Tool Box and set/packaging relationships

В 1998–2000 присутствуют отдельные Tool Box tables с Casting=`Tool Box`, при этом Team / Number и Primary Sponsor повторяют гоночный контекст конкретных машин. Notes включают явные формулировки `Packaged with Ford Thunderbird` и `Packaged with Ford Taurus`. В 1998 также есть тематические multi-car/set sections (например Roush Racing Set, PLAYERS INC Special Edition Set, Toy Story 2-related releases).

Подтверждение:
- Tool Box — самостоятельный product/casting type, не гоночный автомобиль только потому, что его строка содержит racing team/sponsor context.
- `Packaged with ...` является явным source-backed component/packaging relationship; хранить его как связь упаковки/комплекта с компонентом, а не подменять Casting.
- Set/packaging identity и individual casting identity должны быть разными уровнями; состав набора не выводить только из названия секции.

### 27. Source schemas vary by racing discipline and year

В 1997–2000 обнаружены разные схемы: стандартная 11-колоночная Pro Racing, варианты порядка Photo Loose/Photo Packaged, схемы без Interior Color, Tool Box tables с 10 колонками, open-wheel schema с шестью колонками и таблицы Gallery/navigation без обычных product headers. QA сохраняет исходные заголовки и строки, а не нормализует их в один шаблон.

Подтверждение:
- Поля должны быть nullable и schema-scoped; отсутствие поля в таблице не равно пустому значению у товара.
- Photo Packaged, Photo Carded и Photo Boxed являются исходными role labels, которые следует сохранять до нормализации image evidence.
- Gallery/navigation tables нужно отличать от product tables по структуре и контексту, а не по наличию слова Pro Racing.

## Обновлённые выводы после партии 6

24. Pro Racing требует разделения Team, racing number, Primary Sponsor, Year # и Series; их нельзя объединять в одно поле.
25. Повтор Toy # между ассортиментами, вариантами ливреи и упаковки подтверждает, что он не является глобальным ключом; исходные строки остаются самостоятельными source records.
26. Tool Box и тематические sets показывают, что racing context может быть у неавтомобильных продуктов и упаковок; необходимы отдельные product type и package/component relationships.
27. Схема Pro Racing зависит от года и гоночной дисциплины; source headers и table scope должны сохраняться без насильственного сведения к единому набору колонок.


## Проверочная партия 7: Pro Racing (2001–2005)

Проверены годовые QA и CSV за 2001–2005 годы.

| Год | Таблиц | Строк | Embedded images | Ссылок |
|---|---:|---:|---:|---:|
| 2001 | 16 | 93 | 94 | 192 |
| 2002 | 13 | 93 | 86 | 189 |
| 2003 | 16 | 134 | 139 | 268 |
| 2004 | 7 | 71 | 70 | 157 |
| 2005 | 4 | 21 | 38 | 68 |
| **Всего** | **56** | **412** | **427** | **874** |

### 28. Team number and team/livery labels persist, but Series context changes

В 2001–2004 основная схема — `Team n°`, `Team`, `Wheels`, `Series`, `Photo`; в 2005 заголовок меняется на `Team #`. `Team` содержит значения вроде Kelloggs, Pfizer, M&M's Yellow, Alltel, Tide, Valvoline и другие, то есть это source label для командно-спонсорской/ливрейной идентичности, а не надёжно выделенное юридическое имя гоночной команды. В 2003 STOCKERZ появляется отдельная схема `Casting`, `Team`, `Team #`, `Wheels`, `Photo`, `Photo Sealed`.

Подтверждение:
- Сохранять Team n° и Team # как разные source header labels, даже если нормализованный слой позднее сопоставит их с одним concept.
- Team number не является Toy #; у большинства записей 2001–2005 Toy # вообще отсутствует в source schema.
- `Team` не следует автоматически трактовать как manufacturer, formal racing team или Primary Sponsor без отдельного подтверждения.
- `Series` является отдельным source context: Pro Racing, Pro Racing Recreational Series, Pro Racing Treasure Hunt, STOCKERZ, Race Day, Pro Racing Showcase, Pro Racing Artist Collection, Pro Racing Justice League и Cars Movie Promo.

### 29. Never-released status is not a missing photo

В 2001, 2002 и 2003 строки содержат текст `NEVER RELEASED` в колонках Photo, Photo Loose или Photo Carded. Примеры: Anglia Panel Truck #45 (2001), несколько моделей в 2002, а также ATV/Bass Boat/Hammered Coupe entries в 2003.

Подтверждение:
- Значение `NEVER RELEASED` — содержательное source assertion о статусе выпуска, а не filename, image URL или обычное пустое поле изображения.
- Image evidence и release status должны быть разными типами данных; не терять текст статуса при нормализации фото-колонок.
- Не превращать статус в глобальное утверждение о casting: он относится к конкретной строке/версии/заявленному ассортименту источника, пока не проверен отдельно.

### 30. Item Number, team number and product identifier are distinct

В 2004 появляется дополнительный `Item Number` в таблице Dodge Intrepid Stocker, но проверенные значения пусты; строка Pit Cruiser также имеет пустой Item Number при заполненных Team n° и Team. В 2001 четыре строки используют дополнительные поля Toy # и Card, но основной schema Toy # не содержит.

Подтверждение:
- Не подставлять Team n°/Team # в Item Number или Toy #.
- Отсутствие значения Item Number при наличии колонки — missing value, а отсутствие самой колонки в других таблицах — schema scope.
- Разные source schemas могут быть локальными даже на одной странице/в одном году.

### 31. Showcase variation tables preserve image-view and unheaded context

В 2004 секция Showcase Variation содержит две строки в таблице без detected headers: первая перечисляет `Side View`, `Top View`, `Base View`, вторая содержит пустые значения. Другие unheaded tables в 2001–2005 содержат годовые навигационные ссылки; они остаются в extraction как source rows, но не являются товарными позициями.

Подтверждение:
- Unheaded table не должна автоматически становиться product table; требуется учитывать cell content и section context.
- Side/Top/Base View — image-view labels, потенциально относящиеся к evidence angles, а не атрибуты casting или release.
- Навигационные строки сохраняются как raw source data, но исключаются из product entity creation.

## Обновлённые выводы после партии 7

28. Team n°/Team #, Team label, Series и Item Number являются разными source concepts; team number не заменяет product identifier.
29. NEVER RELEASED в фото-колонках является release-status assertion, а не изображением или пустым фото.
30. Showcase Variation подтверждает необходимость классифицировать unheaded tables по содержимому и роли; Side/Top/Base View могут описывать угол image evidence.


## Проверочная партия 8: Basic Pro Racing и Pro Racing 1:43 Scale

Проверены Basic Pro Racing Series и Larger Scale Pro Racing 1:43 Scale.

| Dataset | Таблиц | Строк | Embedded images | Ссылок |
|---|---:|---:|---:|---:|
| Basic Pro Racing Series | 11 | 124 | 245 | 504 |
| Pro Racing 1:43 Scale | 1 | 41 | QA не сообщает | QA не сообщает |

### 32. Basic Pro Racing is a separate release scope, not a duplicate of annual Pro Racing

Basic Pro Racing Series содержит 124 строки за 1997–2002 годы, включая Basic Pro Racing Cart, Grand Prix Kart Racing и отдельную Roush Racing/Valvoline Diamond Anniversary section. Основная схема совпадает с ранними NASCAR-like таблицами (`Casting`, `Team / Number`, `Primary Sponsor`, body/base, wheel, Toy #, Country, Notes, package/loose photos), но это отдельный source dataset и assortment context. В 2002 встречается alphanumeric Toy # `BA003-0910`; другая строка имеет пустой Toy # и note о baggie series, содержащей преимущественно premium cars.

Подтверждение:
- Не объединять Basic Pro Racing и annual Pro Racing только по совпадению Casting/Team/Toy #; хранить source dataset, page, section и release context.
- Toy # должен храниться как строковый идентификатор, поддерживающий alphanumeric values и leading zeros; не приводить к integer.
- Baggie series и Kart Racing sections требуют собственных product/packaging context; не предполагать стандартную blister/card упаковку.
- Повтор Toy #17416 в Basic Pro Racing 1997 с разными sponsor/variant descriptions показывает, что Toy # не является ключом для одной неизменной конфигурации.

### 33. Pro Racing 1:43 has a distinct scale-specific source schema

1:43 dataset содержит одну таблицу Vehicles и 41 строку. Исходные 11 headers: Casting, Year, Color, Tampo, Base Color, Interior Color, Wheel Type, Toy #, Country, Notes, Photo. Export дополнительно содержит нормализованные поля Col #, Series, Sticker и другие; однако Col #, Series и Sticker отсутствуют в исходных headers и должны оставаться null/unsupported, а не заполняться догадками.

Подтверждение:
- 1:43 scale — scope этой таблицы/коллекции; его следует сохранять на уровне source collection/release, не выводить из Casting name.
- `Year` обозначает год гоночной машины/модельного представления в source table, не обязательно год выпуска игрушки.
- `Tampo` содержит как racing numbers (`#17`, `#18`, `#1`, `#2`), так и driver names (`David`, `Mika`, `Kimi`); это marking/decal evidence, не Toy # и не автоматически отдельный Driver entity.
- В 41 строке Toy # заполнен только у одной записи (55573); остальные пустые значения не следует восстанавливать из Tampo/Year.
- Notes содержат packaging relationships: Single Pack, World Champions 2-Pack, Constructors Champions 4 Pack, Part of a 3 Pack, Comes in a 2 Pack, Book package. Set/package membership должна быть отдельной связью.
- Photo values смешивают Image Not Available placeholders, website assets, prototype/sample references и несколько связанных image labels в одной ячейке. Это не однородный image URL field; сохранять raw value и тип evidence.
- Notes вроде `Might be a 2nd version` — неопределённое source assertion, а не подтверждённый variant relationship.

## Обновлённые выводы после партии 8

32. Basic Pro Racing — отдельный assortment/source scope; повторные идентификаторы и похожие поля не дают основания сливать его строки с annual Pro Racing.
33. Toy # должен поддерживать буквенно-цифровые строки; Year в 1:43 таблице относится к машине/гоночному сезону, а не автоматически к выпуску игрушки.
34. 1:43 Tampo может хранить racing numbers и driver-name markings, тогда как Photo/Notes могут содержать placeholder, website asset, prototype и set-package evidence; эти роли требуют раздельной типизации.


## Проверка Gallery evidence: Pro Racing (2026-11-10)

Сверены 13 Pro Racing-related pages в `GALLERY-SCAN.csv`, `GALLERY-PROGRESS.csv` и consolidated `GALLERY-EXTRACTION.csv`: annual Pro Racing 1997–2005 (9 страниц), Basic Pro Racing Series, Hot Wheels Racing Selects, Team Transporter и Larger Scale Pro Racing 1:43 Scale.

Итог: 13 страниц, 17 Gallery containers, 100 Gallery items. Annual Pro Racing 1997–2005 даёт 29 items на четырёх страницах (1998: 4; 1999: 12; 2000: 12; 2002: 1); остальные пять годовых страниц корректно классифицированы NO_GALLERY. Смежные страницы дают ещё 71 item: Basic Pro Racing 13, Racing Selects 1, Team Transporter 2, 1:43 Scale 55.

Все 100 записей уже присутствуют в `GALLERY-EXTRACTION.csv`, все page-level counts совпадают с `GALLERY-SCAN.csv`, все 100 ключей `source page + gallery index + item index` уникальны. Новые строки в master не добавлялись, чтобы не создать дубликаты. `GALLERY-PROGRESS.csv` уже содержит все 13 страниц со статусом SCANNED и соответствующими counts.

Модель данных: Gallery item является отдельным evidence record, а не автоматически product photo или отдельным товаром. Pro Racing examples включают international card artwork, multi-car/set packaging views, pre-production sample group photo, advertising inserts и 1:43 prototypes/website assets. Filename, alt, caption, file-page link, image URL и raw markup должны оставаться доступными; classification as carded/loose/prototype/advertisement requires caption/source context.


## Pro Racing inline image audit: NO_GALLERY annual pages (2026-11-10)

Audited the five annual pages 1997, 2001, 2003, 2004, and 2005 that have no dedicated Gallery. Their source HTML contains 497 image elements inside product tables (156, 94, 139, 70, and 38 respectively); all 497 are already preserved in the corresponding annual extraction CSVs through `cell_image_metadata_json` and `raw_row_html`. The 30 remaining image elements are site/community header and Fandom footer branding assets. No additional article-body inline images were found. No second image CSV was created and no Gallery master rows were added. Detailed reconciliation: `research/extractions/PRO-RACING-INLINE-IMAGE-AUDIT.md`.


## Pro Racing Gallery evidence classification (2026-11-10)

First-pass evidence-type classification completed for all 100 existing Pro Racing Gallery items: 9 card-art/card-variation records; 41 packaging/set/comparison records; 4 advertising/promotional records; 35 prototype/pre-production/sample records; 2 damaged-packaging records; 2 resin-driver-figure records; 5 website assets; 1 signed hauler/variant evidence record; and 1 unclassified Racing Selects lot image. This is not product identity resolution: uncertain source associations remain explicit, and multiple views of one set/prototype are not separate products. Record-level mapping: `research/galleries/PRO-RACING-GALLERY-CLASSIFICATION.md`.
