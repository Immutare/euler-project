basicNumbers = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six",
                "7":"seven", "8":"eight", "9":"nine", "10":"ten", "11":"eleven", "12":"twelve",
                "13":"thirteen","20":"twenty", "30":"thirty", "40":"forty", "50":"fifty",
                "60":"sixty","70":"seventy","80":"eighty", "90":"ninety"}

# decimals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# specials = ["ten","eleven", "twelve", "thirteen","thousand"]
# multiplesOfTen = ["ten", "twenty", "thirty", "forty", "fifty", "sixty","eighty", "ninety"]

def decimals(num):
    return basicNumbers[str(num)]

def nameThatNumber(num):
    strNum = str(num)
    lenNum = len(strNum)
    strAux = ''

    if num < 10:
        return decimals(num)
    if num < 100:
        if basicNumbers[]
        # strAux = strAux + strNum[0] +
        # if basicNumbers[strNum[1:]] == None:
        #     strAux = strAux[2]
        # else:
        #     strAux = strAux + basicNumbers[strNum[1:]]


algo = "123"

print algo[1:]

print nameThatNumber(60)
