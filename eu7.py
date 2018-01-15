# x = 10001
# sqr = x ** 0.5
cont = 1
starting_number = 3
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

while cont <= 10000:
    if isPrime(starting_number):
        cont = cont + 1
        print "Primo #{0}:  {1}".format(cont,starting_number)
    starting_number = starting_number + 1
