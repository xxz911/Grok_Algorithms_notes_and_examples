# Для бинарного поиска массив должен быть отсортирован
# Бинарный поиск выполняется за ларифмитическое время O(Log n)
# (последовательный поиск за линейное время O(n))


def binar_search(list, item):
    # Границы текущего поиска
    low = 0
    high = len(list) - 1

# Поиск
    while low <= high:
        # Средний элемент
        mid = int((low + high) / 2)
        # Проверка среднего элемента
        guess = list[mid]

        # Значение найдено
        if guess == item:
            return mid
        # Много
        if guess > item:
            high = mid - 1
        # Мало
        else:
            low = mid + 1
    # Значения не существует
    return None

# Тест для бинарного поиска
def test(list, item):
    res = binar_search(list, item)
    if res == None:
        print("Нет совпадений")
    elif list[res] == item:
        print("Поиск сработал, индекс в списке : " + str(res))
    else:
        print("Тест не пройден")


list = [1, 3, 6, 9, 10, 11, 14, 15, 18, 20, 22, 23, 24, 26, 27, 28, 30]
test(list, 26)
