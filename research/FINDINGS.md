# Research Findings

Здесь фиксируются результаты чтения сохранённых источников. Статус явно указан у каждого пункта.

## Архив и таксономия

- **Observation | 2026-11-08.** Архив содержит 532 файла: 530 HTML/HTM и 2 CSV. Источник: инвентаризация репозитория.
- **Observation.** Папки архива повторяют категории Fandom (например, Early Collections, Early Special Series, Modern Special Series). Это структура источника, а не доказательство реальной иерархии продуктов.
- **Observation.** Отдельные страницы могут содержать несколько таблиц и разные типы сущностей: автомобили, аксессуары, игровые наборы, компоненты и невыпущенные продукты. Отсутствие HTML-таблицы не означает отсутствие полезных данных.

## Ранние коллекции и тематические группы

- **Observation.** Patch Cards (1978–1979) описывают тематические группы, среди которых Classy Customs, Drag Strippers, Oldies But Goodies, Rescue Team, Speedway Specials, Super Streeters и The Heavies. Принадлежность модели к тематической группе не обязательно исключает её появление в других выпусках или коллекциях.
- **Observation.** Flying Colors (1974–1978) содержит несколько таблиц; одна из таблиц включает поля Casting, Body Color, Tampos, Wheel Type и Versions.
- **Observation.** Speed Fleet представлен как минимум двумя отдельными таблицами: Blue Card и Rainbow Card. Их нельзя автоматически объединять без сохранения контекста таблицы и упаковки.
- **Observation.** В Trailbusters встречаются повторяющиеся сочетания года и Toy Number при различиях колёс, цветов или конструктивных особенностей.
- **Observation.** Страница Sizzlers включает не только автомобили, но и зарядные устройства, треки, аксессуары и игровые наборы.

## Предварительные межстраничные наблюдения

Следующие пункты перенесены из первичного исследовательского прохода и **требуют повторной построчной проверки по исходным HTML**. Не использовать их как окончательные идентификационные соответствия.

- **Preliminary observation.** В таблицах Patch Cards и Flying Colors обнаружены совпадения названий моделей и Toy Number, а также случаи различающихся номеров для одинаково названных моделей. Примеры, требующие проверки: Prowler, Monte Carlo Stocker, Formula 5000, Paddy Wagon и Mustang Stocker.
- **Preliminary observation.** На страницах Boss Hoss, Heavy Chevy и King Kuda смешаны записи разных периодов и типов выпусков, включая ранние выпуски и поздние коллекционные релизы.
- **Preliminary observation.** Speed Fleet содержит повторяющиеся номера при разных годах или вариантах; пример для проверки — Sol-Aire CX4, которому приписываются номера 5902 и 1494 в разные годы.

## Принцип интерпретации

Совпадение названия или Toy Number само по себе не доказывает тождество конкретного выпуска. Для сопоставления учитывать casting, год, рынок, серию/ассортимент, цвет, тампо, колёса, конструкцию, упаковку и источник записи.


## Построчная проверка ранних коллекций (2026-11-08)

Проверены сохранённые HTML-таблицы в следующих файлах:
- `Early Collections/Flying_Colors.htm`
- `Early Collections/Classy Customs _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Drag Strippers _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Oldies But Goodies _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Rescue Team _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Speedway Specials _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Super Streeters _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/The Heavies _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Boss Hoss _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Heavy Chevy _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/King Kuda _ Hot Wheels Wiki _ Fandom.html`
- `Early Collections/Speed Fleet _ Hot Wheels Wiki _ Fandom.html`

**Проверенные количества строк данных** (строка заголовка исключена):
- Flying Colors: 5 таблиц, соответственно 44, 42, 33, 77 и 16 строк данных (212 строк суммарно). Заголовки таблиц не полностью одинаковы.
- Patch Cards: Classy Customs — 12; Drag Strippers — 17; Oldies But Goodies — 8; Rescue Team — 6; Speedway Specials — 17; Super Streeters — 13; The Heavies — 7.
- Boss Hoss: 2 таблицы, 23 и 10 строк данных.
- Heavy Chevy: 4 таблицы, 19, 1, 16 и 8 строк данных.
- King Kuda: 4 таблицы, 9, 1, 23 и 11 строк данных.
- Speed Fleet: 2 таблицы, 40 и 36 строк данных. Годы в первой таблице охватывают 1987–1990, во второй — 1986–1989. Не назначать этим таблицам ярлыки Blue Card/Rainbow Card только по порядку: это нужно связать с заголовками/контекстом страницы и упаковкой.

**Сверка Patch Cards ↔ Flying Colors по точному тексту названия и Toy Number:**
- Prowler: Patch Cards Toy #9207; Flying Colors Toy #6965. Это реальное расхождение полей Toy # в двух страницах, не ошибка сравнения с Collector #.
- Paddy Wagon: Classy Customs Toy #6966; Flying Colors содержит записи Toy #6966 и #7966 в разных таблицах/контекстах. Требуется привязка к году/варианту/таблице, нельзя выбрать один номер как единственный.
- Mustang Stocker: Super Streeters Toy #9203; Flying Colors Toy #7644. Реальное расхождение Toy #.
- Monte Carlo Stocker: Speedway Specials Toy #7660 и Collector #21; Flying Colors Toy #7660. Ранее упомянутый №21 — Collector #, а не Toy #. Противоречия Toy Number здесь не подтверждается.
- Formula 5000: Speedway Specials Toy #9119 и Collector #53; Flying Colors Toy #9119. Ранее упомянутый №53 — Collector #, а не Toy #. Противоречия Toy Number не подтверждается.
- Примеры одинаковых названий и совпадающего Toy #: Buzz Off #6976, Red Baron #6964, Army Funny Car #2023, Rodger Dodger #8259, '57 T-Bird #2013, Chief's Special #7665, Corvette Stingray #9241, '56 Hi-Tail Hauler #9647. Это совпадение названия и номера, но не доказательство идентичности каждой записи: цвет, тампо, год и колёса могут различаться.

**Другие наблюдения по таблицам:**
- Boss Hoss, Heavy Chevy и King Kuda имеют несколько таблиц с разными структурами колонок. Внутри каждой страницы соседствуют ранние записи 1970-х и поздние коллекционные релизы. Страницы описывают историю кастинга/выпусков, а не одну серию.
- Speed Fleet: повторения Toy # и названий необходимо рассматривать в контексте года, цвета, wheel type и заметок. Две таблицы содержат 76 строк данных суммарно; точная семантика границ таблиц требует дополнительной фиксации по тексту страницы.

**Ограничение проверки:** это прямой разбор сохранённых HTML и сверка исходных ячеек, а не независимая проверка исторической достоверности Fandom. Количество строк означает число строк данных в HTML-таблицах, а не число уникальных кастингов или релизов.


## Дополнительная проверка Early Collections (2026-11-08)

Проверены исходные таблицы следующих страниц: Action Command, Classics, Evil Weevil, Extras, Grand Prix, Heavyweights, HiRakers, Megaforce, Nitty Gritty Kitty, Real Riders, Speed Demons, Speed Machines (1983), Sugar Caddy, Super Chromes (1976), TNT-Bird, The Hot Ones (1981), Trailbusters, Ultra Hots Series (1984), Workhorses.

### Структура таблиц и количество строк

Количество строк данных (без заголовка):
- Action Command: 2 таблицы — 8 и 30.
- Classics: 1 — 25.
- Evil Weevil: 2 — 8 и 5.
- Extras: 1 — 9.
- Grand Prix: 1 — 7 строк HTML с 11 названиями/датировками внутри ячеек; структура не является обычной построчной таблицей.
- Heavyweights: HTML-таблиц не обнаружено.
- HiRakers: 1 — 16.
- Megaforce: 1 — 7.
- Nitty Gritty Kitty: 3 — 5, 4 и 9.
- Real Riders: HTML-таблиц не обнаружено.
- Speed Demons: 2 — 6 и 16.
- Speed Machines (1983): 1 — 27.
- Sugar Caddy: 3 — 12, 3 и 1.
- Super Chromes (1976): 3 — 25, 19 и 2.
- TNT-Bird: 2 — 11 и 3.
- The Hot Ones (1981): 4 — 90, 3, 4 и 1; последняя таблица — навигационный список, не релизы.
- Trailbusters: 1 — 49.
- Ultra Hots Series (1984): 6 — 6, 7, 2, 3, 4 и 4; поздние таблицы имеют неполный набор колонок.
- Workhorses: 2 — 37 и 49.

### Наблюдения, важные для нормализации

- **Observation.** HiRakers содержит повторения одного Toy # в разные годы и с изменениями деталей. Например, 40's Woodie #1131 указан в 1980, 1981, 1982 и 1983 годах; в заметках различаются гладкие и текстурированные панели, цвет и рынок. Следовательно, одного Toy # недостаточно для идентификации варианта.
- **Observation.** Trailbusters подтверждает повторные записи одного Toy #/кастинга при разных годах, колёсах и конструктивных признаках. Baja Breaker #4360: 1987 с открывающимся капотом и BW/Gray Hub RR; 1989 с закрытым капотом и BW/CT. Это не следует сводить к одной строке по Toy #.
- **Observation.** Speed Demons имеет таблицу с шестью базовыми моделями и отдельную таблицу выпусков/вариантов. Eevil Weevil #2062 появляется в 1987 с UH-колёсами, в 1988 с BW и в 1989 в другом цвете/тампо; Fangster #2059 также меняет Wheel Type между 1987 и 1988. Поля серии и физического варианта необходимо разделять.
- **Observation.** Action Command содержит две таблицы с разными периодами/ассортиментами. Одинаковые Toy # повторяются с другими цветами и годами: Assault Crawler #3338 — Olive (1987) и Tan (1988); Big Bertha #9372 — Olive (1987) и Tan (1988); Combat Medic #2519 — Olive (1987) и Tan (1988). Это подтверждает важность года, цвета и декора как атрибутов выпуска.
- **Observation.** Super Chromes (1976) содержит несколько таблиц с разными типами колёс/вариантов, но названия и Toy # повторяются между таблицами. Например, Mustang Stocker #9203 и Prowler #9207. Сама страница связывает кастинги с хромированными вариантами; название группы не заменяет идентичность выпуска.
- **Observation.** Ultra Hots Series (1984) содержит шесть таблиц, не все с Toy # и страной. Первая таблица включает Sol-Aire CX-4 #5902, поздние таблицы повторяют названия с другими цветами/тампо, но без Toy #. Импортёр должен сохранять неполные строки и не выводить Toy # из соседней таблицы.
- **Observation.** Workhorses содержит 86 строк данных в двух таблицах, поля включают Toy #, цвет, тампо, колёса, год, страну и заметки о конструктивных особенностях. Для CAT-линейки заметки фиксируют изменения надписей/панелей, а не только цвет.
- **Observation.** The Hot Ones (1981) имеет одну крупную таблицу на 90 строк и две небольшие таблицы без года/Toy #, плюс навигационную таблицу. Нельзя трактовать каждую таблицу страницы как равноправный список выпусков.
- **Observation.** Grand Prix имеет HTML-таблицу без обычных заголовков. Внутри ячеек содержатся 11 имён с годами: 1968–1970, что отличается от упрощённого подсчёта строк таблицы.
- **Observation.** Heavyweights и Real Riders не имеют HTML-таблиц в сохранённых страницах. Это не означает отсутствия данных: вероятны текстовые/изображенческие списки и описательные разделы.

**Ограничение:** количество строк отражает HTML-разметку архивных страниц, а не число уникальных кастингов или полных релизов. Все выводы выше являются наблюдениями по Fandom HTML, не независимой исторической верификацией.


## Разбор страниц без стандартных таблиц и неоднозначных таблиц (2026-11-08)

### Heavyweights
Источник: `Early Collections/Heavyweights _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница описывает Heavyweights как серию футуристических грузовиков 1970–1971 годов. Указаны три типа кузова с пластиковым задним модулем; при утрате модуля модели, по описанию страницы, становятся трудноразличимыми.
- **Observation.** Список представлен не HTML-таблицей, а галереями по годам. В разделе 1970 показаны Ambulance, Cement Mixer, Dump Truck, Fire Engine, Moving Van и Tow Truck (6 названий). В разделе 1971: Fuel Tanker, S'cool Bus, Scooper, Snorkel, Team Trailer, Waste Wagon и Racer Rig (7 названий).
- **Observation.** В статье присутствует изображение страницы каталога Toys & Hobbies 1972, но сама галерея разделена на 1970 и 1971. Не трактовать год каталога как год выпуска всех изображённых моделей.
- **Design requirement.** Парсер должен извлекать названия из gallery captions и связывать их с ближайшим заголовком года; отсутствие таблицы не должно приводить к пропуску серии.

### Real Riders
Источник: `Early Collections/Real Riders _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Эта страница помечена категорией Disambiguation и фактически различает два значения: Real Rider Wheels (двухкомпонентное колесо с резиновой шиной) и Real Riders Series (название серии автомобилей с такими колёсами).
- **Observation.** Статья связывает концепцию Real Riders с Bob Rosas и Larry Wood и приводит цитату о привлекательности реалистичных резиновых шин для взрослых коллекционеров.
- **Observation.** В статье перечислены продуктовые линейки/периоды, использовавшие Real Rider tires: использование на HWC.com с 2001, отдельная premium series 2005, а также Treasure Hunts, Auto Milestones, Ultra Hots 2006–2007, Classics 5 chase pieces, Garage Premiums, Hot Wheels Delivery, Nostalgic Brands, Pop Culture и Car Culture. Это список применений технологии, а не одна непрерывная серия.
- **Design requirement.** Real Rider wheel/tire должен быть отдельным техническим атрибутом/типом колеса; Real Riders Series и прочие линейки, использующие такие колёса, должны храниться как самостоятельные серии/ассортименты.

### Grand Prix (1969–1970)
Источник: `Early Collections/Grand Prix _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Текст страницы сообщает о дебюте серии в 1969 году: 8 автомобилей в 1969 и добавление Ferrari 312P и Porsche 917 в 1970. Ford J-Car описан как перенесённый из 1968 года в Grand Prix.
- **Observation.** Нестандартная HTML-таблица имеет 8 строк, но в её ячейках находятся 11 названий с годами: Brabham Repco F1 (1969), Chaparral 2G (1969), Indy Eagle (1969), Ferrari 312P (1970), Ford J-Car (1968), Ford Mark IV (1969), Lola GT70 (1969), Lotus Turbine (1969), McLaren M6A (1969), Porsche 917 (1970), Shelby Turbine (1969).
- **Observation.** Таким образом, число HTML-строк не равно числу моделей; год, указанный рядом с моделью, также не обязательно равен году включения в серию (пример Ford J-Car).
- **Observation.** Страница дополнительно отмечает проблему совместимости открытых колёсных машин с Superchargers и неудавшееся предложение добавить боковые обтекатели.
- **Design requirement.** Сохранять исходную структуру ячеек и извлечённые модельные упоминания отдельно; различать debut year модели и series inclusion year.

### Ultra Hots Series (1984–1986)
Источник: `Early Collections/Ultra Hots Series (1984) _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Вводный текст определяет период серии как 1984–1986 и связывает её появление с введением колёс UH. Также явно отделяет revival 2022 года и The Hot Ones 2025 года от серии Larry Wood 2006–2007.
- **Observation.** На странице шесть таблиц с разной семантикой: 1984 (6 строк данных), 1985 (7), 1986 (2), Stamper 3-Pack (3), 4-Pack (4), Gift Pack (4). Первые три таблицы имеют Toy # и Country; таблицы наборов этих полей не имеют.
- **Observation.** Таблицы наборов содержат повторения моделей из годовых таблиц, но это записи о составе конкретных наборов, а не обязательно дополнительные уникальные релизы. В тексте к 3-Pack сказано, что все три модели эксклюзивны для него; для 4-Pack сказано, что модели не являются эксклюзивными.
- **Observation.** Таблица 1984 содержит Flame Runner #7293, Predator #7292, Quick Trik #7295, Sol-Aire CX-4 #5902, Speed Seeker #7299 и Wind Splitter #7296. В 1985 встречаются Jet Sweep X5 #7528, Nightstreaker #9537, Redliner #9534, Silver Bullet #9535, Street Beast #9538, Street Scorcher #9536 и Wind Splitter #9539. В 1986 перечислены Back Burner #2544 и Jet Sweep X5 #2546.
- **Observation.** Таблицы 3-Pack, 4-Pack и Gift Pack повторяют отдельные названия, при этом Toy # отсутствует. Нельзя переносить Toy # из годовой таблицы в записи о наборе без подтверждённой связи конкретного варианта.
- **Design requirement.** Набор/pack должен быть отдельной сущностью с отношением состава к продуктам/вариантам; поле Toy # должно оставаться nullable, а не выводиться из похожего названия.

**Ограничение проверки:** выводы в этом разделе являются наблюдениями по сохранённой HTML-странице Fandom. Они фиксируют структуру и содержание архива, но не являются независимой исторической верификацией.


## Дополнительная проверка ранних коллекций и тематических страниц (2026-11-08)

### Speed Fleet: границы двух таблиц подтверждены
Источник: `Early Collections/Speed Fleet _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Заголовки страницы прямо называют первую таблицу **Speed Fleet Blue Card**, вторую — **Speed Fleet Rainbow Card**. Ранее отмеченная неопределённость о назначении таблиц снята.
- **Observation.** Вводный текст описывает Blue Card как отдельную линейку автомобилей 1987–1990 годов, а Rainbow Card как выпуск в рамках Mainline в 1986–1989 годах с карточкой Speed Fleet.
- **Observation.** Первая таблица содержит 40 строк (включая заголовок), вторая — 36; обе имеют одинаковые поля Toy #, Model Name, Color, Year, Wheel Type, Country, Notes и фото.
- **Design requirement.** Сохранять связь между ассортиментом и упаковкой: Speed Fleet Blue Card и Speed Fleet Rainbow Card не следует автоматически считать одной серией только из-за общего названия. Для Rainbow Card отдельно хранить связь с Mainline.

### Patch Cards: подтверждение по страницам The Heavies и Super Streeters
Источники: `Early Collections/The Heavies _ Hot Wheels Wiki _ Fandom.html`, `Early Collections/Super Streeters _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Обе страницы прямо описывают себя как две из семи тематических групп Patch Cards, выпущенных в 1978–1979 годах; для получения патча требовалось отправить шесть proofs of purchase и 25 центов за пересылку. Обе страницы указывают Hong Kong как страну производства перечисленных моделей.
- **Observation.** Обе страницы отмечают, что некоторые модели также встречались на Flying Colors cards. Это подтверждает, что тематическая группа и карточный ассортимент должны моделироваться как независимые отношения, а не как взаимоисключающие классы.
- **Observation.** The Heavies имеет таблицу с 7 строками данных и отдельными полями Toy # и Collector #. Это ещё один прямой пример необходимости раздельных типов номеров.
- **Observation.** Super Streeters имеет таблицу с 13 строками данных и теми же полями Toy # и Collector #.

### Sugar Caddy: разные поколения tooling и происхождение
Источник: `Early Collections/Sugar Caddy _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает Sugar Caddy как модификацию Custom Eldorado, дебютировавшую в серии The Spoilers в 1971 году. В описании перечислены особенности оригинального продукта: открывающийся капот, наклейка с номером 1–9 на двери, голубое стекло, варианты интерьера, спонсорский decal sheet и металлический либо пластиковый collector button.
- **Observation.** Отдельно описано производство CIPSA в Мексике, а также re-tool в 2009 году для HWC.com Series 8 Neo Classics.
- **Observation.** Таблицы разделяют Original Versions (12 строк данных), CIPSA Versions (3) и Retooled Versions (1). Следовательно, одна страница объединяет исходные варианты, региональное производство и поздний re-tool.
- **Design requirement.** Сохранять производственную площадку/рынок и происхождение tooling на уровне выпуска/кастинга; re-tool должен создавать отдельную связь Modified Casting/Tooling lineage, а не просто новый цветовой вариант.

### Дополнительные замечания
- **Observation.** Nitty Gritty Kitty имеет три таблицы с одинаковым набором подробных полей (год, серия, цвет, тампо, тип/цвет базы, окна, интерьер, колёса, Toy #, страна, заметки). На странице также отдельно выделены 1:64, 100% и retooled версии. Это подтверждает необходимость различать scale/product line и поколения tooling.
- **Observation.** TNT-Bird имеет отдельные таблицы Original Versions и Re-Tooled Versions. Само разделение страницы показывает, что повторное использование названия после re-tool не должно автоматически означать идентичность casting.
- **Observation.** На странице Super Streeters и The Heavies общий текст Patch Cards указывает 1978–1979 и Hong Kong; это первичное подтверждение формулировок этих двух тематических страниц, а не независимая проверка дат.


## Early Special Series: дополнительные продуктовые типы и границы бренда (2026-11-08)

### Farbs (1972)
Источник: `Early Special Series/Farbs _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает короткоживущую серию 1972 года из четырёх выпущенных cartoonish "people cars", созданных Eddy Goldfarb; инженер проекта — Bob Rosas.
- **Observation.** Ещё два названия, Bye-A-Nose и Wyndan Cheeks, указаны как проекты, не прошедшие стадию прототипирования. В таблице присутствуют четыре выпущенных имени: Hy Gear, Myles Ahead, Red CatchUp и Hot Rodney.
- **Observation.** Страница прямо говорит, что продукция производилась Mattel, использовала колёса, применявшиеся также на Hot Wheels, но официально не брендировалась как Hot Wheels. При этом на упаковке упоминаются Hot Wheels track и аксессуары.
- **Design requirement.** Не выводить принадлежность к бренду Hot Wheels из производителя Mattel, совместимости с трассой или текста на упаковке. Нужен явный Brand Relationship и статусы Released/Prototype.

### Zowees (1972)
Источник: `Early Special Series/Zowees _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Zowees описаны как миниатюрные модели масштаба 1:125. Первые восемь были произведены для Shell Oil Company как promotional items; затем слегка изменённые версии этих восьми и ещё шесть новых моделей продавались через розницу.
- **Observation.** Розничные модели продавались в multipacks, а не по одной; встречались наборы из 2, 3, 4 и 6 Zowees, а также канадские наборы, где одна Zowees сочеталась с машинкой Hot Wheels 1972 года.
- **Observation.** В Германии восемь Shell promotional моделей продавались Mattel Germany под именем Fun Buggies, причём у всех были другие названия.
- **Observation.** Конструкция описана как металлическая база/двигатель с защёлкивающимися пластиковыми кузовом и колёсами.
- **Design requirement.** Моделировать Zowees как отдельный продуктовый тип/масштаб, промо-канал Shell, розничные multipacks и региональные aliases (Fun Buggies) раздельно. В наборе хранить состав, а не искусственно создавать одиночные розничные релизы.

### Truck Co.
Источник: `Early Special Series/Truck Co. _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья определяет Truck Co. как серию тягачей с дополнительными транспортными средствами (bonus vehicles); прямо отмечено использование тех же cab castings, что и в Steering Rigs.
- **Observation.** Таблица имеет 20 строк данных и поля Toy #, Vehicles, Color, Tampo, Notes и изображения.
- **Design requirement.** Общий cab casting должен быть связан с разными product/series releases; bonus vehicle и тягач должны быть компонентами комплекта, а не сливаться в одну сущность.

### Fat Daddy Sizzlers: отдельные модели и аксессуар
Источники: Fireworks, HiWay Hauler, Law Mill, Needle Nose, Ram Rocket, Red Baron (Sizzlers), Steering Trailer.

- **Observation.** Страницы Fireworks, HiWay Hauler, Law Mill, Needle Nose, Ram Rocket и Red Baron описывают модели, введённые в 1973 году и снятые с производства вместе с линейкой Sizzlers в 1973 году. Все связаны с Fat Daddy Sizzlers; большинство описаний приписывают дизайн George Soulakis.
- **Observation.** На страницах имеются отдельные таблицы версий с разными количествами записей: Fireworks — 4, HiWay Hauler — 4, Law Mill — 2, Needle Nose — 5, Ram Rocket — 4, Red Baron — 1 (по числу строк данных).
- **Observation.** Страница Steering Trailer описывает его не как автомобиль, а как аксессуар к Sizzlers: он крепился сзади модели и позволял ей двигаться по прямой, кругу или восьмёрке после зарядки. Он продавался только в Steering Trailer Set вместе с Law Mill.
- **Observation.** В тексте Steering Trailer есть явная редакционная ошибка: предложение о версиях ошибочно называет Ram Rocket вместо Steering Trailer.
- **Design requirement.** Steering Trailer должен быть Accessory/Mechanism component, а Steering Trailer Set — комплектом с отношением состава к Law Mill и аксессуару. Ошибочный текст источника сохранять как provenance, но не использовать как достоверное описание объекта.

### Flip Outs: серия и castings
Источник: `Early Special Series/Flip Outs _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница организована по четырём названиям/разделам: Camaro Wind, Ford Aerostar, Police Car и Nissan 200SX. Таблицы не имеют обычных заголовков, поэтому структуру следует интерпретировать с осторожностью.
- **Observation.** Ссылки внутри таблиц связывают Camaro Wind с Road Flipper и Flipper Snapper, Ford Aerostar — с Capsider и Vaultin' Van; это показывает наличие нескольких имён/вариантов или связанных кастингов внутри разделов.
- **Design requirement.** Сохранять без потерь порядок ячеек и заголовки секций для таблиц без th; не принимать название секции автоматически за имя casting.

**Ограничение:** наблюдения основаны на содержимом архивных Fandom HTML. Исторические даты и атрибуции пока не сверены с независимыми каталогами.
