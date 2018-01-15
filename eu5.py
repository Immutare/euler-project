"""


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def isAnAnswer(num):
    for i in range(1,21):
        if num % i != 0:
            return False
    return True


number = 2520

while not isAnAnswer(number):
    number = number + 20

print number
