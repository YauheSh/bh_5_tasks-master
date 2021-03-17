"""
Написать функцию bang, которая печатает "Boom"

Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


def bang():
    print('Boom')


def repeat_n_times(func, n=3):
    current = 1
    if current <= n:
        def wrapper():
            print('one')
            result = func()
            print('two')
            return result
    else:
        return
    return wrapper


# dec_obj = repeat_n_times(bang)
#
# print(dec_obj())
@repeat_n_times
def bang():
    print('Boom')


print(bang())

