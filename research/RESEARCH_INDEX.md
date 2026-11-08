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
