# -*- coding: utf-8 -*-
from __future__ import print_function
import time
start_time = time.time()

def oddNum(num, cont):
    cont += 1
    num = 3 * num + 1

    # print ("{0} ->".format(num), end="")

    if num == 1:
        return cont
    elif num % 2 == 0:
        cont = evenNum(num, cont)
    else:
        cont = oddNum(num, cont)
    return cont


def evenNum(num, cont):
    cont += 1
    num = num / 2

    # print ("{0} ->".format(num), end="")

    if num == 1:
        return cont
    elif num % 2 == 0:
        cont = evenNum(num, cont)
    else:
        cont = oddNum(num, cont)
    return cont

# numero = 13
contAux = 1
mayCont = 0
mayNum = 0

# print ("{0} ->".format(13), end="")

# contAux = oddNum(numero,contAux)

# print (contAux)

for numero in range(13,1000000):
    if numero % 2 == 0:
        contAux = evenNum(numero, contAux)
    else:
        contAux = oddNum(numero, contAux)
    if (mayCont < contAux):
        mayCont = contAux
        mayNum = numero
    # print ("{0}, ~ {1}".format(numero, contAux))
    contAux = 1

print ("El número {0} tiene una cadena de {1}".format(mayNum, mayCont))
print("--- %s seconds ---" % (time.time() - start_time))

# for i in range(13,1000000):
