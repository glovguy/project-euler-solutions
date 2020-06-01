'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''


def is_palindrome(num):
    strn = str(num)
    ln = len(strn)
    for i in range(0, int(ln/2)):
        if strn[i] != strn[ln-i-1]:
            return False
    return True


def largest_palindrome_product():
    palins = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if is_palindrome(i*j):
                palins.append(i*j)
                continue
    return max(palins)


print(largest_palindrome_product())
