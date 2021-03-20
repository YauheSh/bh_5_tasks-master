"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1:
        return True
    elif n % 2 == 1:
        return False
    else:
        if n // 2 == 0:
            return True
        else:
            return check_number(n // 2)


print(check_number(18))
