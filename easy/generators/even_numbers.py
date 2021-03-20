"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(n=1):
    for i in range(n):
        if i == 0:
            continue
        else:
            yield print(i * 2)


even_gen = get_even_number(10)


next(even_gen)
next(even_gen)
next(even_gen)
next(even_gen)
next(even_gen)
next(even_gen)

