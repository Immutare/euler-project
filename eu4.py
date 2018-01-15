u"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalin(num):
    newNum = str(num)
    cant = 0
    if (len(newNum) % 2 == 0):
        cant = len(newNum) / 2
        reversedNum = newNum[::-1]
        if newNum[:cant] == reversedNum[:cant]:
            # print newNum[:cant]
            # print reversedNum[:cant]
            return True
        return False

listNum = []

for i in range(999, 450, -1):
    for j in range(999, 450, -1):
        if isPalin(i*j):
            listNum.append(i*j)

listNum.sort(reverse = True)
print listNum[0]
