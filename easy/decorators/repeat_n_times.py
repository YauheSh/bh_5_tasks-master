"""
Написать функцию bang, которая печатает "Boom"

Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


def decorator(n):
    def inner_dec(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return inner_dec


@decorator(3)
def bang():
    print('Boom')


bang()





