"""
Написать функцию calc_sum, которая принимает неограниченное количество целых
чисел и  возвращает их сумму

для расчета суммы можно воспользоваться функцией sum
"""


def calc_sum(*args):
    return sum(args)

print(calc_sum(1, 2, 3))


#если без SUM
#summa = 0
#for i in args:
#    summa += i
#   return summa


#print(calc_sum(1, 2, 3))

'''if __name__ == '__main__':
    some_values = []
    while True:
        value = input('Введите число:')
        if value == 'stop':
            break
            some_values.append(int(value))
    print(calc_sum(*some_values))
    '''


