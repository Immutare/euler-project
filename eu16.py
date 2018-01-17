num = 2 ** 1000
acum = 0

strNum = str(num)

for x in strNum:
    acum += int(x)
    print "{0}\tacum: {1}".format(x,acum)

print acum
