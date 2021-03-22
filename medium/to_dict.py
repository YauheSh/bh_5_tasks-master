"""
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и
возвращает словарь, в котором каждый элемент списка является и ключом и
значением. Предполагается, что элементы списка будут соответствовать
правилам задания ключей в словарях.
"""


def to_dict(lst: list) -> dict:
    some_dict = {}
    for i in range(len(lst)):
        some_dict.update({lst[i]: lst[i]})
    return some_dict


print(to_dict([1, 2, 5, 9, 13]))
