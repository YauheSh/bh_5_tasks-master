"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    start_fib = 0
    sum_fib = 1
    if num_count == 0:
        raise ValueError(f'Введите значение больше 1')
    for i in range(num_count):
        start_fib, sum_fib = sum_fib, start_fib + sum_fib
        yield sum_fib


gen_fib_obj = fibonacci(5)


try:
    print(next(gen_fib_obj))
    print(next(gen_fib_obj))
    print(next(gen_fib_obj))
    print(next(gen_fib_obj))
    print(next(gen_fib_obj))
except ValueError as exc:
    print(f'{exc}')
