import unittest
from sets import Set

f = open('p79keylog.txt', 'r')

keylog = []
for line in f:
    keylog.append(int(line))


class DigitSeries(object):
    """Understands a series of digits"""
    def __init__(self, digits):
        self.nums = int(digits)
        self.digits = str(digits)

    def __hash__(self):
        return hash(frozenset(self.digits))

    def __getitem__(self, item):
        return DigitSeries(self.digits[item])

    def __add__(self, other):
        return DigitSeries(self.digits + other.digits)

    def __eq__(self, other):
        return self.digits == other.digits

    def __str__(self):
        return self.digits

    def common_digits(self, other):
        commonDigitsSet = []
        for currenti in range(0, 3):
            for eachi in range(0, 3):
                if self.digits[currenti] == other.digits[eachi]:
                    commonDigitsSet.append(DigitPair(currenti, eachi))
        return commonDigitsSet

    def slice(self, digitPair):
        return DigitSeries(self.digits[:digitPair.a])

    def possible_combinations(self, other):
        commonDigitSet = self.common_digits(other)
        combinations = [pairs.split_and_reassemble(self, other) for pairs in commonDigitSet]
        return combinations

    def shuffle_in(self, other):
        setOfShuffledDigitSeries = set()
        spotsAvailable = len(self.digits) + 1
        for eachDigit in range(spotsAvailable):
            oneShuffle = self.digits[:eachDigit] + other.digits + self.digits[eachDigit:]
            setOfShuffledDigitSeries = setOfShuffledDigitSeries | {DigitSeries(oneShuffle)}
        setOfShuffledDigitSeries = remove_duplicate_entries(setOfShuffledDigitSeries)
        return setOfShuffledDigitSeries


class DigitPair(object):
    """Understands a pair of digits"""

    def __init__(self, first, second):
        self.a = first
        self.b = second

    def __eq__(self, other):
        return (self.a == other.a and self.b == other.b) or \
               (self.a == other.b and self.b == other.a)

    # for x in range(numCombinationsBefore):
    #     beforeSharedDigit = self.digits[:commonDigitSet[0][x]] + other.digits[:commonDigitSet[0][x + 1]]
    #     sharedDigit = self.digits[commonDigitSet[0][0]]
    #     afterSharedDigit = self.digits[commonDigitSet[0][0] + 1:] + other.digits[commonDigitSet[0][1] + 1:]
    #     combinations.append(int(beforeSharedDigit + sharedDigit + afterSharedDigit))

    def split_and_reassemble(self, digitSeriesA, digitSeriesB):
        prefix = digitSeriesA[:self.a].shuffle_in(digitSeriesB[:self.b])
        sharedDigit = digitSeriesA[self.a]
        suffix = digitSeriesA[self.a:].shuffle_in(digitSeriesB[self.b:])
        return prefix + sharedDigit + suffix


def remove_duplicate_entries(myList):
    outputList = set()
    for eachItem in myList:
        if eachItem not in outputList:
            outputList = outputList | {eachItem}
    return outputList

# def is_compatible(firstCommonDigit, secondCommonDigit):
#     if firstCommonDigit[0] == secondCommonDigit[0] or firstCommonDigit[1] == secondCommonDigit[1]:
#         return False
#     firstSlope = firstCommonDigit[1] - firstCommonDigit[0]
#     secondSlope = secondCommonDigit[1] - secondCommonDigit[0]


class Weaving(object):
    def __init__(self, jumpList, maxJumps):
        self.jumpList = jumpList
        self.maxJumps = maxJumps

    def __hash__(self):
        return hash(frozenset(self.jumpList))

    def __eq__(self, other):
        if type(other) is not Weaving: return False
        return self.jumpList == other.jumpList and self.maxJumps == other.maxJumps

    def __str__(self):
        strRep = ''
        for eachSpot in self.jumpList:
            strRep = strRep + str(eachSpot) + '~'
        strRep += '(' + str(self.maxJumps) + ')'
        return strRep

    def __add__(self, other):
        return self.increment(other, 0)

    def increment(self, amount, spot):
        self.jumpList[spot] += amount
        while self.jumpList[spot] >= self.maxJumps:
            self.increment(1, spot + 1)
            self.jumpList[spot] -= self.maxJumps
        return self


class TestFunctions(unittest.TestCase):

    def test_common_digits(self):
        self.assertEqual(DigitSeries(729).common_digits(DigitSeries(316)), [])
        self.assertEqual(DigitSeries(620).common_digits(DigitSeries(762)), [DigitPair(0, 1), DigitPair(1, 2)])
        self.assertEqual(DigitSeries(129).common_digits(DigitSeries(620)), [DigitPair(1, 1)])

    def test_shuffle_in(self):
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(1)), set([DigitSeries(11)]))
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(2)), set([DigitSeries(21), DigitSeries(12)]))
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(2)), set([DigitSeries(12), DigitSeries(21)]))
        self.assertEqual(DigitSeries(11).shuffle_in(DigitSeries(2)),
                         set([DigitSeries(112), DigitSeries(121), DigitSeries(211)]))
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(22)),
                         set([DigitSeries(122), DigitSeries(212), DigitSeries(221)]))

    def test_remove_duplicate_entries(self):
        self.assertEqual(remove_duplicate_entries(set(['a', 'a'])), set(['a']))
        self.assertEqual(remove_duplicate_entries(set([DigitSeries(11), DigitSeries(11)])), set([DigitSeries(11)]))

    def test_encoded_weaving(self):
        testWeaving = Weaving([1, 0, 0], 3)
        criticalWeaving = Weaving([2, 0, 0], 3)
        self.assertEqual(testWeaving, Weaving([1, 0, 0], 3))
        self.assertEqual(testWeaving + 1, Weaving([2, 0, 0], 3))
        self.assertEqual(criticalWeaving + 1, Weaving([0, 1, 0], 3))
        addFive = Weaving([1, 2, 0], 3)
        self.assertEqual(testWeaving + 5, addFive)

    # def test_possible_combinations(self):
    #     self.assertEqual(DigitSeries(123).possible_combinations(DigitSeries(300)), [DigitSeries(12300)])
        # self.assertEqual(DigitSeries(123).possible_combinations(DigitSeries(200)),
        #                  [DigitSeries(12003), DigitSeries(12030), DigitSeries(12300)])


if __name__ == '__main__':
    unittest.main(verbosity=1)
