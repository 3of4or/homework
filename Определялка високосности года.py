print('Определялка високосности года\nВведите год:')

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, '- високосный год')

if (year < 0) or (year > 2999) :
    print('Не балуйся с годами')

else :
    print(year, '- не високосный год')