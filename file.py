def z1():
    from PIL import Image

    image = Image.open(r"Z:\1-мд-21\Воронков Никита\3\Image\priroda.jpg")

    left = 0
    top = 300
    right = image.width
    bottom = image.height

    cropped_image = image.crop((left, top, right, bottom))

    cropped_image.save(r"Z:\1-мд-21\Воронков Никита\3\Image\priroda1.jpg")



def z2():
    from PIL import Image
    праздники = {
        "Новый год": r"Z:\1-мд-21\Воронков Никита\3\Image\ng.jpg",
        "Рождество": r"Z:\1-мд-21\Воронков Никита\3\Image\ros.jpg",
        "8 Марта": r"Z:\1-мд-21\Воронков Никита\3\Image\8marta.jpg"
    }


    праздник = input("Введите название праздника: ")
    for key in праздники:
        if key == праздник:
            print("Открытка загружается")
            y = Image.open(праздники[key])
            y.show()




def z3():
    from PIL import Image, ImageDraw, ImageFont

    праздники = Image.open(r"Z:\1-мд-21\Воронков Никита\3\Image\ng.jpg")
    Imgdraw = ImageDraw.Draw(праздники)
    x = input("Введите имя: ")
    txt = str(x) + ', поздравляю! '
    font = ImageFont.truetype("Roboto-Black.ttf", size=70)
    y = Imgdraw.textlength(txt, font=font)
    z = праздники.size
    w = (z[0] // 3) - (y // 3)
    Imgdraw.text((w, 20), txt, font=font, fill=("#000000"))
    праздники.save(r"Z:\1-мд-21\Воронков Никита\3\Image\ng11.jpg")
    праздники.show()


z3()