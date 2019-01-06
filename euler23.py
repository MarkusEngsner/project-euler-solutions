#Non-abundant sums, Problem 23 
#Problem description:
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that 
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Task: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# https://projecteuler.net/problem=23


from math import sqrt

def divisorSum(n):
    divSum = 1 
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            divSum += i
            if i != n/i: #to prevent adding the same number twice
                divSum += n/i
    return int(divSum)


def isAbundant(n):
    return divisorSum(n) > n


def abundantList(n):
    result = []
    for i in range(1, n+1):
        if isAbundant(i):
            result.append(i)
    return result


def twoSums(L, LIMIT):
    result = set()
    for i in range (len(L)):
        for j in range(i, len(L)):
            sumOfTwo = L[i] + L[j]
            if sumOfTwo > LIMIT:
                break
            elif sumOfTwo not in result:
                result.add(sumOfTwo)
    return result


def isSumOfTwo (n, sumSet, LIMIT):
    if n > LIMIT:
        return True
    return n in sumSet


def notSumOfTwoResult():
    LIMIT = 28123 #the known limit for numbers that can't be written as the sum of two abundant numbers
    abundantNumbers = abundantList(LIMIT)
    twoSumSet = twoSums(abundantNumbers, LIMIT)
    result = 0
    for i in range(1, LIMIT):
        if not (isSumOfTwo(i, twoSumSet, LIMIT)):
            result += i
    return result


print(notSumOfTwoResult())