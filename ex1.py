list = []  

while len(list) < 10:
    n = int (input("Informe um número: "))
    list.append(n)

for n in list:
    if (n%2) == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')