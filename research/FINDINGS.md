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

### Ограничение источника
Страница `Modern Special Series/Hot Wheels Classics _ Hot Wheels Wiki _ Fandom.html` в архиве не содержит извлекаемых заголовков, параграфов или таблиц в сохранённом HTML; её нельзя считать исследованной по содержимому. Все остальные выводы выше — observations из архивных Fandom HTML, не независимая историческая верификация.
