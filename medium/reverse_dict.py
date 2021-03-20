"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(some_dict: dict) -> dict:
    new_dict = {some_dict[new_value]: new_value for new_value in some_dict}
    return new_dict


print(reverse_dict({1: 's', 2: 'd', 3: 'f'}))


# some_dict = {1: 's', 2: 'd', 3: 'f'}
# for i in some_dict:
#     print(some_dict[i])
