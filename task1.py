# 1. Случайности не случайны.
# Дано: n - целое число.
#
# Задание: написать функцию-генератор, которая возвращает n дробных чисел из диапазона [0, n].
# Используйте функцию random.uniform для генерации случайных чисел.
#
# Пример:
#  list(f(3)), результат: [0.460552766096591, 2.6440795402868016, 0.3830553232366699]

from random import uniform


def generate_fractional_numbers(n):
    for _ in range(n):
        yield uniform(0, n)


print(list(generate_fractional_numbers(3)))
