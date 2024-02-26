# N = int(input('Введите какое количество слов будет введено: '))
#
# b = 1
#
# c = ""
#
#
# for w in range(1, N + 1):
#     a = input("Введите слово: ")
#     c = c + " " + a
#
# print(c)







# c = ""
# a = ''
#
# while a != "stop":
#     a = input("Введите слово: ")
#     c = c + " " + a
#
# print(c)




# a = input('Введите слово: ')
# if 'ф' in a:
#     print('Ого! Это редкое слово!')
# else:
#     print('Эх, это не очень редкое слово...')


import random

n = 0
f = 0
a1 = 0
a2 = 0
o = 0

while f < 3:
    a1 = random.randint(0, 10)
    a2 = random.randint(0, 10)
    o = a1 + a2
    h = int(input(f'{a1} + {a2} ='))
    if o == h:
        print('Правильно!')
        n += 1
    else:
        print('Ответ неверный')
        f += 1
print(f'Игра окончена. Правильных ответов: {n}')





