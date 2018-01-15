import random

num = 0
cant = 0
cont = 0
salto = 1

def cantDivisores(num):
    aux = 0
    num2 = int(num ** 0.5)
    # print "{0} to {1}".format(1, num2+1)
    for i in range(1, num2):
        print "{0} % {1} == {2}".format(num, i, num % i)
        if num % i == 0:
            # print "{0} % {1} == {2}".format(num, i, num % i)
            aux += 2
    if num2 ** 2 == num:
        aux -= 1
    return aux

while cant < 10:
    cant = cantDivisores(num)
    num += salto
    salto += 1
    cont += 1
    print "({0}) divisores: {1}".format(num, cant)


print "Triangulo:", num
