#декоратор тройной
# def decorator(n):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             print('cod before')
#             result = func(*args, **kwargs)
#             print('cod after')
#             result += n
#             return result
#         return wrapper
#     return inner_decorator
#
# @decorator(2)
# @decorator(6)
# def some_function(n):
#     return n
#
#
# print(some_function(2))
#

# рекурсивная функция для опред факториала
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n
#
#
# print(factorial(5))


def triangle(n, current=1):
    if current <= n:
        print(str(current) * current)
        triangle(n, current + 1)

triangle(10)



