"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""
SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def multiply_dict_values(some_of_dict: dict):
    mult_num = 1
    for key, value in enumerate(some_of_dict):
            mult_num = mult_num * some_of_dict[value]
    return mult_num


print(multiply_dict_values(SOME_DICT))
