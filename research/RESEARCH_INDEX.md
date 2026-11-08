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
