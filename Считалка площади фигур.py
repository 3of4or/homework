print('Введите тип фигуры')
shape = input().lower()
if shape == 'круг':
    import math
    print('Введите радиус')
    rad = int(input())
    S = round(math.pi*(rad**2), 2)
    print('Площадь круга:', S)

if shape == 'треугольник':
    print('Введите сторону A')
    A = int(input())
    print('Введите сторону B')
    B = int(input())
    print('Введите сторону C')
    C = int(input())
    p = (A+B+C)/2
    S = round((p*(p - A) * (p -B) * (p - C))**(0.5), 2)
    print('Площадь треугольника:', S)

if shape == 'прямоугольник':
    print('Введите сторону A')
    A = int(input())
    print('Введите сторону B')
    B = int(input())
    S = round(A * B, 2)
    print('Площадь прямоугольника:', S)