u"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
num1 = 999
num2 = 999

def isPalin(num):
    newNum = str(num)
    cant = 0
    if (len(newNum) % 2 == 0):
        cant = len(newNum) / 2
        if newNum[::cant] == newNum[::-cant]:
            return True
        return False
