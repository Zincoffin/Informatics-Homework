#1
a = float(input())
b = float(input())
if b == 0:
    print('куда на ноль делить брат')
else:
    print(a / b)
#2
summa = int(input())
if summa > 20:
    print(f'стоимость составила {round(summa - (summa * 0.35), 2)}, ваша скидка 35%')
else:
    print('ноу мани ноу хани')
#3
a = int(input())
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if 1 <= a <= 12:
    if 9 <= a < 12:
        print(f'это {months[a]}, осень')
    elif 3 <= a < 6:
        print(f'это {months[a]}, весна')
    elif 6 <= a < 9:
        print(f'это {months[a]}, лето')
    else:
        print(f'это {months[a]}, зима')
else:
    print('такого месяца нет')