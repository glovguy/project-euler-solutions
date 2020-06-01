'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''


def is_prime(num):
    upperLimit = int(num/2)
    for n in range(2, upperLimit):
        if num%n == 0:
            return False
    return True


def prime_factors(num):
    if is_prime(num):
        return [num]
    upperLimit = int(num/2)
    for n in range(2, upperLimit):
        if num%n == 0:
            return [*prime_factors(n), *prime_factors(num/n)]


primes = prime_factors(600851475143)
print('Primes: ', primes)
print('Largest: ', max(primes))
