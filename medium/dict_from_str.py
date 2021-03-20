"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(some_str: str) -> dict:
    some_dict = {letter: some_str.count(letter) for letter in some_str}
    return some_dict


print(dict_from_str(STR_VAL))
