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
