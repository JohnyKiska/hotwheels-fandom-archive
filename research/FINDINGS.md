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
