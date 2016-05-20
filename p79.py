import unittest

f = open('p79keylog.txt', 'r')

keylog = []
for line in f:
    keylog.append(int(line))


class DigitSeries(object):
    """Understands a series of digits"""
    def __init__(self, digits):
        self.nums = digits
        self.digits = str(digits)

    def __hash__(self):
        return hash(frozenset(self.nums))

    def __getitem__(self, item):
        return DigitSeries(self.digits[item])

    def __add__(self, other):
        return DigitSeries(self.digits + other.digits)

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
        return self


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


# def is_compatible(firstCommonDigit, secondCommonDigit):
#     if firstCommonDigit[0] == secondCommonDigit[0] or firstCommonDigit[1] == secondCommonDigit[1]:
#         return False
#     firstSlope = firstCommonDigit[1] - firstCommonDigit[0]
#     secondSlope = secondCommonDigit[1] - secondCommonDigit[0]


class test_functions(unittest.TestCase):

    def test_does_simplify(self):
        self.assertEqual(DigitSeries(729).common_digits(DigitSeries(316)), [])
        self.assertEqual(DigitSeries(620).common_digits(DigitSeries(762)), [DigitPair(0, 1), DigitPair(1, 2)])
        self.assertEqual(DigitSeries(129).common_digits(DigitSeries(620)), [DigitPair(1, 1)])

    def test_possible_combinations(self):
        self.assertEqual(DigitSeries(123).possible_combinations(DigitSeries(300)), [DigitSeries(12300)])
        self.assertEqual(DigitSeries(123).possible_combinations(DigitSeries(200)), [DigitSeries(12003), DigitSeries(12030), DigitSeries(12300)])


if __name__ == '__main__':
    unittest.main(verbosity=1)
