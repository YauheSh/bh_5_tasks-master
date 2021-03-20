"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(func_list: list, flor=0):
    for key, value in enumerate(func_list):
        if isinstance(value, list):
            line_print(func_list[key], flor+1)
        else:
            if flor == 0:
                print(key, value)
            elif flor == 1:
                print(f"\t {key} {value}")
            elif flor == 2:
                print(f"\t\t{key} {value}")


some_list = [1, 2, [1, 2, [5, 7], 3], 8]
line_print(some_list)
