"""
Написать функцию bang, которая печатает "Boom"

Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


# def bang():
#     print('Boom')
#
#
# def repeat_n_times(func, n=3):
#     for i in range(n):
#         def wrapper():
#             result = func()
#             return result
#     return wrapper
#
#
# # dec_obj = repeat_n_times(bang)
# #
# # print(dec_obj())
# @repeat_n_times
# def bang():
#     print('Boom')
#
#
# # print(bang())
'''
def decorator(n):
    def inner_dec(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return inner_dec


@decorator(3)
def bang():
    print('Boom')

'''


def bang():
    print('Boom')


def decorator(func):
    n = 3
    for i in range(n):
        def wrapper():
            return func()


dec_func = decorator(bang)
print(dec_func())




