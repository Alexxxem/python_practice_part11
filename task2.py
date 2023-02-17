# 2. Ленивое объединение
# Дано: 2 списка произвольной длины.
#
# Задание: написать функцию, которая возвращает результат объединения этих списков.
# Используйте функцию itertools.chain.
#
# Пример:
#  list(f([1, 2], [3, 4])), результат: [1, 2, 3, 4]

from itertools import chain


def merge_lists(*lists):
    return chain(*lists)


numbers1 = [1, 2, 3]
numbers2 = [4, 5]
print(list(merge_lists(numbers1, numbers2)))
