def z1():
    a = {'Россия': 'Москва', 'Бразилия': 'Бразилиа', 'Германия': 'Берлин'}

    for key, value in a.items():
        print(key + ': ' + value)

    print(a.get(input('Введите страну, столицу которой хотите узнать: ')))

    s = {country: a[country] for country in sorted(a)}

    for country, capital in s.items():
        print(country + " – " + capital)


def z2():
    a = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }


    def q(word):
        b = 0
        for letter in word.upper():
            if letter in a:
                b += a[letter]
        return b


    word = input("Введите слово: ")


    c = q(word)
    print(f"Стоимость слова '{word}' в игре 'Эрудит' составляет: {c} очков.")

z2()
