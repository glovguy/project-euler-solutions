import sys

testUntil = 1048576
EvenlyDivisibleBy = 10
testRange = range(1, testUntil+1)
debug = False


def my_num(myVar):
    outputNum = 1
    for iter in range(1, min(len(str(bin(myVar)))-2, EvenlyDivisibleBy)+1):
        if bin(myVar)[len(str(bin(myVar)))-iter] == str(1):
            outputNum *= (iter+1)
    if bin(myVar)[len(str(bin(myVar))) - 1] == str(1): sys.stdout.write('.')
    return outputNum


for eachNum in testRange:
    for eachDivisor in range(1, EvenlyDivisibleBy+1):
        if my_num(eachNum) % eachDivisor != 0:
            break
        elif eachDivisor == EvenlyDivisibleBy:
            print "\nAnswer:"
            print my_num(eachNum)
            print "is evenly divisible by " + str(EvenlyDivisibleBy)
            print "as well as every number lower"
            quit()
    pass
