'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''


def triplet_to_1000():
    for c in range(998, 0, -1):
        maxB = 1000-c-1
        for b in range(maxB, int(maxB/2), -1):
            a = 1000 - c - b
            if a**2 + b**2 == c**2:
                print('Pythagorean triplet that matches: ', a, b, c)
                return a*b*c

print('Answer: ', triplet_to_1000())
