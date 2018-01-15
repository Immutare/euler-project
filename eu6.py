"""
"""

cant = 100
acumSum = acumSquare = 0

for i in range(1,cant+1):
    acumSum = acumSum + i ** 2
    acumSquare = acumSquare + i

acumSquare = acumSquare ** 2

print "Difference of {0} and {1} is: {2}".format(acumSum, acumSquare, acumSquare - acumSum)
