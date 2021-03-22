"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list: list):
    new_list = []
    for i in range(len(some_list)):
        new_list.append(some_list[i])
        if new_list.count(new_list[i]) > 1:
            print(f"Число {some_list[i]} встречается несколько раз. Yes")
        else:
            print(f"Число {some_list[i]} встречается один раз. No")


list_of_number = [5, 2, 5, 2, 3, 1, 4]


yes_or_no(list_of_number)
