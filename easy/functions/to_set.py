"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(some_list: list):
    some_tuple = tuple(some_list)
    result = f'The length of this tuple is {len(some_tuple)}'
    return some_tuple, result


print(to_set([1, 2, 3, 'b']))







