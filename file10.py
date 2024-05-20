def z1():
    import json

    with open('products.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

    products = data['products']

    for product in products:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        print("В наличии") if product['available'] else print("Нет в наличии")
        print()



import json

def z2():
    with open('products.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_product = {
        "name": input("Введите название товара: "),
        "price": input("Введите стоимость товара: "),
        "available": input("Товар в наличие?(True/False): ").lower() == "true",
        "weight": int(input("Введите вес товара: "))
    }
    data["products"].append(new_product)
    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    with open('products.json', 'r', encoding='utf-8') as file:
        new_data = json.load(file)

    for product in new_data['products']:
        print(f'Название: {product["name"]}'
              '\n' f' Цена: {product["price"]}'
              '\n' f' Вес: {product["weight"]}')
        if product['available']:
            print("В Наличии")
        else:
            print('Нет в наличии')


def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    ru_en = {}
    for line in lines:
        eng_word, ru_tr = line.strip().split('-')
        for ru_word in ru_tr.split(','):
            if ru_word.strip() not in ru_en:
                ru_en[ru_word.strip()] = [eng_word]
            else:
                if eng_word not in ru_en[ru_word.strip()]:
                    ru_en[ru_word.strip()].append(eng_word)
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for key in sorted(ru_en.keys()):
            trans = ','.join(sorted(ru_en[key]))
            file.write(f'{key}-{trans}\n')

z3()

