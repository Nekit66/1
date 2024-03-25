def z1():
    a = [1, 2, 3, 4, 5]
    b = int(input('Введите число: '))
    if b in a:
        print("Список: " , a)
        print('Число пользователя: ' , b)
        print('Такое число есть в списке')
    else:
        print("Список: " , a)
        print('Число пользователя: ' , b)
        print('Такого числа нет в списке')



def z2():
    a = [1, 2, 3, 4, 5, 5, 6]
    b = []

    for i in a:
        if a.count(i) > 1 and i not in b:
            b.append(i)

    if b:
        print("Повторяющиеся элементы в списке:", b)
    else:
        print("Нет повторяющихся элементов в списке.")




def z3():
    dni = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    a = int(input("Сколько выходных дней на неделе вы хотите? "))
    if a < 0 or a > len(dni) // 2:
        print('Некорректный ввод!')
    else:

        weekends = dni[-a:]
        workdays = dni[:-(a)]

        print("Ваши выходные дни:", ', '.join(weekends))
        print("Ваши рабочие дни:", ', '.join(workdays))



def z4():
    group1 = ['Петров', 'Сидоров', 'Иванов', 'Козлов', 'Смирнов', 'Морозов', 'Васильев', 'Зайцев', 'Попов', 'Лебедев']
    group2 = ['Кузнецов', 'Новиков', 'Макаров', 'Алексеев', 'Соловьев', 'Волков', 'Ломакин', 'Козлов', 'Иванов',
              'Григорьев']

    sports_team = tuple(group1[:5] + group2[:5])


    print("Список студентов в группе 1:", group1)
    print("Список студентов в группе 2:", group2)
    print("Спортивная команда:", sports_team)


    print("Длина спортивной команды:", len(sports_team))


    sorted_team = sorted(sports_team)

    ivanov_count = sports_team.count('Иванов')
    print("Студент 'Иванов' включен в команду:", 'Иванов' in sports_team)
    print("Количество вхождений фамилии 'Иванов' в команду:", ivanov_count)


z2()