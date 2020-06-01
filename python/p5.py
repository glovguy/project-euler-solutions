'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


def factorial(num):
    fctr = 1
    for i in range(1, num):
        fctr *= i
    return fctr


def meets_criteria(num):
    for n in range(2,20):
        if num%n != 0:
            return False
    return True


def smallest_divisible_by_20():
    upperBounds = factorial(20)
    for i in range(2520, upperBounds, 20):
        if meets_criteria(i):
            return i


print(smallest_divisible_by_20())
