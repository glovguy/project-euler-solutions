'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def is_prime(num):
    upperLimit = int(num/2)
    for n in range(2, upperLimit):
        if num%n == 0:
            return False
    return True

def prime_numbers(until):
    t=0
    i=2
    while t < until+1:
        while not is_prime(i):
            i+=1
        t+=1
        yield i
        i+=1

primes = prime_numbers(10001)
allPrimes = [j for j in primes]
print(allPrimes[len(allPrimes)-1])
