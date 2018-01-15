"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
numero = 600851475143
factors = []
prime = 2

while True:
    if numero % prime == 0:
        factors.append(prime)
        numero = numero / prime
    else:
        prime+=1

    if numero == 1:
        break

print factors[-1:]
