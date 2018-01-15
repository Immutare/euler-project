primeNumbers = [2]

def isPrime(number):
    sqr = number ** 0.5
    for x in primeNumbers:
        if x > int(sqr):
            break
        if number % x == 0:
            return False

    primeNumbers.append(number)
    return True

acum = 2
cont = 1

for i in range(3,2000000):
    if isPrime(i):
        cont += 1
        acum += i
        print "Primo #{0}:  {1}\tAcum: {2}".format(cont,i,acum)
    if i % 10000 == 0:
        print "#{0}".format(i)

print "Sum: {0}".format(acum)
