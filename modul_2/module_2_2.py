a = input('Введите число 1: ')
b = input('Введите число 2: ')
c = input('Введите число 3: ')
#
if a == b and a == c:
    print('Вы ввели 3 одинаковых числа.')
elif a == b or a == c or b == c:
    print('Вы ввели 2 одинаковых числа.')
else:
    print('Вы ввели 0 одинаковых чисел.')