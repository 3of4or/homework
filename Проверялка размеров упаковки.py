print('Введите ширину, см')
width = int(input())
print('Введите длину, см')
length = int(input())
print('Введите высоту, см')
height = int(input())
if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif length > 200:
    print('Ищите упаковку для лыж')
elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
    print('Коробка №2')
else:
    print('Коробка №3')