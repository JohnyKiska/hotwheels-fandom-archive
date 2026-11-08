# HW Catalog Research

Единая точка входа для результатов исследования архива Hot Wheels Fandom и других источников.

## Правила ведения

- **Fact** — факт, подтверждённый конкретным источником.
- **Observation** — наблюдение по сохранённому HTML, ещё не проверенное независимым источником.
- **Hypothesis** — рабочее объяснение, требующее проверки.
- **Unresolved** — противоречие или вопрос без достаточного подтверждения.
- **Design requirement** — требование к будущей модели данных, выведенное из наблюдений; это ещё не утверждённая схема БД.

Для каждого содержательного вывода указывать источник (путь в архиве или внешний URL), область проверки и статус. Не повышать статус автоматически. Сохранять исходные значения и формулировки источника.

## Документы

| Документ | Назначение |
|---|---|
| [FINDINGS.md](FINDINGS.md) | Наблюдения и подтверждённые факты |
| [UNRESOLVED.md](UNRESOLVED.md) | Противоречия и вопросы на проверку |
| [DATA_MODEL_REQUIREMENTS.md](DATA_MODEL_REQUIREMENTS.md) | Требования к будущей модели данных |

## Исследовательский охват

Исходный архив: [hotwheels-fandom-archive](https://github.com/JohnyKiska/hotwheels-fandom-archive).

В архиве сохранено 532 файла: 530 HTML/HTM и 2 CSV (согласно инвентаризации, выполненной 2026-11-08). Структура папок отражает таксономию Fandom и не должна приниматься за фактическую продуктовую иерархию Hot Wheels.

## Очередь исследования

1. [x] Построчно проверена первая группа Patch Cards и Flying Colors; точные количества и выявленные расхождения записаны в FINDINGS.md.
2. [x] Проверена структура таблиц Boss Hoss, Heavy Chevy и King Kuda; полная хронология релизов остаётся задачей.
3. [x] Уточнена семантика Speed Fleet: Blue Card line и Rainbow Card в составе Mainline; названия секций подтверждены HTML-заголовками.
4. [x] Проведён структурный и выборочный построчный проход по 19 дополнительным страницам Early Collections; наблюдения внесены в FINDINGS.
5. [x] Разобраны Heavyweights (годовые галереи), Real Riders (disambiguation), Grand Prix (вложенные названия в ячейках) и шесть таблиц Ultra Hots 1984–1986/pack listings.\n6. [x] Дополнительно проверены The Heavies, Super Streeters, Sugar Caddy, Nitty Gritty Kitty и TNT-Bird.\n7. [ ] Продолжить ранний блок, затем перейти к Modern Special Series, Notable Modern Themed Assortments и Other Modern Series.
7. После исследования раннего блока перейти к Modern Special Series, Notable Modern Themed Assortments и Other Modern Series.

## История обновлений

- 2026-11-08: создана исследовательская документация; добавлены предварительные наблюдения и требования к модели данных.

- 2026-11-08: выполнена построчная сверка Flying Colors, семи Patch Cards, Boss Hoss, Heavy Chevy, King Kuda и Speed Fleet; исправлены две ошибки интерпретации Collector # как Toy #.
8. [x] Проверены Farbs, Zowees, Truck Co., шесть моделей Fat Daddy Sizzlers и аксессуар Steering Trailer; зафиксированы бренд-границы, regional aliases, комплекты и source typo.
9. [ ] Продолжить проверку оставшихся Early Special Series и затем Other Early Series.


- 2026-11-08: добавлены наблюдения по 14 страницам Early Special Series; зафиксированы поколения механизмов, наборы/компоненты, regional aliases, tooling lineage и нерешённые вопросы.

- 2026-11-08: завершён первичный структурный проход по пяти страницам Other Early Series (Action Cycles, Action Racers, Attack Pack, Hot Wheels Railroad, Key Force); добавлены требования по multi-type families, трансформации и железнодорожным системам.

- 2026-11-08: начат Modern Special Series; изучены 100%, AcceleRacers (2005/2006/2025), Boulevard (2012/2020), Car Culture (2016/2026 и Team Transport 2026), Character Cars (Star Wars/Marvel/Disney), Color Shifters/Color Reveal, Pop Culture, Replica Entertainment и Fast & Furious Premium.

- 2026-11-08: Modern Special Series batch 2: исследованы Pro Racing 1997/2005 и Basic Pro Racing, Hot Wheels Delivery, Garage 2010/2016, Hot Wheels id, Nostalgic Brands и Flying Customs 2020–2022; добавлены вопросы по лицензиям, промо и digital ecosystem.


- 2026-11-08: Hot Wheels Classics (2005–2009) повторно исследована по обновлённому HTML; разобраны пять серийных таблиц (621 data rows), track sets, варианты Toy #/Series #, button/Spectraflame, Walgreens/Comic-Con/RLC exclusives и Chase. Результаты добавлены в FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследованы Flying Customs 2006–2007 и 2013: 24 записи в двух годовых таблицах раннего Target-exclusive выпуска и 27 записей 2013 года в шести Mix; зафиксированы Toy #/casting variants, страны производства, base codes, wheel types и tooling/chassis notes. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследована страница Hot Wheels Cool Classics (2013–2014): две таблицы по 30 позиций, Toy # Y9424–Y9453 и BDR-series, Spectrafrost colors, Retro Slot Wheels/metal base и два варианта card artwork для каждого года. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.


- 2026-11-08: исследована страница Crashers (2007), Fandom revision 756909: 32 строки основной таблицы, spring-activated plastic body/base crash mechanism с тремя направлениями откидывания; Bonus Vehicle 2-Packs N1722–N1727, Crashers 3-Pack N9337 и Crossroad Crash playset. Также разобраны смежные Mega Wrecks (2008; 3 позиции, lights & sounds) и Bumper Busters (4 позиции, multi-stage crash damage). Зафиксированы аномалии Toy #, неоднозначные wheel codes и требования к моделированию механики/комплектов. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследована страница Dragstrip Demons (2009–2010), Fandom revision 807648: заявленные 55 выпусков, 18 castings/13 новых, отменённая позиция 18/30, двойной wheel variant для N8964, повтор позиции 12/25 в 2010 и спорная историческая атрибуция Wedge Dragster. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследована страница Vintage Racing (2011), Fandom revision 797035: 30 позиций, Thailand manufacturing claim, множественные Base codes и ошибка печати #22 на карточках позиции 15/30 (T8455). Зафиксирована явная связь замены с Dragstrip Demons. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследованы Dragstrip Demons как сегмент Car Culture 2018 (Fandom revision 760101; пять релизов FVN69–FVN73) и Vintage Racing Club 2024 (revision 703020; два mix, 11 релизов HRV00–HRV10). Зафиксированы wheel configurations, base codes, mix-local numbering и различия с Dragstrip Demons 2009–2010/Vintage Racing 2011. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследованы Formula One Collection 2025 (Fandom revision 780455) и 2026 (revision 816712): 16 индивидуальных driver-specific релизов в 2025 и 20 в 2026; дополнительно 10 командных продуктов, отдельный продукт JRB39 и Formula One Podium Set JRB40 в 2026. Зафиксированы Driver, racing number, team naming, chassis labels, RRPPZ wheels и stand codes. Выделены отдельные сущности пилота, сезонного участия, команды, реального гоночного автомобиля, Hot Wheels release и multipack/set. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследованы Pro Racing 1997–2005 и Basic Pro Racing Series (Fandom revisions 783371, 764854, 801821, 809610, 792684, 765107, 783974, 773614, 801554, 815908). Зафиксированы разнородные таблицы NASCAR/Indy-CART/F1, промо-продукты, wheel codes, Toy #/Item Number, unreleased entries, casting/release variants и явные driver attributions в Pro Racing Luxury Rides 2003. Добавлены требования отделять racing entry, driver, team, sponsor, racing number, casting и release; не выводить пилота из номера/спонсора без источника. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.

- 2026-11-08: исследованы Hot Wheels Racing Selects (Fandom revision 763674) и Pro Racing Team Transporter (revision 783311). Racing Selects содержит две таблицы с явными полями Racing Number, Casting, Color, Team Sponsor, Driver и Notes, включая continuation rows, разные castings под одинаковым номером и исправление ошибочной атрибуции #32 Tide (Ricky Craven vs Scott Pruett). Team Transporter содержит 137 записей за 1998–2006, три truck castings (International Eagle 9400, Kenworth T2000, Freightliner Columbia), ссылки на комплектные гоночные машины и вариации/аномалии. Зафиксированы требования моделировать hauler и car как отдельные продукты и set components; не сливать автоматически с Car Culture Team Transport (2018+). Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.


- 2026-11-08: исследованы все девять страниц Car Culture: Team Transport за 2018–2026 годы (Fandom revisions 740997, 780158, 764386, 789564, 816153, 753242, 804894, 768859, 815941). Прослежена непрерывная нумерация #1–#97, ежегодные Mix, отдельные N/A exclusives, развитие парных комплектов до наборов с несколькими компонентами (hauler/trailer/car), расширение castings и компонентные wheel/base-code/novelty notes. Сопоставлено с Pro Racing Team Transporter 1998–2006: общая логика bundle, но нет основания сливать Series identity. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.


- 2026-11-08: проведён структурный и выборочный построчный проход по Car Culture 2016–2026, а также отдельным страницам Car Culture 2-Packs (revision 816371) и Car Culture Factory Set (revision 766209). Годовые страницы содержат 4–8 тематических сегментов; Series # 1/5–5/5 локален сегменту; с 2022 в обычных сегментах видны Chase 0/5, тогда как RLC 6th Car Set 2017 имеет 0/5 без Chase label. Изучены 2-Packs как двухкомпонентные bundle-продукты и Factory Sets 2022–2026 как агрегаты тематических сегментов и Team Transport Mixes. Зафиксированы Container Sets как отдельная/неразрешённая категория, переменные вложенные наборы и требования к scoped identifiers, component relations и provenance. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.


- 2026-11-08: начат межкаталожный проход Car Culture / Mainline / Boulevard / Pop Culture. Сопоставлены Car Culture 2016–2026 и сохранённый список Mainline 2024: обнаружено 49 строковых совпадений casting names (кандидаты, не доказанные identity matches). Выявлены прямые ссылки Identical to / Similar to на Toy # других выпусков в Car Culture 2-Packs и Pop Culture; зафиксирована необходимость хранить typed source assertions, target identifier и namespace. Обновлены FINDINGS, UNRESOLVED и DATA_MODEL_REQUIREMENTS.
- 2026-11-08: уточнён протокол расширения межкаталожной сверки после anchor sample Mainline 2024. Зафиксировано, что 49 совпадений Car Culture ↔ Mainline 2024 являются row-level name-match candidates, а не числом подтверждённых кастингов. Добавлены требования к отдельным comparison runs, хранению исходных строк и namespace для Toy #, градациям доказательств и различению casting family/casting. В UNRESOLVED добавлены вопросы по покрытию Mainline других лет, adjudication Mazda RX-3 family и расширению Boulevard/Pop Culture.


- 2026-11-08: начат source-discovery этап для межкаталожной сверки Mainline 2025. Найдены публичные Fandom-страницы Mainline 2025, Car Culture 2025, Boulevard 2025 и Team Transport 2025; локальный Mainline 2025 HTML не обнаружен поиском по коду репозитория. Полные страницы и revision IDs ещё не зафиксированы, поэтому match count не рассчитывался. Подробности и ограничения добавлены в FINDINGS.md; acquisition/adjudication tasks добавлены в UNRESOLVED.md.


- 2026-11-08: исправлена ошибка source discovery для Mainline 2025. Пользователь указал полный архив `JohnyKiska/hotwheels`, branch `archive/historical-html-1968-2026`, каталог `ALLHW/`. Проверены каталог `ALLHW/2025` и `ALLHW/MANIFEST.csv`: Mainline 2025 HTML найден (824,886 bytes); записаны Git blob SHA и manifest SHA-256. В ALLHW присутствуют годовые папки 1968–2026; в MANIFEST отдельно представлены две страницы за 2010 год. Mainline 2025 теперь source-available; остаются извлечение таблиц, контроль полноты и Premium comparisons. Подробности в FINDINGS.md и задачи в UNRESOLVED.md.

- 2026-11-08: завершён первый structured exact-name pass Mainline 2025 ↔ Car Culture/Boulevard/Team Transport 2025. Mainline: 440 строк / 250 Collector #; CC: 48 строк / 2 кандидата; Boulevard: 25 / 2; Team Transport: 29 компонентов / 3 distinct component-name candidates. Исходные revision IDs/blob SHA, extraction QA и кандидаты записаны в research/comparisons/MAINLINE-PREMIUM-2025.md. Это name matches, не подтверждённая casting/tooling identity.


## Архивный аудит

- [ARCHIVE_PROCESSING_AUDIT.md](ARCHIVE_PROCESSING_AUDIT.md) — инвентаризация Mainline 1968–2026 и статус обработки годовых страниц.


- 2026-11-08: выполнен аудит Mainline archive tree: 59 годовых папок (1968–2026), 60 HTML-страниц с отдельными обычной и International страницами за 2010 год; 2025 имеет полную extraction QA, 2024 использован как частичный anchor, остальные годовые страницы требуют систематического извлечения/QA. Отчёт: ARCHIVE_PROCESSING_AUDIT.md.


- 2026-11-08: повторно извлечена и QA-проверена полная таблица Mainline 2024 из канонического архива: 441 строка, 441 уникальный Toy #, 250 Collector #, 132 пометки (2nd Color), 15 TH и 15 STH. CSV и отчёт: research/extractions/MAINLINE-2024.csv и MAINLINE-2024-EXTRACTION-QA.md. 49 прежних Car Culture name-match candidates остаются не adjudicated.


- 2026-11-08: независимо извлечены Mainline 2010 USA и International (Fandom revisions 815649/815650): USA 440 source rows в 28 таблицах, International 228 строк в 24 таблицах. Сохранены два CSV с table/section provenance; выявлены 213 общих Toy #, 39 USA-only, 13 International-only и 21 расхождение Model Name среди общих Toy # при сравнении первого появления. Отчёт: research/comparisons/MAINLINE-2010-USA-INTERNATIONAL.md. Эти совпадения/расхождения требуют adjudication.


- 2026-11-08: извлечена и QA-проверена Mainline 2026: 440 строк, 440 уникальных Toy #, 250 Collector #, 137 пометок (2nd Color), 15 TH и 15 STH; 126 сырых Series labels. Сохранены CSV и отчёт: research/extractions/MAINLINE-2026.csv и MAINLINE-2026-EXTRACTION-QA.md. Fandom revision 816337.


- 2026-11-08: извлечена и QA-проверена Mainline 2023: 445 строк, 445 уникальных Toy #, 250 Collector #, 141 пометка (2nd Color), 15 TH и 15 STH; 1 таблица. CSV и отчёт: research/extractions/MAINLINE-2023.csv и MAINLINE-2023-EXTRACTION-QA.md. Fandom revision 772739.


- 2026-11-08: извлечена и QA-проверена Mainline 2022: 447 строк, 447 уникальных Toy #, 250 Collector #, 142 пометки (2nd Color), 15 TH и 15 STH; 1 таблица. CSV и отчёт: research/extractions/MAINLINE-2022.csv и MAINLINE-2022-EXTRACTION-QA.md. Fandom revision 797387.


- 2026-11-08: извлечена Mainline 2021: основная таблица 447 строк (447 уникальных Toy #, Collector # 001–250), отдельно Hot Wheels id: Chase Series 8 строк с Collector # = No #. Всего 455 source rows в двух таблицах; сохранён table/section provenance. CSV и QA: research/extractions/MAINLINE-2021.csv и MAINLINE-2021-EXTRACTION-QA.md. Fandom revision 797153.


- 2026-11-08: извлечена Mainline 2020: основная таблица 447 строк (447 уникальных Toy #, Collector # 001–250), отдельно Hot Wheels id Chase Series 8 строк с Collector # = No #. Два Photo cell содержат имена broken-media placeholders (GHD85 и GHF27), сохранены в CSV. CSV и QA: research/extractions/MAINLINE-2020.csv и MAINLINE-2020-EXTRACTION-QA.md. Fandom revision 812218.


- 2026-11-08: извлечена Mainline 2019: основная таблица 447 строк (447 уникальных Toy #, Collector # 001–250), отдельно Unnumbered Special Editions 2 строки (GFJ71, GJN99; Collector # = No #). Всего 449 source rows в двух таблицах. CSV и QA: research/extractions/MAINLINE-2019.csv и MAINLINE-2019-EXTRACTION-QA.md. Fandom revision 812200.


- 2026-11-08: извлечена Mainline 2018: основная таблица #1–365 содержит 365 строк; отдельно извлечены 104 строки из 10 секций (TH, STH, Super Ultimate Chase, Red Editions, Zamac, retailer exclusives, Daredevil Chase). Все дополнительные строки имеют Collector # = No #. Зафиксированы 6 Series # с zero-width Unicode. CSV и QA: research/extractions/MAINLINE-2018.csv и MAINLINE-2018-EXTRACTION-QA.md. Fandom revision 811760.


- 2026-11-08: извлечена Mainline 2017: основная таблица #1–365 (365 строк), дополнительно 85 строк в 9 отдельных секциях, включая TH/STH, Red Editions, retailer exclusives и Digital Circuit Chase Variants. TH/STH задаются заголовками таблиц, а не Series text. CSV и QA: research/extractions/MAINLINE-2017.csv и MAINLINE-2017-EXTRACTION-QA.md. Fandom revision 781777.


- 2026-11-08: извлечена Mainline 2016: 433 строки в 31 series-specific таблице (250 Collector # positions), отдельно 8 Special Edition rows в двух таблицах. 397 Series # cells содержат zero-width Unicode, сохранённый в CSV. TH/STH указаны в Series text. CSV и QA: research/extractions/MAINLINE-2016.csv и MAINLINE-2016-EXTRACTION-QA.md. Fandom revision 724947.


- 2026-11-08: извлечена Mainline 2015: 433 строки в 34 series tables (250 numeric Collector #); отдельно Scavenger Hunt 4 строки с Collector # = No # и шестой колонкой Series #. В Mainline tables только 5 полей (Toy #, Col.#, Model Name, Series, Photo), Series # отсутствует как колонка. CSV экспорт исправлен с header-based mapping и исключением navigation table. QA: research/extractions/MAINLINE-2015-EXTRACTION-QA.md. Fandom revision 790646.


- 2026-11-08: извлечена Mainline 2014: 433 строки в 32 series-specific tables (250 Collector # positions), отдельно 4 Scavenger Hunt (Kroger Exclusive) rows с Collector # = No #. Одна Mainline таблица (Batman 75th Anniversary) имеет 5 колонок без Series #; 153 Series # cells содержат zero-width Unicode. CSV и QA: research/extractions/MAINLINE-2014.csv и MAINLINE-2014-EXTRACTION-QA.md. Fandom revision 804340.


- 2026-11-08: извлечена Mainline 2013: 433 строки в 30 series tables (250 numeric Collector #), отдельно 6 Kroger-exclusive Scavenger Hunt rows с Collector # = No # и Series # 1/6–6/6. Mainline tables имеют 5 колонок без Series #. CSV и QA: research/extractions/MAINLINE-2013.csv и MAINLINE-2013-EXTRACTION-QA.md. Fandom revision 790643.


- 2026-11-08: извлечена Mainline 2012: 387 строк в 23 основных таблицах, Collector # 001–247 без пропусков (не до 250); отдельно Windshield Banner Exclusives + Redline Exclusives 20 cross-listed rows и Year of the Dragon Edition 1 row с No #. 16 из 20 эксклюзивных строк exact repeats, 4 имеют текстовые расхождения при том же Toy #. Сохранены CSV и QA: research/extractions/MAINLINE-2012.csv и MAINLINE-2012-EXTRACTION-QA.md. Fandom revision 778347.


- 2026-11-08: извлечена Mainline 2011: 429 строк в 21 основных таблицах, Collector # 001–244 без пропусков; две дополнительные секции Windshield Banner Exclusives и Redline Exclusives содержат 20 exact row repeats, а не новые уникальные Toy #. 15 TH и 15 STH находятся в Series labels. CSV и QA: research/extractions/MAINLINE-2011.csv и MAINLINE-2011-EXTRACTION-QA.md. Fandom revision 806210.


- 2026-11-08: извлечена Mainline 2009: 342 строки в 14 основных таблицах, Collector # 001–190 без пропусков; Toy # повторяется между color entries (202 unique Toy #, 104 IDs repeated within Mainline rows). Дополнительно Redline Exclusives 10 и Goodyear Tire Exclusives 2 rows, все 12 exact repeats Mainline rows. 12 TH и 12 STH. CSV и QA: research/extractions/MAINLINE-2009.csv и MAINLINE-2009-EXTRACTION-QA.md. Fandom revision 811763.


- 2026-11-08: извлечена Mainline 2008: 358 строк в 18 таблицах, Collector # 001–196 без пропусков, 208 уникальных Toy # (часть повторяется между color entries), 91 пометка (2nd Color), 12 TH и 12 STH. CSV и QA: research/extractions/MAINLINE-2008.csv и MAINLINE-2008-EXTRACTION-QA.md. Fandom revision 803369.


- 2026-11-08: извлечена Mainline 2007: 315 строк в 18 таблицах, Collector # 001–180 без пропусков, 193 уникальных Toy # (повторяются между цветами), 80 пометок (2nd Color), 12 TH и 13 STH (включая отдельную Toys R Us Promo). Все 315 Series # содержат zero-width Unicode; сохранены raw. CSV и QA: research/extractions/MAINLINE-2007.csv и MAINLINE-2007-EXTRACTION-QA.md. Fandom revision 804327.


- 2026-11-08: извлечена Mainline 2006: 363 строки в 17 таблицах, Collector # 001–223 без пропусков, 223 уникальных Toy #; Open Stock отдельно 141 строка в пятиколоночной схеме без Series #. Зафиксированы 74 (2nd Color), 12 TH, 90 повторяющихся Toy # values. CSV и QA: research/extractions/MAINLINE-2006.csv и MAINLINE-2006-EXTRACTION-QA.md. Fandom revision 811755.


- 2026-11-08: извлечена Mainline 2005: 288 строк в 19 таблицах, Collector # 001–187 без пропусков; Open Stock 86 строк в отдельной пятиколоночной схеме без Series #. 40 пометок (2nd Color), 13 Treasure Hunt (включая Mail-In), 77 повторяющихся Toy # values, 135 Series # cells с zero-width Unicode. CSV и QA: research/extractions/MAINLINE-2005.csv и MAINLINE-2005-EXTRACTION-QA.md. Fandom revision 797737.


- 2026-11-08: извлечена Mainline 2004: 268 строк в 16 таблицах, numeric Collector # 001–212 без пропусков плюс отдельный Collector #000 для First Editions Mail-In. Таблицы 13–16 используют пятиколоночную схему без Series #; 101 Series # values содержат zero-width Unicode. Зафиксированы 48 (2nd Color) и 12 T-Hunt. CSV и QA: research/extractions/MAINLINE-2004.csv и MAINLINE-2004-EXTRACTION-QA.md. Fandom revision 811756.


- 2026-11-08: извлечена Mainline 2003: 222 строки в 22 таблицах, Collector # 001–220 без пропусков; таблица 2003 Hot Wheels (32 строки) использует 5-column schema без Series #. Collector #035 / Toy #56391 имеет три цветовых варианта; один Series # blank (Sonic Special #207), один literal Unnumbered (Roll Patrol). CSV и QA: research/extractions/MAINLINE-2003.csv и MAINLINE-2003-EXTRACTION-QA.md. Fandom revision 797937.


- 2026-11-08: извлечена Mainline 2002: 240 строк в 18 таблицах, Collector # 001–240; отдельно Final Run 3 rows (Series # 1/12, 4/12, 6/12), не включать в Mainline namespace. Таблица 2002 Hot Wheels (126 rows) использует 5-column schema без Series #. CSV и QA: research/extractions/MAINLINE-2002.csv и MAINLINE-2002-EXTRACTION-QA.md. Fandom revision 777856.


- 2026-11-08: извлечена Mainline 2001: 240 rows, Collector # 001–240 без пропусков; отдельно Final Run 12 rows (собственный namespace 001–012) и Store Exclusives 4 rows с Toy #/Collector #/Series # blank в source. Таблица 2001 Hot Wheels имеет 5 колонок без Series #. CSV и QA: research/extractions/MAINLINE-2001.csv и MAINLINE-2001-EXTRACTION-QA.md. Fandom revision 806211.


- 2026-11-08: извлечена Mainline 2000: 249 строк в 17 таблицах; 245 distinct nonblank Toy #. Выявлены три source scopes: core annual tables, Virtual Collection (35 rows, alphanumeric Series # codes) и Bonus Cars (4 rows with blank Toy # and Collector # 001–004 in separate scope). Пять numeric Collector # values absent: 147, 170, 184, 185, 186. 2000 Hot Wheels uses 5-column schema. CSV и QA: research/extractions/MAINLINE-2000.csv и MAINLINE-2000-EXTRACTION-QA.md. Fandom revision 799670.


- 2026-11-08: извлечена Mainline 1999: 196 numbered-list rows с Collector #649–1121 (non-dense), отдельно Final Run 12 rows (Collector # blank) и Bonus Cars 4 rows (Toy # blank, Collector #001–004 in bonus scope). 1999 Hot Wheels table has 5-column schema without Series #. 277 numeric values in range 649–1121 are not represented on this page; do not infer missing releases. CSV и QA: research/extractions/MAINLINE-1999.csv и MAINLINE-1999-EXTRACTION-QA.md. Fandom revision 799669.


- 2026-11-08: извлечена Mainline 1998: 185 numbered-list rows, 184 unique Collector # values (633–908, non-dense); #780/Toy #19949 repeated twice. Отдельно Bonus Cars 4 rows (Toy # blank for two entries, Collector #001–004 in bonus scope). 1998 Hot Wheels table has 5-column schema; four tables declare optional Photo 2; some rows omit trailing empty cell. Preserved header typo "Serie s". CSV и QA: research/extractions/MAINLINE-1998.csv и MAINLINE-1998-EXTRACTION-QA.md. Fandom revision 811155.


- 2026-11-08: извлечена Mainline 1997: 119 numbered-list rows (numeric Collector #147–642, non-dense), отдельно Bonus Cars 4 rows (#001–004) и 7 other series tables (28 rows, Collector # = N/A). Обнаружен конфликт Toy #18365: Pontiac Salsa в 1997 Hot Wheels vs Auburn 852 в Classics Series; Toy #11850 повторяется в двух numbered tables, Toy #15789 пересекает Mainline/Street Racers. CSV и QA: research/extractions/MAINLINE-1997.csv и MAINLINE-1997-EXTRACTION-QA.md. Fandom revision 799665.


- 2026-11-08: извлечена Mainline 1996: 141 строка в 17 таблицах; 136 уникальных Toy # и Collector # values; 12 Treasure Hunts, 4 Bonus Cars, 64 строки в 1996 Hot Wheels без Series #. Выявлены две точные повторные строки (#473 BMW M1 и #491 Rocket Shot) и три межсекционных Toy # collisions между Bonus Cars и Treasure Hunts. CSV/QA: research/extractions/MAINLINE-1996.csv и MAINLINE-1996-EXTRACTION-QA.md. Fandom revision 800722.


- 2026-11-08: извлечена Mainline 1995: 97 строк в 15 таблицах, 97 уникальных Toy # и Collector #, 12 Treasure Hunts. Таблица 1995 Hot Wheels имеет отдельные поля Color и Rims (7 колонок). В 72 Series # сохранены zero-width Unicode. CSV/QA: research/extractions/MAINLINE-1995.csv и MAINLINE-1995-EXTRACTION-QA.md. Fandom revision 797722.


- 2026-11-08: извлечена Mainline 1994: 14 строк в двух 12-колоночных таблицах (New Models 5, Reissues 9). Сохранены Color, Tampo, Base Color / Type, Window Color, Interior Color, Wheel Type, Toy # и Notes. Выявлены BMW 850i с двумя Wheel Type, пустой Toy # у Sol-Aire CX-4, INTL identifier у Road Roller и подозрительное смещение полей Tough Customer. CSV/QA: research/extractions/MAINLINE-1994.csv и MAINLINE-1994-EXTRACTION-QA.md. Fandom revision 783555.


- 2026-11-08: извлечена Mainline 1993: 72 строки в пяти таблицах с разными схемами. 64 уникальных Toy #; 36 уникальных nonblank Col # в New Castings/Reissues. Отмечены повторяющиеся Col #149/197/224, Toy #2781/3502/4314/5667, три пустых Col # и четыре пустых Toy # в Tattoo Machines. Demolition Man использует # in Series, 25th Anniversary Series отдельный набор полей. CSV/QA: research/extractions/MAINLINE-1993.csv и MAINLINE-1993-EXTRACTION-QA.md. Fandom revision 797943.


- 2026-11-08: извлечена Mainline 1992: 24 строки в трёх таблицах (New Castings 12, Reissues 7, Gleam Team 5). Две схемы: 12 и 9 колонок. Уникальные Col # 24; Toy # 22; у Gleam Team #189/#190 Toy # отсутствует. CSV/QA: research/extractions/MAINLINE-1992.csv и MAINLINE-1992-EXTRACTION-QA.md. Fandom revision 783535.


- 2026-11-08: извлечена Mainline 1991: 62 строки в New Castings (27), Reissues (24) и California Customs (11). 39 уникальных nonblank Col #, 46 уникальных Toy #; 10 пустых Col # и 9 пустых Toy #. Повторяются Col #129/148 и Toy #1470/1897/2097/3209/7607/9749. California Customs имеет отдельную схему без Col #. CSV/QA: research/extractions/MAINLINE-1991.csv и MAINLINE-1991-EXTRACTION-QA.md. Fandom revision 797729.


- 2026-11-08: извлечена Mainline 1990: 87 строк в четырёх таблицах (New Castings 8, Reissues 50, The Simpsons 2, California Customs 27). Только New Castings имеет Col #; Toy # отсутствует у восьми Reissues rows; 11 повторяющихся Toy # groups. CSV/QA: research/extractions/MAINLINE-1990.csv и MAINLINE-1990-EXTRACTION-QA.md. Fandom revision 754020.


- 2026-11-08: извлечена Mainline 1989: одна таблица, 76 строк, Col. #001–076 без пропусков, Series #1/76–76/76; Toy # в источнике отсутствует. CSV/QA: research/extractions/MAINLINE-1989.csv и MAINLINE-1989-EXTRACTION-QA.md. Fandom revision 754017.
