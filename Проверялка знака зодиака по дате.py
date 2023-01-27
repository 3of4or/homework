month = input("{blue}Введите месяц: {endcolor}".format(blue="\033[96m", endcolor="\033[0m")).capitalize()
day = int(input("{blue}Введите день: {endcolor}".format(blue="\033[96m", endcolor="\033[0m")))

if (month == 'Январь') or (month == '1') and 0 < day <32:
    if day > 19:
        print('Ваш знак зодиака: Водолей')
    else: print('Ваш знак зодиака: Козерог')    

elif (month == 'Февраль') or (month == '2') and 0 < day <29:
    if day > 18:
        print('Ваш знак зодиака: Рыбы')
    else: print('Ваш знак зодиака: Водолей')

elif (month == 'Март') or (month == '3') and 0 < day <32:
    if day > 20:
        print('Ваш знак зодиака: Овен')
    else: print('Ваш знак зодиака: Рыбы')

elif (month == 'Апрель') or (month == '4') and 0 < day <31:
    if day > 19:
        print('Ваш знак зодиака: Телец')
    else: print('Ваш знак зодиака: Овен')

elif (month == 'Май') or (month == '5') and 0 < day <32:
    if day > 20:
        print('Ваш знак зодиака: Близнецы')
    else: print('Ваш знак зодиака: Телец')

elif (month == 'Июнь') or (month == '6') and 0 < day <31:
    if day > 20:
        print('Ваш знак зодиака: Лев')
    else: print('Ваш знак зодиака: Близнецы')

elif (month == 'Июль') or (month == '7') and 0 < day <32:
    if day > 22:
        print('Ваш знак зодиака: Лев')
    else: print('Ваш знак зодиака: Рак')

elif (month == 'Август') or (month == '8') and 0 < day <31:
    if day > 22:
        print('Ваш знак зодиака: Дева')
    else: print('Ваш знак зодиака: Лев')

elif (month == 'Сентябрь') or (month == '9') and 0 < day <32:
    if day > 22:
        print('Ваш знак зодиака: Весы')
    else: print('Дева')

elif (month == 'Октябрь') or (month == '10') and 0 < day <31:
    if day > 22:
        print('Ваш знак зодиака: Скорпион')
    else: print('Ваш знак зодиака: Весы')

elif (month == 'Ноябрь') or (month == '11') and 0 < day <32:
    if day > 21:
        print('Ваш знак зодиака: Стрелец')
    else: print('Ваш знак зодиака: Скорпион')

elif (month == 'Декабрь') or (month == '12') and 0 < day <31:
    if day > 19:
        print('Ваш знак зодиака: Козерог')
    else: print('Ваш знак зодиака: Стрелец')

else: print('Я ещё не понимаю таких дат') 