from random import *

def func(a):
    if a > 0:
        print("P")
    elif a == 0:
        print("N")
    else:
        print("N")

def somaImposto(taxaImposto, custo):
    custoNovo = custo * (taxaImposto / 100)
    custoNovo += custo
    print(custoNovo)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.') 

valores = [7, 2, 5, 0, 4]

def dobraValores():
    for v in valores:
        n = v * 2
        print(n)

def area(l, c):
    a = l * c
    print(a)

def textoAdaptavel(msg):
    tam = "-" * len(msg)
    print("--" + tam + "--")
    print(msg)
    print("--" + tam + "--")

def contador2():
    for n in range(10, 1, 1):
        print(n)

def maiorNumero(*num):
    l = len(num)
    a = max(num)
    print(f'Foram analisados {l} números e o maior é {a}.')