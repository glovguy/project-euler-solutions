import unittest

f = open('p79keylog.txt', 'r')

keylog = []
for line in f:
    keylog.append(int(line))


def common_digits(currentKey, eachkey):
    commonDigitsSet = []
    for currenti in range(0, 3):
        for eachi in range(0, 3):
            if str(currentKey)[currenti] == str(eachkey)[eachi]:
                commonDigitsSet.append([currenti, eachi])
    return commonDigitsSet


class test_functions(unittest.TestCase):
    def test_does_simplify(self):
        self.assertEqual(common_digits(729, 316), [])
        self.assertEqual(common_digits(620, 762), [[0, 1], [1, 2]])
        self.assertEqual(common_digits(129, 620), [[1, 1]])


if __name__ == '__main__':
    unittest.main(verbosity=1)
