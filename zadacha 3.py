k1 = input('Введите колличество учеников класса 1: ')
k1 = int(k1)
k2 = input('Введите колличество учеников класса 2: ')
k2 = int(k2)
k3 = input('Введите колличество учеников класса 3: ')
k3 = int(k3)
sum = k1+k2+k3
SumDesck = sum / 2
if SumDesck % 2:
    SumDesck = int(SumDesck)
    print(f'Колличество необходимых парт: {SumDesck + 1}шт.' )
else:
    SumDesck = int(SumDesck)
    print(f'Колличество необходимых парт: {SumDesck}шт.' )
