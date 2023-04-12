from PIL import Image, ImageDraw, ImageFont
def z1():
    image = Image.open('dr.jpeg')
    cropped = image.crop((200,400,1450,2000))
    cropped.save('dr_new.jpeg')
    cropped.show()

def z2():
    holidays = {'Яблочный спас': 'ys.jpg',
                'День Ивана Купалы': 'ik.jpg',
                'День клоуна': 'dk.jpg',
                'День Рождения': 'dr.jpg',
                }
    a = input('Введите праздник: ')
    for key in holidays:
        if key == a:
            b = Image.open(holidays[key])
            b.show()

def z3():
    image = Image.open("dr.jpeg")
    idraw = ImageDraw.Draw(image)
    a = input('Введите имя: ')
    text = str(a) + ", поздравляю!"
    font = ImageFont.truetype("Srbija Sans.otf", size=130)
    b = idraw.textsize(text, font=font)
    c = image.size
    d = (c[0] // 2) - (b[0] // 2)
    idraw.text((d, 10), text, font=font, fill=('#ff0000'))
    image.save('dr_text.png')
    image.show()

z3()