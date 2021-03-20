"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 2
next(tn_gen) -> 6
next(tn_gen) -> 24
"""


def triangular_numbers(n):
    tn = 0
    for i in range(n):
        tn = i * (i + 1) * 1 / 2
        yield print(int(tn))
    pass


tn_gen = triangular_numbers(10)


next(tn_gen)
next(tn_gen)
next(tn_gen)
next(tn_gen)
next(tn_gen)
next(tn_gen)
next(tn_gen)


