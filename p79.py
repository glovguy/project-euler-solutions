import unittest


class DigitSeries(str):
    """Understands a series of digits"""

    def common_digits(self, other):
        commonDigitsSet = set()
        for currenti in range(0, 3):
            for eachi in range(0, 3):
                if self[currenti] == other[eachi]:
                    commonDigitsSet.add(DigitPair(currenti, eachi))
        return commonDigitsSet

    def slice(self, digitPair):
        return DigitSeries(self[:digitPair.a])

    def possible_combinations(self, other):
        commonDigitSet = self.common_digits(other)
        combinations = set([x for pairs in commonDigitSet for x in pairs.split_and_reassemble(self, other)])
        return combinations

    def shuffle_in(self, other):
        if len(self) == 0 or len(other) == 0:
            shuffledDigitSeries = DigitSeries(self + other)
            return set([shuffledDigitSeries])
        setOfShuffledDigitSeries = set()
        baseWeaving = Weaving(len(other) * [0], len(self)+1)
        setOfWeavings = {baseWeaving}
        incrementWeaving = Weaving(list(baseWeaving.jumpList), int(baseWeaving.maxJumps))
        incrementWeaving += 1
        while baseWeaving.jumpList != incrementWeaving.jumpList:
            setOfWeavings = setOfWeavings | {Weaving(list(incrementWeaving.jumpList), int(incrementWeaving.maxJumps))}
            incrementWeaving += 1
        for eachWeaving in setOfWeavings:
            setOfShuffledDigitSeries = setOfShuffledDigitSeries | {eachWeaving.weave_in(self, other)}
        return setOfShuffledDigitSeries


class DigitPair(object):
    """Understands a pair of digits"""

    def __init__(self, first, second):
        self.a = int(first)
        self.b = int(second)

    "Might consider getting rid of this class if this doesn't have any other methods."

    def __eq__(self, other):
        return (self.a == other.a and self.b == other.b) or \
               (self.a == other.b and self.b == other.a)

    def __hash__(self):
        return hash(self.a + self.b)

    def split_and_reassemble(self, digitSeriesA, digitSeriesB):
        prefix = DigitSeries(digitSeriesA[:self.a]).shuffle_in(DigitSeries(digitSeriesB[:self.b]))
        sharedDigit = DigitSeries(digitSeriesA[self.a])
        suffix = DigitSeries(digitSeriesA[self.a+1:]).shuffle_in(DigitSeries(digitSeriesB[self.b+1:]))
        return [DigitSeries(pre + sharedDigit + suf) for pre in prefix for suf in suffix]


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
    """Understands a particular combination of two digit series"""
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

    def __add__(self, num):
        output = Weaving(list(self.jumpList), int(self.maxJumps))
        [output.increment(1, 0) for _ in range(0, num)]
        return output

    def increment(self, amount, spot):
        self.jumpList[spot] += amount
        while self.jumpList[spot] >= self.maxJumps:
            if len(self.jumpList) > spot+1:
                self.increment(1, spot + 1)
            self.jumpList[spot] = self.jumpList[spot] - self.maxJumps
            if len(self.jumpList) > spot+1:
                self.jumpList[spot] += self.jumpList[spot + 1]
        return self

    def weave_in(self, base, insert):
        output = DigitSeries()
        for eachSpot in range(0, len(base)+1):
            for eachJump in range(0, len(self.jumpList)):
                if self.jumpList[::-1][eachJump] == eachSpot: output += DigitSeries(insert[eachJump])
            if eachSpot < len(base): output += base[eachSpot]
        return output


class TestFunctions(unittest.TestCase):

    def test_possible_combinations(self):
        self.assertEqual(DigitSeries(123).possible_combinations(DigitSeries(300)), set([DigitSeries(12300)]))
        self.assertEqual(DigitSeries(123).possible_combinations(DigitSeries(200)),
                         set([DigitSeries(12003), DigitSeries(12030), DigitSeries(12300)]))
        self.assertEqual(DigitSeries(33).possible_combinations(DigitSeries(33)),
                         set([DigitSeries(33), DigitSeries(333), DigitSeries(3333)]))

    def test_common_digits(self):
        self.assertEqual(DigitSeries(729).common_digits(DigitSeries(316)), set())
        self.assertEqual(DigitSeries(620).common_digits(DigitSeries(762)), set([DigitPair(0, 1), DigitPair(1, 2)]))
        self.assertEqual(DigitSeries(129).common_digits(DigitSeries(620)), set([DigitPair(1, 1)]))

    def test_shuffle_in(self):
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(1)), set([DigitSeries(11)]))
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(2)), set([DigitSeries(21), DigitSeries(12)]))
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(2)), set([DigitSeries(12), DigitSeries(21)]))
        self.assertEqual(DigitSeries(11).shuffle_in(DigitSeries(2)),
                         set([DigitSeries(112), DigitSeries(121), DigitSeries(211)]))
        self.assertEqual(DigitSeries(1).shuffle_in(DigitSeries(22)),
                         set([DigitSeries(122), DigitSeries(212), DigitSeries(221)]))
        self.assertEqual(DigitSeries(2).shuffle_in(DigitSeries()), set([DigitSeries(2)]))
        self.assertEqual(DigitSeries(12).shuffle_in(DigitSeries()), set([DigitSeries(12)]))

    def test_remove_duplicate_entries(self):
        self.assertEqual(remove_duplicate_entries(set(['a', 'a'])), set(['a']))
        self.assertEqual(remove_duplicate_entries(set([DigitSeries(11), DigitSeries(11)])), set([DigitSeries(11)]))

    def test_weaving_equality(self):
        self.assertEqual(Weaving([0, 0], 3), Weaving([0, 0], 3))
        self.assertNotEqual(Weaving([0, 0], 3), Weaving([1, 0], 3))
        self.assertNotEqual(Weaving([0, 0], 2), Weaving([0, 0], 3))

    def test_weaving_increment(self):
        testWeaving = Weaving([1, 0, 0], 3)
        self.assertEqual(testWeaving, Weaving([1, 0, 0], 3))
        self.assertEqual(testWeaving + 1, Weaving([2, 0, 0], 3))
        testWeaving = Weaving([2, 0, 0], 3)
        self.assertEqual(testWeaving+1, Weaving([1, 1, 0], 3))
        onlyOne = Weaving([1, 0, 0], 3)
        fiveAdded = Weaving([1, 1, 1], 3)
        self.assertEqual(onlyOne + 5, fiveAdded)
        largerWeaving = Weaving([1, 0, 0], 8)
        largerWithFifteen = Weaving([3, 2, 0], 8)
        self.assertEqual(largerWeaving + 15, largerWithFifteen)
        precycleWeaving = Weaving([4, 4], 5)
        cycledWeaving = Weaving([0, 0], 5)
        self.assertEqual(precycleWeaving + 1, cycledWeaving)
        precycleWeaving = Weaving([4, 4], 5)
        cycleFurther = Weaving([2, 1], 5)
        self.assertEqual(precycleWeaving + 7, cycleFurther)
        lowMaxJumpsWeaving = Weaving([0, 0], 2)
        lowMaxJumpIncremented = Weaving([1, 0], 2)
        self.assertEqual(lowMaxJumpsWeaving + 1, lowMaxJumpIncremented)

    def test_weave_in(self):
        basicWeaving = Weaving([0, 0], 3)
        one = DigitSeries(12)
        another = DigitSeries(45)
        basicResult = DigitSeries(4512)
        self.assertEqual(basicWeaving.weave_in(one, another), basicResult)
        simpleWeaving = Weaving([1, 1], 3)
        simpleResult = DigitSeries(1452)
        self.assertEqual(simpleWeaving.weave_in(one, another), simpleResult)
        complicatedWeaving = Weaving([2, 1], 3)
        complicatedResult = DigitSeries(1425)
        self.assertEqual(complicatedWeaving.weave_in(one, another), complicatedResult)


if __name__ == '__main__':
    unittest.main(verbosity=1)
    ## Import file
    # f = open('p79keylog.txt', 'r')
    # keylog = []
    # for line in f:
    #     keylog.append(DigitSeries(int(line)))
    # print keylog
    # keylog.pop(0)
