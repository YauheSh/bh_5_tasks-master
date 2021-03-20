"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


def common_numbers(first: list, second: list) -> list:
    common_list = first + second
    return sorted(common_list, reverse=True)


print(common_numbers([4, 2, 3], [1, 2, 3]))

