from tqdm import trange

testUntil = 2**20
EvenlyDivisibleBy = 20


def binary_digit_to_encoded_factor(binaryDigit):
    encodedFactor = 1
    lengthOfBinaryString = len(str(bin(binaryDigit)))-2
    for iter in range(1, lengthOfBinaryString+1):
        if binary_number_has_1_in_spot(binaryNum=binaryDigit,spot=iter):
            encodedFactor *= (iter+1)
    return encodedFactor


def binary_number_has_1_in_spot(binaryNum, spot):
    return bin(binaryNum)[len(str(bin(binaryNum))) - spot] == str(1)


def the_answer_is(answer):
    print "\nAnswer:"
    print answer
    print "is evenly divisible by " + str(EvenlyDivisibleBy)
    print "as well as every number lower"
    quit()


for binaryDigit in trange(1, testUntil+1):
    for eachDivisor in range(1, EvenlyDivisibleBy+1):
        if binary_digit_to_encoded_factor(binaryDigit) % eachDivisor != 0:
            break
        elif eachDivisor == EvenlyDivisibleBy:
            the_answer_is(binary_digit_to_encoded_factor(binaryDigit))
    pass
print "No answer found"
