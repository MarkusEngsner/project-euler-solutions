# Quadratic primes, Problem 27
# Problem description:
# Euler discovered the remarkable quadratic formula:
#   n ** 2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
# However, when n=40, 40 ** 2 + 40 + 41 = 40 * (40+1) + 41 is divisible by 41,
# and certainly when n = 41 , 41 ** 2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n ** 2 − 79n + 1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
# The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
#   n ** 2 + an + b
# where |a|<1000 and |b|≤1000
# where |n| is the modulus/absolute value of n,
# e.g. |11|=11 and |−4|=4

# Task: Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
# https://projecteuler.net/problem=27

# Simplifications:
# since Quadratic when (n = 0) = 0 ** 2 + 0 * a + b = b
# means that b has to be a prime for there to be any consecutive values


from time import time


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True


def consecutivePrimes(a, b, primeDict):
    n = 0
    while True:
        quadratic = n ** 2 + a * n + b
        try:
            if not primeDict[quadratic]:  # checks if it's a prime
                pass
        except:
            if not quadratic > PREBUILDMAX:
                break
            # has to be checked again if primeDict didn't include big enough numbers
            if not isPrime(quadratic):
                break
        n += 1
    return n


def largestConsec():
    primeDict = {x: True for x in range(2, PREBUILDMAX) if isPrime(x)}
    bList = [b for b in range(1, 1001) if isPrime(b)]
    maxA = 0
    maxB = 0
    highestConsecutive = 0
    lower = -1000
    higher = 1000
    for a in range(lower + 1, higher):
        for b in bList:
            consecutive = consecutivePrimes(a, b, primeDict)
            if consecutive > highestConsecutive:
                maxA = a
                maxB = b
                highestConsecutive = consecutive
    return (maxA, maxB)


start = time()
PREBUILDMAX = 20000
a, b = largestConsec()
answer = a * b
end = time()
print("Answer: {}".format(answer))
print("Took {}s".format(round((end - start), 2)))
# Takes about 0.4s on my machine