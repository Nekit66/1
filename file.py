def z1():
    from pathlib import Path
    from PIL import Image

    input_dir = Path(r'Z:\1-мд-21\Воронков Никита\Image9\input_images')
    output_dir = Path(r'Z:\1-мд-21\Воронков Никита\Image9\output_images')

    output_dir.mkdir(parents=True, exist_ok=True)

    for file in input_dir.iterdir():
        if file.suffix in ['.jpg', '.png', '.bmp']:
            input_path = file
            output_path = output_dir / file.name

            image = Image.open(input_path)
            image = image.convert('L')
            image.save(output_path)

    print("Все изображения успешно обработаны!")


def z2():
    import os
    from PIL import Image

    input_dir = (r'Z:\1-мд-21\Воронков Никита\Image9\input_images')
    input_files = os.listdir(input_dir)

    output_dir = (r'Z:\1-мд-21\Воронков Никита\Image9\output_images')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in input_files:
        extension = os.path.splitext(file)[1]

        if extension.lower() in ['.jpg', '.png']:
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)

            image = Image.open(input_path)

            image = image.convert('L')

            image.save(output_path)

    print("Все изображения JPG и PNG успешно обработаны!")


def z3():
    import csv

    with open('file.csv', 'r', encoding='utf-8') as laba9:
        csv_reader = csv.reader(laba9, delimiter=',')

        total_cost = 0
        shopping_list = []
        for row in csv_reader:
            product = row[0]
            quantity = row[1]
            price = row[2]

            purchase_cost = float(quantity) * float(price)

            shopping_list.append(f"{product} - {quantity} шт. за {purchase_cost} руб.")

            total_cost += purchase_cost

    print("Нужно купить:")
    for item in shopping_list:
        print(item)

    print(f"Итоговая сумма: {total_cost} руб.")


z3()