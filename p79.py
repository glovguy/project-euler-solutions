import unittest

f = open('p79keylog.txt', 'r')

keylog = []
for line in f:
    keylog.append(int(line))


class fragment(object):
    def __init__(self, digits):
        self.nums = digits
        self.digits = str(digits)

    def common_digits(self, other):
        commonDigitsSet = []
        for currenti in range(0, 3):
            for eachi in range(0, 3):
                if self.digits[currenti] == other.digits[eachi]:
                    commonDigitsSet.append([currenti, eachi])
        return commonDigitsSet

    def possible_combinations(self, other):
        commonDigitSet = self.common_digits(other)
        return [int(self.digits[:commonDigitSet[0][0]] + other.digits[:commonDigitSet[0][1]] +
            self.digits[commonDigitSet[0][0]] +
            self.digits[commonDigitSet[0][0]+1:] + other.digits[commonDigitSet[0][1]+1:])]


class test_functions(unittest.TestCase):

    def test_does_simplify(self):
        self.assertEqual(fragment(729).common_digits(fragment(316)), [])
        self.assertEqual(fragment(620).common_digits(fragment(762)), [[0, 1], [1, 2]])
        self.assertEqual(fragment(129).common_digits(fragment(620)), [[1, 1]])

    def test_possible_combinations(self):
        self.assertEqual(fragment(123).possible_combinations(fragment(300)), [12300])
        self.assertEqual(fragment(123).possible_combinations(fragment(200)), [12003, 12030, 12300])


if __name__ == '__main__':
    unittest.main(verbosity=1)
