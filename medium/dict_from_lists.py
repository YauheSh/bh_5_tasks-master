"""
Написать функцию get_dict_from_lists, которая принимает 2 значения - 2 списка
одинаковой длины: LIST_1 и LIST_2.

Необходимо, чтобы функция составляла и возвращала словарь, у которого ключи -
элементы LIST_1, а значения - элементы LIST_2
"""
LIST_1 = [str(i) for i in range(20)]
LIST_2 = [i for i in range(20)]


def get_dict_from_lists(first: list, second: list) -> dict:
    some_dict = {first[i]: second[i] for i in range(len(first))}
    return some_dict


# def get_dict_from_lists(first: list, second: list) -> dict:
#     some_dict = {}
#     for i, value in enumerate(first):
#         some_dict[value] = second[i]
#     return some_dict


print(get_dict_from_lists(LIST_1, LIST_2))
