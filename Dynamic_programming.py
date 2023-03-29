# Тема довольно сложная, поэтому я изложу кратко основные моменты, подробности лучше искать в книге или в поисковике

# Задача о рюкзаке:
# Есть рюкзак в котором надо унести товары весом до 4 фунтов
# Надо положить в рюкзак максимально дорогой набор предметов(с учетом вместимости рюкзака в 4 фунта)
# Какие вещи есть: магнитофон(4 фунта, 3000$), ноутбук(3 фунта, 2000$), гитара(1 фунта, 1500$),

# Стоит начинать с подрюкзаков(от 1 фунта и доходить до 4 фунтов)
# Построить таблицу(строка гитара), где столбцы это размеры рюкзака(от 1 до 4), а строки это предметы
# Выбирать, что класть в рюкзак стоит из тех вещей которые мы проверяем или проверяли до этого


# - Динамическое программирование применяется для оптимизации какой-либо характеристики при
# заданных ограничениях. В задаче о рюкзаке требуется максимизировать стоимость отобранных вещей с ограничением
# по вместимости
# рюкзака.
# - Динамическое программирование работает только в ситуациях, в которых задача может быть разбита на автономные задачи,
# независящие друг от друга
# - В каждом решении на базе динамического программирования строится таблица
# - Значения ячеек таблицы обычно соответствуют оптимизируемой характеристике. Для задачи о рюкзаке значения
# представляли общую стоимость товаров
# - Каждая ячейка представляет подзадачу, поэтому мы должны подумать о том, как разбить задачу на НЕЗАВИСИМЫЕ друг от
# друга подзадачи
# - Не существует единой формулы для вычисления решений методом динамического программирования
# - Динамическое программирование предусматривает что мы либо мы берем предмет либо нет, брать половину мы не можем

