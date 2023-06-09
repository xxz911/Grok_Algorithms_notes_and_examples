# Деревья

# Вернемся к примеру с бинарным поиском. Когда пользователь вводит своё имя на сайте Facebook,
# сайт должен проверить содержимое большого массива. Мы выяснили,
# что для нахождения значения в массиве быстрее всего использовать бинарный поиск.
# Однако тут есть проблема, каждый раз когда новый пользователь регистрируется, придется заново сортировать массив
# (бинарный поиск работает только с отсортированным массивом).
# Намного удобнее было бы вставить пользователя в правильную ячейку,
# чтобы потом не пришлось сортировать массив.

# Именно эта идея заложена в основу структуры данных БИНАРНОГО ДЕРЕВА ПОИСКА

# Для каждого узла все узлы ЛЕВОГО поддерева содержат МЕНЬШЕГО значения, а все узлы ПРАВОГО поддерева - БОЛЬШИЕ значения
# Бинарные деревья поиска работают быстрее, по сравнению с бинарным поиском, в вставке и удалении, однако
# они не поддерживают произвольный доступ, и быстродействие зависит от сбалансированности дерева
# Бинарные деревья поиска обычно используются для хранения информации в базах данных


# Инвертированные индексы
# Допустим есть 3 веб страницы с простым содержанием
# - Первая страница (hi, there)
# - Вторая страница (hi, adit)
# - Третья страница (there, we, go)

# Построим хеш таблицу для этого содержимого, где ключами будет слово, а значения указывают на то, на какой странице
# находиться это слово
# Пользователь вводит в поисковике слово hi, мы смотрим на каких страницах встречается это слово и выводим эти страницы
# в результаты поиска
# Структура данных где хеш-таблица связывает слова с местами,
# в которых эти слова встречаются называется ИНВЕРТИРОВАННЫМ ИНДЕКСОМ


# Параллельные алгоритмы
# Связаны с масштабируемостью и обработкой больших объемов данных(прирост может быть не линейным)
# так, если у нас не одно ядро в компьютере, а два, то наш алгоритм не факт что заработает в два раза быстрее,
# на это есть несколько причин:
# 1. Затраты ресурсов на управление параллелизмом
# (разделяем массив на две части, обрабатываем и соединяем результаты в одни массив)
# 2. Распределение нагрузки(делим 10 задач пополам
# (одно ядро тяжелые задачи, второе ядро легкие) по итогу одно ядро выполнит задачу быстрее и будет простаивать,
# пока не решит задачи другое ядро)

# Одной из разновидности параллельных алгоритмов является РАСПРЕДЕЛЕННЫЕ АЛГОРИТМЫ
# Данный алгоритм хорошо работает когда нам надо выполнить большой объем работы и мы хотим сократить время выполнения
# Алгоритм MapReduce известный представитель семейства распределенных алгоритмов
# В основе лежат две простые идеи:
# 1. Функция map(распределяет работу компьютеров)
# 2. Функция reduce


# Алгоритмы SHA
# Одной из разновидностей хещ-функции составляет Алгоритм SHA, он получает строку и возвращает ее хеш-код
# Алгоритм SHA является хеш функцией, которая генерирует хеш-код, который представляет собой короткую
# строку. Хеш-функция для хеш-таблиц преобразует строку в индекс массива, когда SHA преобразует строку в другую строку
# Для каждой строки алгоритм SHA генерирует свой уникальный хеш-код
# SHA позволяет определить совпадают ли два файла, хеширование паролей(сами пароли не хранятся)
# Мы можем преобразовать строку в хеш код, но обратно хеш-код в строку не можем

# SHA хеширование является локально-чувствительным(если изменить один символ, сгенерируется совсем другой код)

# Если надо проверить, насколько хеш-коды похожи(их строки близки) используют Simhash
# (при незначительном различии между строками генерируется практически одинаковый код)


# Конец книги.
