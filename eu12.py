import random

num = 0
cant = 0
cont = 0
salto = 1

def cantDivisores(num):
    aux = 0
    num2 = int(num ** 0.5)
    for i in range(1, num2+1):
        if num % i == 0:
            aux += 2
    if num2 ** 2 == num:
        aux -= 1
    return aux

while cant < 500:
    num += salto
    salto += 1
    cont += 1
    cant = cantDivisores(num)
    print "({0}) divisores: {1}".format(num, cant)


print "Triangulo:", num
