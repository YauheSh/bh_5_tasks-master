"""
Написать генератор factorial, который возвращает подряд числа факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(n):
    fact = 1
    if n == 0:
        return fact
    else:
        for i in range(n):
            if i == 0:
                continue
            else:
                fact *= i
                yield fact


factorial_gen = factorial(10)


next(factorial_gen)
next(factorial_gen)
next(factorial_gen)
next(factorial_gen)
