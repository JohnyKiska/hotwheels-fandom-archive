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


## Early Special Series: ассортиментные системы, технологии и разные поколения (2026-11-08)

### Action Packs (1997–1999)
Источник: `Early Special Series/Action Packs _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает Action Pack как ассортимент блистеров с 1–4 моделями и трековыми аксессуарами; период указан как 1997–конец 1999. Часть tooling кастингов и аксессуаров приписана Corgi Toys.
- **Observation.** Таблицы по годам содержат 8 строк (1997), 7 (1998) и 17 (1999). В примечаниях к JPL Sojourner Mars Rover описана вариация карточки: до посадки марсохода на Марс указывалась планируемая дата посадки 4 июля 1997, после неё надпись убрали.
- **Design requirement.** Упаковочная вариация может быть отдельным Packaging Variant без нового casting/release; комплекты должны иметь компонентный состав и аксессуары.

### California Custom Series (1990–1991)
Источник: `Early Special Series/California Custom Series _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Текст описывает отдельную серию в специальной упаковке с пластиковым медальоном и листом наклеек; медальоны соответствовали темам Street, Beach и Muscle.
- **Observation.** Таблицы 1990 и 1991 годов содержат соответственно 37 и 20 строк данных; поля включают цвет, тампо, материал/цвет базы, окна, интерьер, колёса и Toy #. Одна модель может иметь несколько строк/вариантов.
- **Design requirement.** Тип/тема медальона и упаковочный комплект хранить отдельно от варианта автомобиля.

### Color Changers и Color FX
Источники: `Early Special Series/Color Changers _ Hot Wheels Wiki _ Fandom.html`, `Early Special Series/Color FX _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Color Changers описывает термочувствительную смену цвета, представленную в 1988 году, и несколько связанных ассортиментных названий/поколений: Automagic, Automagic II / Color Racers II, Automagic III и Color Racers. Страница имеет 6 таблиц: 26, 15, 15, 71, 3 и 1 строка данных; последняя таблица является навигационным перечнем Color Shifters, а не перечнем релизов.
- **Observation.** В тексте указано, что Automagic II и Color Racers II использовали одну и ту же группу из 12 машин, но разные варианты блистеров; шесть индивидуальных моделей и шесть комплектов с ice pen/ice cube tray. В одном из вариантов Aeroflash был заменён на Racebait 308.
- **Observation.** Color FX описана как серия пластиковых машинок с изменением цвета, выпущенная в 1993–1995. Структура: 1993 2-Car Sets (16 строк), 1994 Monster Models 2-Car Sets (12), 1995 Super Stampers (6).
- **Design requirement.** Технология color-change должна быть самостоятельным механизмом/атрибутом, а Automagic, Color Racers, Color FX и Color Shifters не следует сливать в одну серию только из-за общей функции. Отдельно хранить состав парных наборов и blister identity.

### Convertables (1991)
Источник: `Early Special Series/Convertables _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница разделяет Hot Rods, Wreckers и Roadsters. Для Wreckers указаны механизмы смятия крыши/подъёма капота, для Hot Rods — выдвижные имитации взорванного двигателя, для Roadsters — поднимающиеся тканевые крыши.
- **Observation.** Roadsters не выпускались, но для них приведены названия и toy numbers: Black Ballet, Formula Fever, Lo-Down Limo и Turnin' T. В таблицах Hot Rods, Wreckers и Roadsters по 4 строки данных; отдельная таблица playset содержит 1 строку.
- **Design requirement.** Хранить невыпущенные позиции со статусом Planned/Unreleased, не превращать их в Released. Функциональные механизмы должны быть описаны на уровне продукта/варианта.

### Crashers: два поколения
Источники: `Early Special Series/Crashers (1999) _ Hot Wheels Wiki _ Fandom.html`, `Early Special Series/Crashers (2007) _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Crashers 1999–2000 использовали металлические кастинги, которые "ломались" при ударе и могли быть возвращены в исходное состояние. Таблицы 1999 Crashers и Crashers 2 содержат 9 и 8 строк данных; отдельно упомянуты два крупномасштабных Ford F-150.
- **Observation.** Crashers 2007–2008 используют пластиковые кузов и базу; удар активирует пружину и отделяет кузов от базы. Страница отдельно перечисляет Vehicles (31 строка), Bonus Vehicle 2-Packs (12), Crashers 3-Pack (3), Playset (3), Mega Wrecks (4) и Bumper Busters (небольшая таблица/раздел).
- **Observation.** В позднем поколении встречаются бонусные обычные Hot Wheels в упаковках, крупные Mega Wrecks с lights & sounds и отдельные наборы. Статья явно предупреждает не путать поколение 2007 с Crashers/Crashers 2 1999–2000.
- **Design requirement.** Два поколения — разные Series Era/product identities с разными механизмами и материалами; бонусные модели и playsets должны быть составными продуктами, не атрибутами одного автомобиля.

### Flippers / Flashmagic Flippers
Источник: `Early Special Series/Flippers _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья связывает Flippers 1990 с дизайнами Lionel, ранее выпущенными как Lionel Revolvers; производство приписано Chief Industrial Co. В 1991 одна модель была переработана с подсветкой/звуком и батарейным питанием под именем Flashmagic Flippers.
- **Observation.** Текст предупреждает, что имена в таблице — имена Lionel, а не имена, присвоенные Hot Wheels. Таблицы содержат 32 строки для 1990, 1 для трековых наборов, 3 для 1991 и 1 для наборов.
- **Design requirement.** Хранить оригинальное имя производителя/разработчика отдельно от официального HW product name; модификацию с новым механизмом считать отдельной модификацией/релизом.

### Gran Toros
Источник: `Early Special Series/Gran Toros _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница описывает линейку масштаба 1:43, производившуюся Mebetoys для Mattel в 1970–1973; производство кастингов происходило в Италии. В Италии использовалось название Sputafuoco, в Германии — Heisse Räder Supergroß.
- **Observation.** Таблица содержит 25 строк моделей и отдельную таблицу из 4 строк track sets/playsets; наборы могли включать автомобиль или продаваться без него. Часть форм была специально создана для Gran Toros, часть происходила от более ранних Mebetoys и модифицировалась.
- **Design requirement.** Обязательно хранить scale, original manufacturer/tooling lineage, regional names и состав набора; не приравнивать 1:43 Gran Toros к стандартным 1:64 Hot Wheels.

### Sizzlers: исторические поколения и ассортимент
Источник: `Early Special Series/Sizzlers _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница описывает моторизованную линейку 1970-х с перезаряжаемой батареей, зарядными устройствами Juice Machine/Goose Pump/Power Pit и отдельной системой Fat Track/гоночных наборов. В таблицах перемежаются автомобили, зарядные устройства, track sets и аксессуары.
- **Observation.** Текст перечисляет 1970, 1971, 1972, Fat Daddy Sizzlers (1973), Sizzlers II (1976), Night Ridin' Sizzlers (1977), hiatus и позднее возрождение 2007–2008. В таблицах есть отдельные исторические и revival блоки: 1970 (8 строк), наборы 1970 (8), 1971 (12), наборы 1971 (12), 1972 (4), revival 2007 (12), аксессуары/наборы 2007 (4), revival 2008 (4).
- **Observation.** В статье также описано переиздание Playing Mantis в 1990-х и прекращение после судебного разбирательства; это отдельный период от Mattel revival 2007.
- **Design requirement.** Моделировать Sizzlers как family/technology с отдельными историческими eras, моделями, chargers, tracks, accessories и sets. Не складывать все таблицы в единый список автомобилей.

### Scorchers и Shift Kickers
Источники: `Early Special Series/Scorchers _ Hot Wheels Wiki _ Fandom.html`, `Early Special Series/Shift Kickers _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Scorchers описаны как spring-powered diecast, введённые в 1979 и снятые в 1982; 12 castings, каждому соответствовали две версии с разными именами. Таблица содержит 24 варианта (23 строки данных плюс заголовок).
- **Observation.** Shift Kickers 1983 использовали modified Scorchers castings и иной механизм: крупный рычаг блокировал/разблокировал колёса. Таблица содержит 6 моделей. Более поздние casting names Shift Kicker в 1991 и 2004 указаны как не связанные с этой серией.
- **Design requirement.** Связь Scorchers → modified casting → Shift Kickers должна быть lineage/derived-from, не тождеством релизов; одинаковое имя Shift Kicker в другие годы не доказывает продолжение.

### RRRumblers
Источник: `Early Special Series/RRRumblers _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** RRRumblers описаны как мотоциклы 1:32 1971–1973 с Track-Rack — съёмной тележкой/опорой с маленькими колёсами для движения по Hot Wheels track. Таблица моделей содержит 16 строк, отдельная таблица rider variations — 44.
- **Observation.** Статья прямо отличает их от Rumblers 2007 со светом и звуком.
- **Design requirement.** Мотоцикл, rider, Track-Rack и track compatibility должны быть отдельными связанными сущностями/компонентами; Rumblers 2007 — отдельная серия.

### Hot Wheels U.S.A. и Hot Wheels World
Источники: `Early Special Series/Hot Wheels U.S.A. _ Hot Wheels Wiki _ Fandom.html`, `Early Special Series/Hot Wheels World _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Hot Wheels U.S.A. — система городских playsets 1980/1981; статья перечисляет региональные названия Hot Wheels World/L'Univers (Канада/UK/Франция) и Meine Kleine Stadt/Il Mondo Hot Wheels (Германия/Италия), а также поздние reissues в Hot Wheels City Sets и Matchbox Adventure Links. Таблица содержит 14 строк.
- **Observation.** Hot Wheels World 1997–2005 описан как совместимая система E-Z Snap track с городскими и stunt/crash playsets. На странице 9 годовых таблиц, от 2 до 23 строк каждая. Есть reissues под Heat Street и Turbo Town, иногда с изменёнными названиями/цветами/наклейками; также встречаются повторы наборов в 2003, 2005 и 2011.
- **Design requirement.** Системы playsets и track — не автомобильные серии; regional naming и reissue lineage должны храниться отдельно от product identity. Совместимость E-Z Snap — явная compatibility relationship.

### Planet Micro
Источник: `Early Special Series/Planet Micro _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница описывает примерно 1:150 масштаб, поздние 1990-е, промежуточную линейку между Micro Hot Wheels и Atomix. Часть моделей основана на 1:64 castings, а Atomix позднее перенёс часть старых и добавил новые формы.
- **Observation.** Страница содержит множество таблиц наборов по темам (NASCAR, space, CAT, rescue, vehicle transport, police, city, military и др.), причём многие строки описывают пары/комплекты, а некоторые таблицы имеют неполные Toy # или пустые ячейки. Отдельная заметка прямо говорит, что Lockheed Martin X-33 в одном наборе на самом деле 1:64, а не micro.
- **Design requirement.** Scale фиксировать на уровне конкретного продукта/выпуска, не наследовать автоматически от серии или набора; сохранять неполные строки и source notes о неверно классифицированных объектах.

**Ограничение:** наблюдения основаны на архивных Fandom HTML; независимая историческая верификация не проводилась.


## Other Early Series: пять страниц, проверка исходной структуры (2026-11-08)

### Action Cycles
Источник: `Other Early Series/Action Cycles _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает мотоциклы примерно 1:12–1:18, выпускавшиеся около 1987–1997/98, первоначально в Hot Wheels Giants. Привод clockwork: оттянуть назад и отпустить; есть поворачиваемые руль/вилка и подвижная центральная подставка. Производитель указан ARCO Toys, дочерняя компания Mattel.
- **Observation.** Таблица содержит 26 строк данных с Toy #, Name, Series, Color.
- **Design requirement.** Масштаб, clockwork mechanism, steering/fork и stand — отдельные характеристики; ARCO Toys фиксировать как производителя, не смешивая с брендом.

### Action Racers
Источник: `Other Early Series/Action Racers _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает автомобили примерно 1:43, выпускавшиеся около 1987–1996, первоначально под Hot Wheels Giants; clockwork pull-back/release mechanism; производитель ARCO Toys.
- **Observation.** Основная таблица содержит 65 строк данных, отдельная Customizers Vehicles — 2 строки. В тексте указано, что некоторые casting повторяются под разными названиями серий, лицензированные машины не всегда имеют proper names; Customizers использует Toy #0606.
- **Design requirement.** Не считать маркетинговое имя серии или Toy # достаточным идентификатором casting; поддержать кастинги без устойчивого официального имени и кастомизируемые версии.

### Attack Pack
Источник: `Other Early Series/Attack Pack _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает линейку 1992–1994 трансформирующихся monster vehicles с несколькими подразделениями: Attack Pack, Big Ones, Biggest Ones, Growlers, Battle Birds, Alien Invaders и Dinosaurs. При нажатии/воздействии продукты открывают пасть или выполняют другие трансформации. В истории есть две команды: Heroic Cat Pack и Evil Rat Pack; таблицы часто содержат Toy #, год, casting name, allegiance и страну.
- **Observation.** На странице есть отдельные таблицы для разных групп/лет; их строки нельзя складывать в один однородный список автомобилей: присутствуют самолёты, инопланетные объекты и динозаврообразные военные машины. Есть раздел unreleased products.
- **Observation.** Статья сообщает, что название Attack Pack повторно использовано в 2026 году для похожих monster trucks в Hot Wheels Monster Trucks. Это одноимённый поздний выпуск, но не основание сливать его с исторической линейкой 1992–1994.
- **Design requirement.** Моделировать Attack Pack как product family/story world с отдельными подразделениями, типами продуктов, allegiance, трансформационными механизмами и lifecycle status. Название 2026 года связывать как name reuse/related theme, а не продолжение по умолчанию.

### Hot Wheels Railroad
Источник: `Other Early Series/Hot Wheels Railroad _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья описывает железнодорожную систему 1983–1985 около 1:64, предназначенную для совместного использования с Hot Wheels; собственный тип рельсов похож на HO и совместим с обычными HO tracks. Локомотивы, вагоны и cabooses соединяются fork-style coupler; производились в Hong Kong, треки — в США.
- **Observation.** Таблицы разделены на rolling stock (14 строк), bundles (5) и playsets/other bundles (12). Наборы могут включать несколько единиц подвижного состава и рельсы. В Канаде использовалось название Le Chemin de Fer.
- **Observation.** Позднее некоторые наборы были переизданы/продолжены в Sto & Go Trucks & Trains, City Trains To Go и Superrails Station.
- **Design requirement.** Хранить locomotives, rolling stock, track pieces, bundles и playsets как разные типы продуктов с component relationships, coupler/track compatibility и региональными aliases.

### Key Force
Источник: `Other Early Series/Key Force _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Key Force — трансформирующиеся игрушки 1992–1994: ключ открывает вторую форму и вставляется в специальные пазы для запуска ракет/активации частей. Ключи индивидуальны для каждого продукта.
- **Observation.** Key Force Warriors — отдельная подсерия 1993 года, где машины трансформируются в роботов. Страница содержит отдельные таблицы Key Force (8 строк), Key Force Warriors (4) и unreleased products (3); упоминаются также McDonald's promotions.
- **Design requirement.** Ключ — уникальный комплектный компонент/инструмент с compatibility только с конкретной игрушкой; трансформационные формы должны быть моделируемы как states/forms одного продукта либо связанные компоненты, а Warriors — отдельный subtype/series relation.

**Ограничение:** наблюдения основаны на архивных Fandom HTML; независимая проверка дат, материалов и производственных атрибуций не проводилась.


## Modern Special Series: первые системные исследования (2026-11-08)

### 100% Hot Wheels / Kalifornia Kustoms
Источники: `Modern Special Series/100% Hot Wheels/2001 100% Hot Wheels _ Hot Wheels Wiki _ Fandom.html`, `.../2006 Kalifornia Kustoms _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Статья 2001 описывает автомобили из 100% castings в индивидуальных акриловых кейсах. Таблица содержит 49 строк данных с Toy #, Casting Name и Color.
- **Observation.** Kalifornia Kustoms 2006 использует те же 100% castings и аналогичную упаковку в акриловый кейс; таблица содержит 12 строк данных, поля Toy #, Casting Name, Color, loose/boxed photos. В таблице есть редакционное замечание о некорректном написании Karmann Ghia как "Karman Ghia".
- **Design requirement.** Acrylic display case — packaging/display format, не свойство casting. Серию/ассортимент 100% следует отделить от общей casting identity и конкретного варианта декора.

### AcceleRacers: 2005, 2006 и 2025
Источники: `Modern Special Series/AcceleRacers/AcceleRacers Series (2005) _ Hot Wheels Wiki _ Fandom.html`, `... (2006) ...`, `... (2025) ...`.

- **Observation.** 2005 AcceleRacers — четыре команды по девять моделей: Teku, Metal Maniacs, Racing Drones и Silencerz. Статья описывает 1:64, специальные anodized finishes на пластиковых кузовах, шестизначные laser-etched base codes, скрытые ребристым блистером, для разблокировки онлайн-контента и игровых машин в Realm Champion. Четыре задуманных мотоцикла (Nightlife, Jaw Jammer, RD-07, Magnesium) не были выпущены; Airy 8 (ранее Jaw Jammer) и Hammer Sled позднее появились в Mainline.
- **Observation.** Страница 2005 имеет 4 таблицы команд по 9 моделей (36 выпущенных позиций), плюс отдельную таблицу track sets/accessories (11 строк данных). Отдельные team membership и series position не заменяют Toy #.
- **Observation.** AcceleRacers 2006 задумывалась как продолжение четырьмя фильмами, с 1:64 basic и 1:24 transformable ассортиментом; фактическая статья описывает семь тематических подсерий: Stripped Metal, Drone'd, AcceleCharged, Acceleron, Team Colors, Realm и другие таблицы/разделы. Встречаются позиции с явной пометкой Unreleased. Шестизначные коды на базах продолжали использоваться для цифрового контента.
- **Observation.** AcceleRacers 2025 — semi-premium/Silver Series assortment к 20-летию оригинала. Таблица содержит 5 моделей; использованы архивные оригинальные графические материалы с переработкой, а не повторное издание прежнего состава.
- **Design requirement.** Хранить franchise/fictional universe, product line era, team affiliation, release, digital unlock code и media tie-in отдельно. Unreleased concepts и фактически выпущенные в Mainline casting должны быть связаны, но не слиты. 2025 anniversary assortment — отдельный release/era, не продолжение линейки 2005 на уровне одной таблицы.

### Boulevard 2012 и 2020
Источники: `Modern Special Series/Boulevard/2012 Hot Wheels Boulevard _ Hot Wheels Wiki _ Fandom.html`, `.../2020 Hot Wheels Boulevard ...`.

- **Observation.** 2012 Boulevard был Walmart exclusive: 30 позиций в тематических группах, из них 5 exclusive castings, остальные 25 находились в regular series. Отдельная таблица 30-Car Set показывает комплектацию и варианты карт, включая upside-down cards.
- **Observation.** Страница 2012 содержит группы Ahead of Its Time, Big Hits, Concept Cars, Legends, Show Rods и Underdogs; таблицы имеют разные количества строк (10, 17, 9, 15, 9, 11), плюс set table.
- **Observation.** Boulevard 2020 организован в 4 mix по 5–6 строк, с полями Toy #, Series #, Casting Name, Body Color, Wheel Type и Base codes. Один Toy #/кастинг может иметь несколько записей/вариантов колёс: Twin Mill #GJT88 в одной таблице приведён с двумя wheel types.
- **Design requirement.** Эксклюзивность к retailer, состав factory set, card orientation, mix/series position и вариант колёс — отдельные атрибуты/сущности. Нельзя считать 30-Car Set одной новой серией или считать один Toy # доказательством единственного wheel variant.

### Car Culture и Team Transport
Источники: `Modern Special Series/Car Culture/2016 Car Culture _ Hot Wheels Wiki _ Fandom.html`, `.../2026 Car Culture ...`, `.../2026 Car Culture_ Team Transport ...`.

- **Observation.** Car Culture 2016 содержит четыре тематических микса: Japan Historics, Euro Style, Trucks, Track Day; каждая таблица содержит 5 моделей (20 позиций).
- **Observation.** Car Culture 2026 отмечает десятилетие линейки и включает восемь тематических миксов по пять моделей (40 основных позиций). Таблица 2026 указывает Toy #, Series #, Casting Name, Body Color, Wheel Type, Base codes, notes о New Casting/New Die-Cast Chassis. Chase-модели описаны как отдельные автомобили в gold finish из любимых моделей прошлых лет, а не просто окрашенные дубликаты основных моделей.
- **Observation.** Team Transport 2026 содержит миксы, где строка автомобиля и строка транспортёра/трейлера выступают парными элементами одного набора. Встречаются новые transport castings и отдельный Walmart Legends Tour Exclusive set.
- **Design requirement.** Car Culture — umbrella assortment с ежегодными mix/series; Team Transport — связанный, но отдельный наборный формат. Транспортёр и перевозимый автомобиль — два продукта в одном package/set, с отдельными casting/release records и отношением комплектности. Chase — отдельный release/variant, а не обязательно chase repaint того же casting.

### Character Cars: лицензии и формы
Источники: `Modern Special Series/Character Cars/Star Wars Character Cars _ Hot Wheels Wiki _ Fandom.html`, `.../Marvel Character Cars ...`, `.../Disney Character Cars ...`.

- **Observation.** Star Wars Character Cars стартовали в 2014; машины представляют персонажей, а faction logo на базе отражает принадлежность к Jedi Order, Galactic Republic, Empire, Resistance, Separatist, First Order, Sith и др. Страница разбивает данные на single packs, 2-packs, exclusives и playset exclusives; одна и та же модель/персонаж может встречаться в разных упаковочных контекстах и вариантах декора. Есть convention exclusives и отдельные casting reuse references.
- **Observation.** Marvel Character Cars стартовали в retail в конце 2014. Таблицы включают single packs, 2-packs, comic-book bundles, RLC/HWC exclusives, retailer exclusives и playset-only vehicles. Есть прямые cross-references вида "Same as" между разными Toy #/декорациями, что демонстрирует повторное использование casting.
- **Observation.** Disney Character Cars начались в 2018 с шести машин и расширились на Disney/Pixar properties. С 2020+ повторно используемые модели и упаковка без Series # сопровождаются пометкой "New" для first appearance; в ассортимент включены тематические наборы и Disney 100 anniversary release с персонажами Disney, Marvel, Star Wars и Pixar.
- **Design requirement.** Character Cars требуют разделения licensed character/IP, character identity, vehicle casting, decoration/variant и release. Faction/allegiance — атрибут персонажа/вселенной или оформления, не casting. Single pack, 2-pack, comic bundle, retailer/convention exclusive и playset exclusive — packaging/set relationships. "Same as" фиксировать как casting reuse или deco relation, не объединять разные Toy #.

### Color Shifters и Color Reveal
Источники: `Modern Special Series/Color Shifters/2008 Color Shifters _ Hot Wheels Wiki _ Fandom.html`, `.../2026 Color Shifters ...`, `Modern Special Series/Color Reveal _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** 2008 Color Shifters использует температурно-зависимое изменение цвета; таблица содержит 31 строку и отдельно указывает warm/cold colors. 2026 таблица имеет 24 позиции и три температурных состояния: Cold, Moderate, Warm; отдельные состояния не следует сводить к двум статическим цветам.
- **Observation.** Color Reveal обозначена как sub-series Color Shifters. На кастинг нанесено водорастворимое покрытие, которое растворяется при первом погружении, после чего работает обычный color-change mechanism. Упаковка — барабан, запечатанный в пластиковый пакет, с двумя машинками; барабан может использоваться как dunk tank и контейнер для хранения. Код упаковки различает составы. В 2023 у моделей металлические кузова вместо пластиковых в ранних Color Reveal.
- **Design requirement.** Color-change mechanism, temperature states, initial soluble coating, material/body construction, package container и package contents должны быть раздельными данными. Color Reveal — связанная подсерия/технологический вариант Color Shifters, но не просто alias.

### Pop Culture, Replica Entertainment и Fast & Furious Premium
Источники: `Modern Special Series/Pop Culture/2013 Pop Culture _ Hot Wheels Wiki _ Fandom.html`, `.../2026 Pop Culture ...`, `Modern Special Series/Replica Entertainment/2023 Replica Entertainment ...`, `Modern Special Series/Fast & Furious Premium Series/2026 Fast & Furious Premium Series ...`.

- **Observation.** Pop Culture 2013 разделён по лицензионным темам (Looney Tunes, The Muppets, King Features Syndicate, DC Comics, General Mills, AC/DC/Live Nation, Universal Monsters, Archie, Mars, Hanna-Barbera и др.). Таблицы имеют Toy #, Casting Name, Theme, Body Color, Wheel Type, Notes. Встречаются новые кастинги, коммерческие/брендовые liveries и несколько машин по одной IP.
- **Observation.** Pop Culture 2026 представлен шестью миксами по 5–6 позиций; тематические лицензии включают Stranger Things, Godzilla, Gran Turismo, G.I. Joe, Forza, Dracula, Airwolf и др. Некоторые строки прямо отмечают идентичность релизу 2025 года.
- **Observation.** Replica Entertainment 2023 включает три микса, а также Disney 100 Premium 5-Pack. В таблицах есть cross-reference "Similar to" и "Identical to" для сопоставления с другими Toy #/релизами.
- **Observation.** Fast & Furious Premium 2026 содержит четыре микса по пять моделей, chase cars с Spectraflame и отдельный Brian O'Conner Bundle. Примечание указывает, что в каждом case один chase, а вместо него в mix case добавляется дополнительный экземпляр одной из основных моделей как filler.
- **Design requirement.** Лицензия/IP и тематическая группировка не должны становиться частью casting identity. "Similar to", "Identical to", "New Casting" и "New Die-Cast Chassis" — разные отношения/события. Chase allocation и case assortment — данные уровня distribution/case pack; bundle composition отдельно от individual releases.

**Ограничение:** это постраничные observations по архивным Fandom HTML; цифры и исторические утверждения требуют независимой сверки с упаковками, каталогами Mattel и другими источниками.


## Modern Special Series: Pro Racing, Garage, Delivery, id и смежные линии (2026-11-08)

### Pro Racing: Premium и Basic
Источники: `Modern Special Series/Pro Racing/1997 Pro Racing _ Hot Wheels Wiki _ Fandom.html`, `.../2005 Pro Racing ...`, `.../Basic Pro Racing Series ...`.

- **Observation.** Pro Racing 1997 Premium разделён на Collector 1st Edition, Short Track 1st Edition, Superspeedway 1st Edition, Season Summary и Racing Trucks. Таблицы используют Casting, Team/Number, Primary Sponsor, Base Color/Material, Interior, Wheel Type, Toy #, Country и Notes/Variations. Повторяющиеся Chevrolet Monte Carlo могут иметь разные гриль/направление/вариант оформления при тех же базовых идентификаторах.
- **Observation.** Basic Pro Racing дебютировал параллельно с premium в 1997. Статья прямо противопоставляет пластиковые колёса/базы и меньшее количество деталей Basic, рассчитанного на игру/трек, более дорогим display-oriented premium castings. Basic использовался для commemorative blisters, baggie promos и MLB team promotions. Таблицы включают разные годы 1997–2002, kart releases и промо-наборы.
- **Observation.** Basic и Premium могут использовать одну гоночную машину/ливрею, но с разными материалами и колёсами; Toy #22500 применяется к non-promotional cars только на international cards. В 2005 Pro Racing страницы сгруппированы по кастингам '67 Plymouth, Dodge Charger Stock Car и Taurus Stocker; таблицы отражают команду/спонсора/колёса/серию, включая альтернативные схемы окраски.
- **Design requirement.** Pro Racing нельзя хранить как один список машин: нужны competition/team identity, sponsor, race number, season, casting, livery, Basic/Premium construction, promo status, regional packaging и отдельные race-series groupings.

### Hot Wheels Delivery (2009–2010)
Источник: `Modern Special Series/Hot Wheels Delivery _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** 2009 Sweet Rides содержит 15 castings с candy-themed deco, die-cast body и chassis. В 2010 Slick Rides содержит 34 castings с логотипами automotive parts retailers; большинство выпускалось в двух цветах, все с die-cast body/chassis и Real Riders. Отдельный Toy R Us set включал все castings плюс пять set exclusives с Real Riders. В части упаковок ошибочно напечатано #/25 вместо #/34.
- **Observation.** Таблицы содержат 20 строк (2009) и 63 строки (2010), включая повторы Super Van с разными цветами и одинаковым Toy # R3727, помеченные Re-Tooled.
- **Design requirement.** Retailer/candy theme, livery, material construction, Real Riders, retool status и set-only exclusivity должны быть отдельными полями/отношениями; печатную ошибку упаковки хранить как source/packaging note.

### Hot Wheels Garage и Larry's Garage
Источники: `Modern Special Series/Hot Wheels Garage (2010) _ Hot Wheels Wiki _ Fandom.html`, `.../Hot Wheels Garage Series (2016) ...`.

- **Observation.** Hot Wheels Garage 2010 следует за Larry's Garage 2009; в 2010 участвовали дизайнеры Larry Wood, Phil Riehlman и graphics guru Wayne Scott. Статья указывает восемь новых castings, девять mass-market exclusive castings (по три для Toys R Us, Walmart и Target) и 30-Car Set. Основная таблица содержит 119 строк и смешивает дизайнерские гаражи, цветовые варианты и эксклюзивы.
- **Observation.** Hot Wheels Garage Series 2016 — отдельный Walmart exclusive выпуск из 10 моделей, таблица содержит 10 строк с Col #, Toy #, Casting, Body Color, Wheel Type и Notes.
- **Design requirement.** Designer attribution, retailer exclusivity, factory set, yearly series identity и casting variant — разные измерения; не объединять Garage 2010 и Garage 2016 по одному имени.

### Hot Wheels id (2019–2022)
Источник: `Modern Special Series/Hot Wheels id _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Hot Wheels id использовал NFC microchip в каждой машине, приложение, Race Portal и Smart Track для записи прогресса/игровых функций; Race Portal был совместим и с обычным Hot Wheels track. Машины имели Spectraflame paint и эксклюзивные id wheels; часть castings была retooled для трека. Статья сообщает о прекращении серии в 2022 из-за слабых продаж, overproduction и завершения chip license, публичное объявление — в 2023.
- **Observation.** Структура статьи включает yearly series/mixes, race portal exclusives и отдельные промо/эксклюзивы. Примеры явно помечены Modified Casting, New Casting, Amazon Exclusive. Встречаются позиции, изначально предназначенные для промо, отменённого из-за COVID-19.
- **Design requirement.** NFC chip identity, app/service compatibility, track compatibility, digital progress, casting modification, release status и exclusivity — самостоятельные связи. Система id не просто декоративная серия, а physical-digital product ecosystem.

### Nostalgic Brands
Источник: `Modern Special Series/Nostalgic Brands _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** Страница объединяет релизы 2011–2012 с лицензированными брендами и ретро-темами: Masters of the Universe, DC Comics, General Mills, Hershey's, Hanna-Barbera, Carvel Ice Cream, The Saturday Evening Post, AC/DC, Atari и др. Таблицы имеют Toy #, Casting Name, Theme, Body Color, Wheel Type и Notes.
- **Observation.** Одна casting может быть использована для разных брендов/тем; часть строк обозначена New tool. Тема может быть конкретным персонажем, продуктом/брендом, художественной работой или музыкальным исполнителем.
- **Design requirement.** Не моделировать Nostalgic Brands как единый лицензированный universe: нужны generic brand/IP/theme records с типом правообладателя и отношением к конкретной ливрее/релизу.

### Flying Customs (2020–2022)
Источник: `Modern Special Series/Flying Customs/Flying Customs Series (2020) _ Hot Wheels Wiki _ Fandom.html`.

- **Observation.** 2020 Target-exclusive Flying Customs описана как продолжение Throwback Series 2019. Страница содержит mix 2020 (две таблицы по 8 строк), 2021 (две таблицы по 8 строк и 10-pack) и 2022 (отдельный раздел/таблица). Таблицы фиксируют Toy #, Casting Name, Body Color, Tampos, Notes.
- **Design requirement.** Target exclusivity, yearly mix, multi-pack composition и throwback/retro styling theme должны быть отдельными сущностями/атрибутами. Нельзя наследовать статус эксклюзивности с одной эры на другую без проверки.


### Hot Wheels Classics (2005–2009)
Источник: `Modern Special Series/Hot Wheels Classics _ Hot Wheels Wiki _ Fandom.html` (обновлённый архивный HTML, Git blob `70d9be50320809395b6a4d7fd220dd96a5ac9ad2`; Fandom revision ID 804424). Статус ниже — Observation по Fandom HTML, не независимая историческая верификация.

- **Observation.** Страница организована в пять отдельных разделов Hot Wheels Classics Series 1–5, затем отдельный раздел Track sets. Категории страницы указывают 2005, 2006, 2007, 2008 и 2009 Hot Wheels; Series 3 прямо назван выпуском 2007 года, Series 4 — 2008 года, а Series 5 содержит карточку с подписью 2008. Следовательно, нельзя автоматически приравнивать номер Series к календарному году без проверки каждой секции/упаковки.
- **Observation.** Пять основных таблиц имеют соответственно 174, 199, 138, 66 и 44 HTML-строки данных (всего 621 строки), при номинальной нумерации 25, 30, 30, 15 и 30 позиций. Число строк отражает повторяющиеся цветовые/колёсные/интерьерные/эксклюзивные варианты, а не число уникальных casting или релизов.
- **Observation.** Series 1–3 используют таблицы с полями Toy #, Series #, Model Name, Body Color, Wheel Type, Notes и изображениями loose/carded. Series 4 меняет схему на Toy #, Series #, Model Name, Color, Notes; Series 5 содержит Toy #, Series #, Model Name, Notes. Отсутствие отдельных столбцов цвета и колёс в Series 5 не означает отсутствия таких различий: описание отдельно упоминает варианты цвета, foil seal и Real Riders Chase.
- **Observation.** Один Toy # повторяется для множества цветов/вариантов; одна позиция Series # может иметь несколько записей с разными цветами, wheel types, интерьерами и notes. Примеры: Series 1 1957 Chevy Bel Air (H7066, 1/25) включает несколько цветов и две записи синего с разными размерами колёс; Series 2 1965 Mustang (J2762, 6/30) содержит различия интерьера и ориентации логотипа; Series 2 1962 Chevy Bubble Top (J2758, 2/30) имеет несколько цветов и вариант с Clear & White interior.
- **Observation.** Номер игрушки не всегда однозначно соответствует одной строке/варианту. В Series 4 один и тот же Series # и casting могут иметь разные Toy # для ранней Button-версии и последующих Spectraflame вариантов (например, Evil Twin 1/15: M3655 и M1858). Описательный текст говорит, что в 2008 число моделей было сокращено с 30 до 15, но существовали два набора по 15: Hot Wheels Vintage Classics with Buttons и последующая Hot Wheels Classics в Spectraflame colors. Это важное различие между нумерацией в серии и отдельными продуктами/релизами.
- **Observation.** Series 3 включает Walgreens-exclusive варианты и Walgreens 3-packs; таблица также содержит дополнительные строки с кодами M1809 и текстом упаковки/пакета, которые не следует без проверки считать обычными самостоятельными позициями основной нумерации. В Series 2 отмечены Comic-Con Exclusive (1/3000), RLC Rewards и Classics Series 2 Set Exclusive.
- **Observation.** Series 4 использует Spectraflame color naming и варианты с кнопкой (button); в Notes есть указания на изменение цвета (например, переход Ice Blue → dark). Следует хранить точную формулировку источника, не сводя все цветовые названия к нормализованному цвету без исходного значения.
- **Observation.** Series 5 содержит Chase-строки и текстовое описание, что часть castings выпускалась с foil seal на карточке и Real Riders tires в меньших количествах. Для 2001 Mini Cooper (15/30), 8 Crate (16/30), '62 Corvette (22/30), Dune Daddy (24/30) и School Busted (30/30) таблица содержит Chase или несколько повторяющихся записей; Chase нельзя определять только по названию модели.
- **Observation.** В отдельном разделе Track sets перечислены Strip Action Set, Stunt Action Set, Drag Race Action Set, Mongoose & Snake Drag Race Set, Super Charger, Loop & Chute Action Set и Hot Curves Race Action Set. Текст указывает, что наборы выпускались рядом с автомобилями и имели обновлённую графику коробок и translucent track joiners вместо красных соединителей. Эти наборы не являются вариантами отдельных машин.
- **Design requirement.** Разделять Series Position, Toy Number и конкретный Release/Variant. Toy # не является ключом варианта и не должен заменять идентификатор релиза.
- **Design requirement.** Варианты цвета, Spectraflame finish, wheel type, interior, tampo/logo orientation, wheel-size differences, foil seal, Real Riders, button accessory и Chase designation хранить как отдельные атрибуты/связи уровня Release/Variant/Packaging, сохраняя исходные Notes.
- **Design requirement.** Для multi-pack и track sets нужна сущность Set/Assortment и состав Product Components; Walgreens 3-packs и Classics track sets нельзя сворачивать в строки основной автомобильной таблицы.
- **Design requirement.** Поддержать неодинаковые схемы исходных таблиц и неполные поля по источнику; импортёр должен сохранять raw row/source cell content и не интерпретировать отсутствие колонки как отрицательное значение.


## Flying Customs (2006, 2007, 2013): ранние релизы

Источник: сохранённые страницы `Modern Special Series/Flying Customs/Flying Customs Series (2006) _ Hot Wheels Wiki _ Fandom.html` (Fandom revision 617095) и `... (2013) ...` (revision 774708). Статус ниже — **Observation**, если не указано иное.

- Страница 2006 описывает Flying Customs как эксклюзив Target, выпущенный в 2006 и 2007 годах, параллельно с Super Chromes и Lowriders, как ретро-трибьют 1970-м. В HTML две раздельные годовые таблицы: 2006 — 17 строк данных (16 с указанной страной Malaysia, одна Scorchin' Scooter без страны); 2007 — 7 строк данных (5 Malaysia, 2 China). Всего 24 записи.
- Таблица 2006 содержит Toy #, Casting Name, Body Color, Country, Notes/Variations и изображения. Таблица 2007 имеет ту же схему. Toy # K4745/K4763 и L5855/K4747 и т. п. фиксируют разные товарные записи одного casting: например, '56 Flashsider (Black/Dark Orange), Baja Breaker (Light Brown/Magenta), Corvette Stingray (Chrome/Green/Orange/Yellow), VW Bug (Blue/Red). Это не отдельные castings.
- Страница 2013 содержит одну таблицу на 27 строк данных, разбитых на шесть Mix (1–6). Поля: Toy #, Casting Name, Body Color, Wheels Type, Notes; в Notes находятся base codes и пометки New tool!/New die-cast chassis!. В тексте заявлены все модели made in Thailand и сочетание UH, GHO, SHO, BW и CT wheels.
- В 2013 таблице Mix 1–6 — группировка ассортимента/волн, а не самостоятельные серии с отдельной нумерацией. Base codes могут перечисляться несколькими значениями на одну строку (например, Dumpin' A: E39, E41, E42; Amphicar: E46, E48, E49, E50), поэтому коды не следует сводить к одному полю/одному значению.
- В 2013 есть 7 строк с явными отметками New tool! или New die-cast chassis! (проверять отдельно: эти два обозначения описывают разные изменения). Для 2013 указаны разные типы колёс, иногда непосредственно в Wheels Type (UH у Porsche 914-6, BW у Porsche 935/78), тогда как у остальных ячеек поле часто содержит только Mix.
- **Observation / identity caution.** Общее название Flying Customs встречается как минимум в релизах 2006–2007 и 2013, но страницы не доказывают непрерывность одной Series Identity. Различаются каналы/контекст, схема таблиц, география производства и структура волн. Сопоставлять как отдельные релизные периоды под общим названием до независимой проверки.
- **Design requirement.** Хранить Mix/assortment wave отдельно от Series Position; поддерживать несколько base codes на релиз, country of manufacture, wheel type и отдельные события tooling/chassis change. Не считать одинаковое название достаточным основанием для объединения идентичностей серии.


## Hot Wheels Cool Classics (2013–2014)

Источник: `Modern Special Series/Cool Classics _ Hot Wheels Wiki _ Fandom.html`, Fandom revision 709071. Все выводы ниже — **Fandom observations**, требующие независимой сверки с упаковками/каталогами.

- Страница описывает Cool Classics как линию, впервые выпущенную в 2013 году и ориентированную на adult collectors; указаны ориентировочная цена US$3.99, metal base, Spectrafrost colors, Retro Slot Wheels и производство всех моделей в Thailand.
- Две годовые секции: 2013 и 2014. В каждой таблице ровно 30 строк, позиции 1/30–30/30. Итого 60 записей таблиц, без утверждения, что это 60 уникальных castings.
- Схема обеих таблиц одинакова: Series #, Model Name, Color, Toy #, Notes, loose/carded images. Для всех 30 строк каждого года указан Spectrafrost и отдельный Toy #.
- 2013 Toy # диапазон Y9424–Y9453 идёт непрерывно по 30 позициям. 2014 использует BDR-коды от BDR22 до BDR51, но в таблице порядок Toy # не совпадает с числовым порядком (например, позиции 1–10: BDR22, BDR31, BDR24–BDR30, BDR23). Не сортировать ассортимент по Toy # и не считать его Series Position.
- В 2013 описание упаковки: серебряный фон за автомобилем и artwork Custom Otto в двух цветах — blue или red; все модели, по утверждению страницы, выходили с обоими вариантами artwork. В 2014 фон белый, Custom Otto artwork gold или pink; также указаны обе версии artwork для каждой модели. Это вариации card artwork, а не разные автомобильные цвета/кастинги.
- В таблицах не выделены wheel type или country по каждой строке; текст даёт общие характеристики для всей линии. Не дублировать эти значения в исходных строках как будто они были указаны индивидуально.
- **Design requirement.** Series Position, Toy #, casting/model identity, Spectrafrost body color и card artwork variation должны быть независимыми сущностями/атрибутами. Варианты упаковочного artwork должны связываться с Packaging/Release, а не создавать новый casting или vehicle variant.
- **Observation.** 2013 и 2014 используют одинаковую номинальную структуру 30 позиций и общее имя, но свои Toy # ranges и artwork schemes; моделировать как годовые выпуски/assortments внутри линии, сохраняя исходные данные каждого года.


### Crashers (2007) и родственные продукты (Fandom revision 756909)

- **Observation (Fandom).** Страница явно отделяет Crashers 2007 от Crashers 1999 и 2000. Для оригинальной серии указаны all-metal castings; выпуск 2007 описан как plastic body / base.
- **Mechanism (Fandom description).** При столкновении с препятствием срабатывает пружина, откидывающая корпус от основания, визуально создавая «crashed» состояние. В таблице направление откидывания указано как Back-Flipping, Side-Flipping или Front-Flipping. Неизвестно, одинаков ли механизм/геометрия для всех продуктов семейства.
- **Core Vehicles table.** 32 строки данных. Поля: Casting Name, Color, Crash Type, Wheel, Toy #, Photo, Crashed. Повторяются шесть имён Smash Masters, Wreck 'n' Roll, Dents-a-Lot, Dread Head, Skull Crushers, Bone Bashers с несколькими цветами и Toy #. Также присутствуют Wall Wrecker, Head Smasher, Side Splitter, Street Skid, Speed Bump и Road Thrash. Не считать строки таблицы уникальными кастингами: это записи релизов/вариантов.
- **Toy # anomalies.** У одной строки Wreck 'n' Roll / Red указан «?» вместо номера. N0891 встречается у Street Skid / Gold и Street Skid / Orange; это может быть ошибка страницы или реальное повторное использование номера, требует проверки. Для Street Skid / Red указан N0867, выбивающийся из соседнего диапазона. Сохранять raw value и пометить аномалии, не исправлять автоматически.
- **Wheel field.** В ячейках встречаются обозначения C6SP, C5SP, CWSP, а также составные строки вроде Orange C6SP, Red C5SP, Red CWSP, Black, Silver. Неясно, какие слова описывают цвет колеса, а какие его тип/код. Хранить исходную строку; не раскладывать без проверки.
- **Bonus Vehicle 2-Packs.** Первый wave Crashers также выпускался в упаковках с дополнительной обычной Hot Wheels машиной. Таблица содержит шесть Toy # (N1722–N1727), каждая строка визуально/структурно объединяет одну обычную машину (Power Pistons, Slikt Back, Torque Screw, Dogfighter, 40 Somethin', Surf Crate) с одним Crasher (Smash Masters, Wreck 'n' Roll, Dents-a-Lot, Dread Head, Skull Crushers, Bone Bashers). Это упаковка-комплект с двумя разными продуктами, а не один casting или одна модель.
- **Crashers 3-Pack.** Отдельный 3-pack с Toy # N9337 содержит Smash Masters Blue, Wreck 'n' Roll Green и Dents-a-Lot Red. Это pack/SKU, включающий три самостоятельных Crasher products.
- **Playset.** Назван Crossroad Crash; страница не приводит SKU, состав или подробное описание. Считать наличие playset зафиксированным, его комплектацию оставить unresolved.
- **Mega Wrecks (2008).** Страница описывает их как более крупные версии Crashers, основанные на mainline castings и оснащённые lights & sounds. Три записи: Rivited Blue / N2882 / Back-Flipping; Bassline Black / N2883 / Front-Flipping; Spine Buster Red / N2884 / Side-Flipping. Это родственная продуктовая линия 2008 года, но не автоматически та же серия или тот же масштаб/механизм, что Crashers 2007.
- **Bumper Busters.** Описаны как ещё более крупные play vehicles, основанные на дизайнах обычных Crashers. Вместо простого откидывания корпуса имеют multi-stage detailed crash damage. Четыре записи: Wreck 'n' Roll Green M6189; Bone Bashers Blue M6190; Wreck 'n' Roll Silver M6191; Bone Bashers Black M6192. По смыслу это отдельный тип продукта/механики и крупный масштаб, не просто цветовые варианты базовых машин.
- **Design implications.** Crash mechanism и crash action/direction должны быть отдельными сущностями/атрибутами. Нужны Product Type / Product Form, Scale (если известен), mechanism activation/action, moving/detachable components и product state/visual transformation. Комплекты/упаковки должны иметь Pack/Assortment и Product Components с количеством и ролью компонента. Mega Wrecks и Bumper Busters требуют моделирования как отдельных продуктовых линий/типов с отношениями based_on к casting/design family, а не как обычных релизов масштаба 1:64.
- **Evidence status.** Все сведения в этом разделе извлечены из сохранённой страницы Hot Wheels Wiki (Fandom revision 756909); это source observations, не независимая проверка Mattel packaging/catalogues.


### Dragstrip Demons (2009–2010)

- **Observation (Fandom).** Страница описывает Dragstrip Demons как список выпусков 2009 и 2010 годов. Заявлены 55 разных автомобилей за два года, 18 использованных castings, из которых 13 названы brand-new never-before-seen. Указаны metal base, Real Rider wheels и detailed decoration; большинство моделей имитируют реальные drag cars.
- **Line chronology.** Страница говорит, что Dragstrip Demons была заменена Vintage Racing в 2011 году. Отдельно отмечено, что в 2018 сегмент Car Culture получил название Dragstrip Demons и использовал оригинальный логотип. Это observation о повторном использовании имени/лого, но не доказательство непрерывной Series Identity.
- **2009 table.** Номинальная сетка 01/30–30/30. В позиции 18 прямо указано “This vehicle was not produced” и N/A. У позиции 05/30 Sox & Martin Super Stock Barracuda повторяются Model Name и Toy # N8964, но Notes различает Goodyear RR5SP и Goodyear RRMag. Следовательно, одна позиция/номер может иметь две wheel variants.
- **2010 table.** Номинальная сетка 01/25–25/25. Позиция 12/25 встречается дважды: '70 Plymouth Duster F/C - Tarmac Twister (V7177) и '63 Nova AWB Snake Eyes (V4237). Страница поясняет, что Nova изначально планировалась как позиция 18 предыдущего года, что и объясняет повторный 12/25. В строке #19 для Mongoo$e McEwen's Wedge Dragster есть note, что Tom “Mong00$e” McEwen никогда не имел такого Wedge Dragster; строка помечена N/A not a Real Dragster of Tom's. Это пример разделения модели и достоверности исторической ливреи/атрибуции.
- **Fields.** Таблицы содержат Series #, Model Name, Toy #, Notes, Real Car, loose/card images. Не считать Series # или Toy # универсальным ID: есть повторяющиеся позиции/номера, пропущенный выпуск и wheel variants.
- **Evidence status.** Все сведения в этом разделе извлечены из сохранённой страницы Hot Wheels Wiki (Fandom revision 807648); это source observations, не независимая проверка Mattel catalogues, упаковок или drag-racing history.


### Vintage Racing (2011)

- **Observation (Fandom).** Страница прямо называет Vintage Racing линией 2011 года, заменившей Dragstrip Demons. Заявлено 30 castings и производство всех автомобилей в Thailand.
- **Table structure.** Одна таблица с 30 позициями 01/30–30/30. Поля: Series #, Model Name, Color, Toy #, Notes, loose/card images. Toy # лежат в диапазоне T8451–T8541 (не непрерывном). Каждая строка содержит Base code(s), иногда несколько кодов (например, позиции 04/30: C42, C46; 09/30: C45, C47; 15/30: D34, D35; 23/30: D34, D36).
- **Packaging error.** Для John Morton's BRE Datsun Bluebird 510, Series #15/30, Toy # T8455, Notes сообщает: “Cards were produced with #22 in error”. Это напечатанная ошибка номера на карточке, а не изменение фактической Series Position.
- **Lineage.** Прямая формулировка “replacing the Dragstrip Demons” даёт более сильное свидетельство преемственности/замены, чем простое сходство названия. Однако это не доказывает, что обе линии должны быть одной Series Identity в БД: нужно сохранить relation типа successor/replaced_by.
- **Evidence status.** Наблюдения извлечены из сохранённой страницы Hot Wheels Wiki (Fandom revision 797035); не подтверждены независимыми каталогами/упаковками.


### Dragstrip Demons (Car Culture, 2018)

- **Observation (Fandom).** Dragstrip Demons is one of six 2018 Car Culture segments listed on the 2018 page. The segment contains five vehicles, positions 1/5–5/5, with Toy # FVN69, FVN73, FVN72, FVN71 and FVN70.
- **Vehicles.** '55 Chevy Bel Air Gasser (green); '63 Chevy Nova (red); '65 Dodge Coronet (yellow); '65 Mercury Comet Cyclone (white); '66 Super Nova (blue).
- **Wheel detail.** The table records detailed wheel names/types per release: Hoosier RRDragD & RRPrf; Goodyear Eagle RRMag; White Hoosier DDRR & Gold RRPrf; Hoosier RRDragD & RRWSP; Goodyear RRDragS & RRPrf. These should remain release-level wheel configuration data, preserving the raw strings and multiple wheel types where shown.
- **Base codes.** Notes contain L35/L36/L39, sometimes multiple codes per release. Preserve as raw multi-valued codes, not Toy # or Series Position.
- **Relation to 2009–2010.** Reuse of the Dragstrip Demons name and original logo was noted on the 2009–2010 page, while the 2018 page places this five-car segment inside Car Culture. This is a later themed segment/name revival; it should not be merged with the earlier 55-release series without stronger identity evidence.
- **Potential model overlap.** 2018 includes a '63 Chevy Nova, while 2010 Dragstrip Demons includes a '63 Nova AWB “Snake Eyes”. Similar year/model wording is not enough to establish identical casting or tooling. Verify casting identity separately.
- **Evidence status.** Extracted from Hot Wheels Wiki (Fandom revision 760101), not independently checked against packaging or Mattel catalogues.

### Vintage Racing Club (2024)

- **Observation (Fandom).** The page describes Vintage Racing Club as a themed series featuring “pre-1974” vehicles from various manufacturers with racing-style decos, and classifies it as part of Hot Wheels “silver label” semi-Premium series.
- **Assortment structure.** Two mixes: Mix 1 has six positions (1/6–6/6), Mix 2 has five (1/5–5/5), total 11 listed releases. Mix is assortment grouping, not a single continuous Series Position sequence.
- **Mix 1.** Toy # HRV00–HRV05: 1954 Mercedes-Benz 300 SL; 1955 Corvette; BMW 2002; 1971 Lamborghini Miura SV; 1971 Porsche 911; 1967 Camaro. Wheel types S5, C5, C5, MM5, C5, MM5. The 1967 Camaro row explicitly notes an opening hood and has the unusual raw note “Base code(s); S43”; the other rows use “Base code(s):”. Only the 300 SL and Corvette rows explicitly state “Metal base”. Do not generalize this to all 11 releases from the table alone.
- **Mix 2.** Toy # HRV06–HRV10: 1962 Corvette; Toyota 2000GT; 1969 Ford Mustang Boss 302; Custom Ford Maverick; Custom Datsun 240Z. Wheel types S5, C5, MM5, P4, P4.
- **Data characteristics.** Table fields: Series #, Toy #, Casting Name, Color, Tampos, Wheel Type, Notes. Multiple base codes per release, detailed tampo descriptions and wheel types should be retained at release level. The 1971 models satisfy the stated “pre-1974” theme boundary.
- **Identity distinction.** This is not the 2011 Vintage Racing line merely because of the shared words “Vintage Racing”. Different year, naming, assortment structure and Toy # namespace; keep as a separate series/assortment identity unless external evidence establishes a formal relation.
- **Evidence status.** Extracted from Hot Wheels Wiki (Fandom revision 703020), not independently verified against packaging/catalogues.


## Formula One Collection (2025–2026)

**Sources:** `Modern Special Series/Formula One Collection/2025 Formula One Collection _ Hot Wheels Wiki _ Fandom.html` (Fandom revision 780455) and `Modern Special Series/Formula One Collection/2026 Formula One Collection _ Hot Wheels Wiki _ Fandom.html` (revision 816712). Status: **Observation** from archived Fandom HTML; not independently verified.

### 2025 page
- Three release tables contain **16 individual driver-specific cars** (6 + 6 + 4 rows), not 18. Each row has columns `Toy #`, `Casting Name`, `Driver`, `Wheel Type`, `Notes`, loose/card photos.
- Toy #s and row data:
  - JBM09 — BWT Alpine F1 Team - A524 (#31), Esteban Ocon; stand U13A.
  - JBM10 — MoneyGram Haas F1 Team - VF-24 (#20), Kevin Magnussen; U14A, U22A.
  - JBM12 — Oracle Red Bull Racing - RB20 (#1), Max Verstappen; U13A, U31A.
  - JBM19 — Oracle Red Bull Racing - RB20 (#11), Sergio Pérez; U15A, U22A.
  - JBM21 — BWT Alpine F1 Team - A524 (#10), Pierre Gasly; U13A.
  - JBM22 — MoneyGram Haas F1 Team - VF-24 (#27), Nico Hülkenberg; U14A, U22A.
  - JBM11 — McLaren Formula 1 Team (#4), Lando Norris; U21A, U24A, U27A.
  - JBM13 — KICK Sauber F1 Team (#77), Valtteri Bottas; U23A, U24A.
  - JBM15 — Williams Racing - FW46 (#23), Alex Albon; U24A.
  - JBM20 — Williams Racing - FW46 (#43), Franco Colapinto; U23A, U25A.
  - JBM23 — KICK Sauber F1 Team (#24), Zhou Guanyu; U21A, U25A.
  - JBM25 — McLaren Formula 1 Team (#81), Oscar Piastri; U24A.
  - JBM14 — Visa Cash App RB Formula One Team (#22), Yuki Tsunoda; U30A, U32A.
  - JBM16 — Mercedes-AMG PETRONAS Formula One Team (#44), Lewis Hamilton; U29A, U32A.
  - JBM18 — Mercedes-AMG PETRONAS Formula One Team (#63), George Russell; U29A, U31A.
  - JBM24 — Visa Cash App RB Formula One Team (#30), Liam Lawson; U29A, U30A.
- Every listed 2025 car uses wheel type RRPPZ. The source explicitly records multiple stand codes for some Toy #s.
- Where supplied, chassis/model strings include A524, VF-24, RB20 and FW46. Several rows name only the team and racing number; do not infer a chassis designation from team/year alone.

### 2026 page
- Four individual-car tables contain **20 driver-specific releases**, grouped 5 + 5 + 5 + 5:
  - JKD78 — MoneyGram Haas F1 Team (#31), Esteban Ocon; U43A.
  - JKD79 — Visa Cash App Racing Bulls Formula One Team (#30), Liam Lawson; U43A.
  - JKD80 — Mercedes-AMG PETRONAS Formula One Team (#63), George Russell; U42A.
  - JKD81 — McLaren Formula 1 Team (#81), Oscar Piastri; U43A.
  - JKD88 — McLaren Formula 1 Team (#4), Lando Norris; U43A.
  - JKD82 — BWT Alpine Formula One Team (#10), Pierre Gasly; V05A.
  - JKD83 — Oracle Red Bull Racing (#1), Max Verstappen; V05A.
  - JKD84 — KICK Sauber F1 Team (#27), Nico Hülkenberg; V05A.
  - JKD85 — Atlassian Williams Racing (#55), Carlos Sainz Jr.; V05A.
  - JKD89 — KICK Sauber F1 Team (#5), Gabriel Bortoleto; V05A.
  - JKD86 — Scuderia Ferrari HP (#44), Lewis Hamilton; V08A.
  - JKD87 — Aston Martin Aramco Formula One Team (#18), Lance Stroll; V14A.
  - JKD90 — MoneyGram Haas F1 Team (#87), Ollie Bearman; V14A.
  - JKD91 — Visa Cash App Racing Bulls Formula One Team (#6), Isack Hadjar; V14A.
  - JKD92 — Mercedes-AMG PETRONAS Formula One Team (#12), Kimi Antonelli; V14A.
  - JKD93 — Scuderia Ferrari HP (#16), Charles Leclerc; V30A, V26A.
  - JKD94 — BWT Alpine Formula One Team (#43), Franco Colapinto; V30A.
  - JKD95 — Oracle Red Bull Racing (#22), Yuki Tsunoda; V30A.
  - JKD96 — Atlassian Williams Racing (#23), Alex Albon; V30A.
  - JKD97 — Aston Martin Aramco Formula One Team (#14), Fernando Alonso; V30A.
- Every listed individual car uses RRPPZ. Stand codes vary by release group.
- Three additional tables list **10 team-branded products**, one per team, without a Driver column: JMM91 McLaren; JMM93 Mercedes-AMG PETRONAS; JMM94 Visa Cash App Racing Bulls; JMM95 MoneyGram Haas; JMM92 KICK Sauber; JMM97 Oracle Red Bull Racing; JMM98 Atlassian Williams; JMM96 BWT Alpine; JMM99 Scuderia Ferrari HP; JMN00 Aston Martin Aramco. These are distinct from driver-specific car rows and should not be assigned a pilot without evidence.
- A separate product row JRB39 has fields for Notes, Cover, Inside Cover, Display and Back but no descriptive value in Notes in the extracted table.
- JRB40 is a Formula One Podium Set; listed contents are McLaren MCL39 (#4), Red Bull RB21 (#1), McLaren MCL39 (#81). This is a multi-product/set relationship, not a single casting.
- The page labels its year navigation “2025 • 2026 • 2027”; this is navigation context, not evidence that a 2027 release table is present in this file.

### Cross-year structural observations
- The `Driver` column is explicit source data and must be preserved as a first-class relationship, not parsed permanently out of `Casting Name`.
- Racing number is distinct from Hot Wheels Toy #. For example JBM09 is the toy identifier while #31 is the represented car's racing number.
- A team can have multiple individual releases in one year, and a driver/team pairing can change across seasons. Treat driver participation as season/context-specific, not as a permanent attribute of a team or casting.
- Team-branded products without a driver and the Podium Set demonstrate that the assortment contains product types beyond individual driver-specific cars.
- Preserve original team names exactly as printed per year; names such as Visa Cash App RB and Visa Cash App Racing Bulls, or Williams Racing and Atlassian Williams Racing, may reflect naming changes and should not be normalized into one historical string.


## Pro Racing (1997–2005) and Basic Pro Racing Series

**Sources:** archived year pages in `Modern Special Series/Pro Racing/`; Fandom revisions: 1997 783371, 1998 764854, 1999 801821, 2000 809610, 2001 792684, 2002 765107, 2003 783974, 2004 773614, 2005 801554, Basic Pro Racing Series 815908. Status: **Observation** from Fandom archive, not independently verified.

### Overall structure
- The yearly pages are not uniform annual checklists. They contain multiple tables grouped by release program, packaging/promo channel, wheel configuration, special paint scheme, track/race event, and sometimes non-car products.
- The data schema changes over time. 1997–2000 pages commonly record casting, team/number, primary sponsor, base/body material, interior, wheel type, Toy #, country, notes and images. From 2001 onward, many tables instead use Team number, Team/sponsor label, Wheels, Series and photo/status fields; item/Toy # is often absent.
- Do not equate a table row with a unique casting or a unique physical release. The same Toy # can recur with different facing/grille/spoiler/paint/packaging notes, and identical cars can be cross-listed in several annual tables/programs.
- The number in Team / Number is a racing number, not a Mattel Toy #. The sponsor/team label is not necessarily the driver name.

### 1997
- The main first table has 28 data rows, including duplicate Toy # entries with variation notes, and several unreleased concepts (e.g. Kranefuss-Haas #37, Neal Motorsports #91, Buz McCall Racing #96 marked NEVER RELEASED in the packaged/loose photo fields).
- Toy # examples: 17408 Morgan-McClure #4, 17407 Hendrick #5, 17411 Roush #6, 17409 Petty #43, 17580 PE2 #44, 17414 Roush #99.
- Explicit differences include car facing direction, grille, spoiler, bumper, decal/autograph and card variation. These are release/variant-level notes, not new casting identities by default.
- Other tables repeat many of the same cars as 1st Edition/Short Track listings, and include a Ford F-150 Irvan-Simo Racing #28 entry (Toy #18631) with plastic base, distinct from the metal-base stock cars.

### 1998
- Multiple separate tables cover annual releases, Preview/1st Edition, Short Track, promo/team listings, and Tool Box products. The page has many repeated entries and incomplete Toy # fields.
- The Team n° / Team / Year # / Series table lists 1998 team labels such as Target #4, Walker #5, and LCI #31; a separate table lists K-mart Havoline #6 and K-mart Duracell #11.
- Tool Box is a separate product/casting category with its own team/sponsor-decorated releases; do not model it as a car.
- At least one table lists Pontiac Grand Prix and Dodge Ram releases with body color and wheel type but no explicit Toy # on every row.

### 1999
- The year page contains NASCAR stock cars plus separate Daytona 500, Hall of Fame, Grand National, Toy Story 2, Tee'd Off, Formula 1 and Tool Box groupings.
- An explicit Formula 1 table lists McLaren Mercedes MP4-14 #1 (Mobil 1, Mika), MP4-14 #2 (Mobil 1, David), and MP4-13 #8 (Mobil 1). “Mika” and “David” are source text fragments, not yet normalized full driver identities.
- Hall of Fame and other special tables include castings whose sponsor/number details are different from ordinary annual stock-car releases. A 1999 note distinguishes Ford Taurus Stocker #26 from the similar Toy Story 2 Set car.
- Tee'd Off entries reuse NASCAR team/sponsor liveries on a different casting. This is a casting-level distinction despite shared team/number/sponsor concepts.
- Preserve source uncertainty such as “(Scandia)?” and rows with missing Toy #.

### 2000
- The main table contains 32 data rows and records numerous NASCAR castings, teams, numbers, sponsors, materials, wheels, Toy #s and countries.
- The page separately lists Petty Enterprises #44 Hot Wheels cars with race/track-specific sponsor text (Darlington, Talladega, California, Michigan, Daytona, Watkins Glen, Phoenix, Homestead-Miami). These should be modeled as event/track livery or promotional variants, not separate teams or drivers.
- Some rows explicitly distinguish alternate liveries and set exclusives, e.g. Petty Enterprises #44 Toy #50452 only in Commemorative Racing 4-Pack.
- A row may have a driver/trading card association, such as the Kenny Wallace Trading Card note on Andy Petree Racing #55, but this is not equivalent to a dedicated Driver column.
- Multiple Toy #s can exist for same team-number livery across different program/table contexts; cross-listing notes explicitly say “Car identical to the one in 2000 Pro Racing Main Series”.

### 2001
- The page is primarily a set of compact tables using Team n° / Team / Wheels / Series / Photo, with several release categories: Pro Racing, Pit Board, Promo, Treasure Hunt, Roush Racing Commemorative and others.
- Explicit unreleased status appears in a table: #45 Georgia Pacific marked NEVER RELEASED. Photo/status values must be preserved as status evidence, not treated as an actual released product.
- Pit Board, Treasure Hunt and other table categories are not necessarily the same physical product format as a standard car.
- There are separate wheel configurations (5SP, MGW, N/A, BW, GYERR, LW, ORSB, 3SP, DDRR, etc.). Preserve the source's raw wheel codes; do not normalize without a wheel-code reference.
- A “Campeanato McCormack” entry and other unusual labels should be retained verbatim pending clarification.

### 2002
- The page includes several standard Pro Racing wheel groups plus Treasure Hunt, baggie, sticker, promo, Daytona Set-UP and M&M's Campaign tables.
- Explicit NEVER RELEASED rows include #32 Tide, #97 Sharpie, #25 Marines, #36 M&Ms and #43 STP in the relevant 5SP tables.
- Treasure Hunt rows identify race/track names rather than driver/team numbers (e.g. Daytona, Darlington, Talladega, California, Watkins Glen, Phoenix, Kansas, Homestead Miami); this is an event/venue relationship.
- Notes distinguish prototypes and production wheel variants, e.g. #4 Kodak “GYERR (Prototype is a GYERR R)”, and cross-year repeats such as “Same as 2001 version”.
- M&M's campaign rows include several repeated #36 sponsor/deco records. Do not deduplicate solely on team number and sponsor.

### 2003
- This page makes the driver relationship explicit in one special table, **Pro Racing Luxury Rides**, where sponsor/team label and driver are both printed: examples include #4 Kodak “Mike Skinner”, #6 Pfizer “Mark Martin”, #10 Nesquik “Scott Riggs”, #10 Valvoline “Johnny Benson”, #12 Alltel “Ryan Newman”, #17 DeWalt “Matt Kenseth”, #21 Motorcraft “Ricky Rudd”, #32 Tide “Ricky Craven”, #36 M&M's “Ken Schrader”, #43 Cheerios “John Andretti”, #43 STP “Richard Petty”, #45 Brawny/Sprint “Kyle Petty”, #97 Sharpie/Rubbermaid “Kurt Busch”, #99 Citgo “Jeff Burton”.
- This is strong evidence that driver identity can be represented separately from the team/sponsor and car number. The same number can have different driver representations: #10 Nesquik/Scott Riggs and #10 Valvoline/Johnny Benson; #43 Cheerios/John Andretti and #43 STP/Richard Petty.
- Other tables include Recreational Series, Race Day, Color Changer, Special Paint Scheme, Wrenchin' & Racing, Stockerz and promos. Suffixes such as 12A/43A identify source-listed product/team-number forms; their meaning needs confirmation.
- Some tables mark rows NEVER RELEASED, e.g. #99 Citgo in the Recreational Series table.
- A 2003 Champions DeWalt #17 entry and related 2003 Champion items are separate commemorative decoration/program entries, not automatically separate real-world race entries.

### 2004
- The page's table structure uses Item Number, Team number, Team, Wheels, Series and Photo. Item Number is frequently blank, with some populated values such as G9276 and G9290.
- Categories include Race Day, Artist Collection, Showcase, Color Changer, Chase for the Cup, Justice League, Test Track, Alternative Paint Scheme and Treasure Hunt.
- Some Justice League entries combine team-number references with character names (e.g. Batman, The Flash, Wonder Woman, Superman, Green Lantern). These are licensed decorative variants, not driver names.
- A #6 entry appears under multiple sponsors (Viagra, Oscar Mayer, Pfizer) and product programs; #21 likewise has multiple liveries (Motorcraft, US Air Force, Rent-A-Center). The same number is not sufficient to infer a unique driver or vehicle identity.
- STOCKERZ is a separate table/category and should not be collapsed into the standard Race Day release table.

### 2005
- Three compact tables list Race Day, Cars Movie Promo and Alternative Paint Scheme entries. Examples include #10 Valvoline Cars Movie Promo, #12 Alltel Race Day, #43 Plymouth/Cheerios, #45 GP Brawny, #6 Pfizer, #16 National Guard, #17 DeWalt, #21 Motorcraft, #97 Sharpie and #99 Office Depot.
- The source's “Team #” and “Team” fields do not provide a dedicated driver column; avoid assigning drivers based on external assumptions without corroborating source evidence.
- The year page appears much more compact than earlier Pro Racing pages and may not represent every release channel or product type.

### Basic Pro Racing Series
- The Basic page contains multiple historically distinct groups, not just one basic NASCAR set. It includes early NASCAR stock cars with plastic bases and GYE10SP wheels; 1998-related headlight/casting notes; a 1997-era Indy/CART group with Reynard 97L #5/#8 and Lola T97 #31 (Walker/Shell/LCI); pace cars and commemoratives; later GP-2009 Formula 1 cars; and many further NASCAR stocker/promotional entries.
- The 1997-era Indy/CART rows include Toy #19117 Reynard 97L #5 Walker, #19116 Reynard 97L #8 Shell, and #19119 Lola T97 #31 LCI. These should be linked to real racing entries only after driver/team/chassis confirmation.
- A separate GP-2009 group includes McLaren #1, Ferrari #3 and HSBC #16 liveries. Do not assume these are the same real-world F1 season or chassis as the 1999 Formula 1 rows without corroboration.
- Basic page entries include multiple material/base and wheel configurations. “Basic” is a source grouping, not proof of a single product type or one coherent racing season.

### Cross-cutting data observations
- Store series/year, source table heading/category, release channel, casting, Toy #/Item Number, racing number, team/sponsor string, wheel code, base/material, interior, country, raw notes and release status separately.
- Represent driver as an optional, independently sourced relationship to a racing entry/season. A driver can be explicitly printed (e.g. 2003 Luxury Rides), hinted by source labels (e.g. 1999 “Mika”/“David”), or absent. Do not promote hints into verified driver identities.
- Team/sponsor is a compound source string in many tables. Preserve raw value and parse into separate team, sponsor, event and driver references only when evidence supports each component.
- Track/venue names, charity rides, movie promotions, superhero names and sponsor campaigns are distinct contexts, not teams or drivers.
- Keep unreleased/prototype/unknown Toy # records; they are useful archive evidence but must not be counted as confirmed retail releases.
