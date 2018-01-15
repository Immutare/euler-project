def isPyth(a,b,c):
    if ((a ** 2) + (b ** 2)) == c ** 2 and a < b and b < c:
        return True
    return False

numA = 1
numB = lastB = 2
numC = 3

while True:
    numB = numB + 1
    numC = (numA ** 2) + (numB ** 2)
    numC = numC ** 0.5

    if (numA + numB + numC == 1000):
        if isPyth(numA, numB, numC):
            break

    if (numA + numB + numC > 1000):
        numA = lastB
        numB = lastB + 1
        lastB = numB

print "{0} + {1} + {2}: {3}".format(numA,numB,numC, numA+numB+numC)
print "Product: {0}".format(numA*numB*numC)
