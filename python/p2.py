def next_fib(n1, n2, n3):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    return [n1, n2, n3]

def even_fibs():
    n1 = 1
    n2 = 2
    n3 = 0
    while True:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        [n1, n2, n3] = next_fib(n1, n2, n3)
        while n3 % 2 != 0:
            [n1, n2, n3] = next_fib(n1, n2, n3)
        yield n3

mygen = even_fibs()
n = 2
runningSum = 0
while n < 4000000:
    runningSum += n
    n = next(mygen)
print(runningSum)
