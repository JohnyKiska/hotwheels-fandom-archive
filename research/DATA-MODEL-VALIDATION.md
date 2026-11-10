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
