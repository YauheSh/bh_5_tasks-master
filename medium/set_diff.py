"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(first: set, second: set, third: set, symmetric=False):
    if symmetric is False:
        print(first.difference(second).difference(third))
    else:
        print(first.symmetric_difference(second).symmetric_difference(third))


first_set = {1, 9, 2, 8}
second_set = {2, 8, 3, 4, 5}
third_set = {6, 7, 11, 42}
set_diff(first_set, second_set, third_set, symmetric=True)
