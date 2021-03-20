"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def num_sum(n, result=0):
    if n == 0:
        return result
    else:
        result += (n % 10)
        return num_sum(n // 10, result)


print(num_sum(2334))
