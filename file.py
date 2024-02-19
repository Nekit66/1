# 1
p = input('Введите пароль: ')
p1 = input('Повторите пароль: ')

if p == p1:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 2
def z2():
    p = int(input('Введите место: '))

    if p % 2 == 0 and p >= 1 and p <= 36:
        print('Купе верхнее')
    elif p % 2 == 1 and p >= 1 and p <= 36:
        print('Купе нижнее')
    elif p % 2 == 0 and p >= 37 and p <= 53:
        print('Боковое верхнее')
    elif p % 2 == 1 and p >= 37 and p <= 53:
        print('Боковое нижнее')
    else: print('ошибка')





# 3
g = input('Введите год: ')
if int(g) % 4 == 0 and int(g) % 100 != 0 or int(g) % 400 == 0:
    print('Год ' + g + ' високосный')
else:
    print('Это год не високосный')






# 4


def z4():
    x = input("Введите 1 цвет: ")
    y = input("Введите 2 цвет: ")
    if (x == 'красный' and y == 'синий') or  (y == "красный" and x == 'синий'):
        print('Фиолетовый')
    elif (x == "красный" and y == 'желтый') or  (y == "красный" and x == 'желтый'):
        print('Оранжевый')
    elif (x == "синий" and y == 'желтый') or  (y == "синий" and x == 'желтый'):
        print('Зелёный')
    else:
        print('ошибка')
z4()

