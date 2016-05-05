from tqdm import trange

testUntil = 1048576
EvenlyDivisibleBy = 10


def binary_digit_to_encoded_factor(digitToUnencode):
    encodedFactor = 1
    lengthOfBinaryString = len(str(bin(digitToUnencode)))-2
    for iter in range(1, lengthOfBinaryString+1):
        if binary_number_has_1_in_spot(digitToUnencode,iter):
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


for eachNum in trange(1, testUntil+1):
    for eachDivisor in range(1, EvenlyDivisibleBy+1):
        if binary_digit_to_encoded_factor(eachNum) % eachDivisor != 0:
            break
        elif eachDivisor == EvenlyDivisibleBy:
            the_answer_is(binary_digit_to_encoded_factor(eachNum))
    pass
print "No answer found"
