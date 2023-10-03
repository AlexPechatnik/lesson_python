# вводится 2 числа, найти большее из них
a = input("vvedite chislo pervoe a = ")
a = int(a)

b = input("vvedite chislo vtoroe b = ")
b = int(b)

if a>b:
    print('a bigger b')
elif a==b:
    print('same')
else:
    print('b bigetst')