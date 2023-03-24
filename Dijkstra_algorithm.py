# Поиск в ширину, чтобы найти путь с минимальным количеством сегментов
# Алгоритм Дейкстры, используется для нахождения пути от начальной точки к конечной за кратчайшее время

# Алгоритм Дейкстры состоит из ЧЕТЫРЁХ шагов:
# 1. Найти узел с наименьшей стоимостью(то есть узел, до которого можно добраться за минимальное время)
# 2. Обновить стоимость соседей этого узла
# 3. Повторять, пока это не будет сделано для всех узлов графа
# 4. Вычислить итоговый путь

# Шаг 1. Найти узел с наименьшей стоимостью
# Направляемся к узлу с наименьшей стоимостью, при это мы считаем что неизвестна стоимость остальных узлов,
# а время достижения до конечной точки бесконечно

# Шаг 2. Обновить стоимость соседей этого узла
# Если мы обнаруживаем, что обнаружили более коротки маршрут к узлу(раньше для перехода к нему требовалось больше времени)
# или например более короткий маршрут к конечному узлу(с бесконечности он становится на наше обнаруженное значение),
# то обновляем его стоимость

# Шаг 3. Повторять, пока это не будет сделано для всех узлов графа
# Повторять, пока не сделаем это для каждого узла графа.
# Алгоритм Дейкстры должен выполнятся для каждого узла(выполнять для конечного узла не надо)

# Шаг 4. Вычислить итоговый путь
# Об этом позже

# Терминология:
# Когда мы работаем с алгоритмом Дейкстры, с каждым ребром графа связывается число, называемое ВЕСОМ
# Графы с ВЕСОМ называются ВЗВЕШЕННЫЕ ГРАФЫ, для вычисление кратчайшего пути в них используется ПОИСК В ШИРИНУ
# Графы без ВЕСА называются НЕВЗВЕШЕННЫЕ ГРАФЫ, для вычисление кратчайшего пути в них используется АЛГОРИТМ ДЕЙКСТРЫ
# В графах могут присутствовать ЦИКЛЫ(можем начать с некоторого узла, перемещаться по графу и вернуться в тот же узел). При
# это обход по циклу НИКОГДА НЕ БУДЕТ КРАТЧАЙШИМ

# Ребра у которых отрицательное значение называются РЕБРА С ОТРИЦАТЕЛЬНЫМ ВЕСОМ, при этом алгоритм Дейкстры НЕ ПРИМЕНЯЕТСЯ
# ПРИ НАЛИЦИИ РЕБЕР С ОТРИЦАТЕЛЬНЫМИ РЕБРАМИ!!!


# Реализация Алгоритма Дейстры
# У нас есть граф в форме ромба, деленного вертикально по центру
# (от начала до А(6), от начала до Б(2), от А до конец(1), от B до A(3), от Б до конец(5))

# Для реализации этого примера нам нужны 4 хеш таблицы:
# 1. Граф
# 2. Стоимость
# 3. Родители
# 4. Обработанные узлы

# Таблица 1
# Создаем граф(словарь)
graph = {}

# Создаем вложенный словарь "start" Указываем соседей для start с весом ребер(с помощью вложенных словарей)
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# Создаем соседей с весом для других узлов
graph["a"] = {}
graph["a"]["finish"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5

# У конечного узла нет соседей
graph["finish"] = {}

# Для получения всех соседей для start можем использовать
print(graph["start"].keys())
# Для получения веса ребер от start до a
print(graph["start"]["b"])


# Таблица 2
# Теперь создаем словарь со стоимостью

# Переменная бесконечности
infinity = float("inf")

# Словарь для стоимости ребер
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

# Таблица 3
# Создаем словарь для родителей узлов
perents = {}
perents["a"] = "start"
perents["b"] = "start"
perents["finish"] = None

# Таблица 4
# Создаем словарь для обработанных узлов
processed = []



# Теперь функция для поиска наименьшего веса
def find_lowest_cost_node(costs):
    # Самая низкая стоимость
    lowest_cost = float("inf")
    # Узел с наименьшей стоимостью
    lowest_cost_node = None
    # Перебераем все узлы
    for node in costs:
        # Стоимость текущего узла
        cost = costs[node]
        # Если стоимость наименьшая из уже виденных и текущий узел не был еще обработан
        if cost < lowest_cost and node not in processed:
            # Стоимость наименьшего узла становится новой наименьшей стоимостью
            lowest_cost = cost
            # Текущий узел становится новым узлол с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


# Функция для поиска наименьшего пути
def find_lowest_way(costs):
    # Найти УЗЕЛ с наименьшим весом среди необработанных(node это узел с наименьшей стоимостью) из таблицы стоимость(costs)
    # При первом цикле это будет узел "b"
    node = find_lowest_cost_node(costs)
    # Если все узлы обработаны, цикл while завершен
    while node is not None:
        # Получить СТОИМОСТЬ узла наименьшим весом среди необработанных из таблицы стоимости(costs)
        # При первом цикле это будет вес узла "b" == 2
        cost = costs[node]
        # Получить СОСЕДЕЙ этого узла из графа(graph)
        # При первом цикле это соседями узла "b" будут "a" и "finish"
        neighbors = graph[node]
        # Перебрать всех соседей текущего узла
        # При первом цикле перебираем соседей узла "b", а именно "a" и "finish"
        for n in neighbors.keys():
            # Вычисляем СТОИМОСТЬ от текущего узла ДО его СОСЕДЕЙ
            # При первом цикле это будет стоимость B плюс расстояние от B до A (2 + graph['b']['a'] т.е. 3)
            new_cost = cost + neighbors[n]
            # Если к соседу можно добраться быстрее через текущий узел
            # Сравниваем стоимость перехода со старыми значениями
            # При первом цикле это новая стоимость будет 5, а старая(из таблицы costs) 6
            if costs[n] > new_cost:
                # Обновить стоимость для этого узла
                # При первом цикле мы нашли, более короткий путь(5 вместо 6), и обновляем значение в таблице costs["a"] = 5
                costs[n] = new_cost
                # Этот узел становится новым родителем для соседа
                # При первом цикле новым родителем для A становится B(parents['a'] = b)
                perents[n] = node
        # Узел помечается как обработанный
        processed.append(node)
        # Найти следующий узел для обработки и повторить
        node = find_lowest_cost_node(costs)
    return print(f'Кратчайщий путь составляет : {costs["finish"]}')

find_lowest_way(costs)