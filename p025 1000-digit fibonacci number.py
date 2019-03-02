# 1000-digit Fibonacci number, Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
#   Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#   F1 = 1
#   F2 = 1
#   F3 = 2
#   F4 = 3
#   F5 = 5
#   F6 = 8
#   F7 = 13
#   F8 = 21
#   F9 = 34
#   F10 = 55
#   F11 = 89
#   F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# Task: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# https://projecteuler.net/problem=25

# Simplification: for x, which is of length n: x >= 10 ** n

from time import time


def fiboLen(n):
    ''' returns the first number in the Fibonacci sequence which is of atleast n length '''
    fibo = 1
    current = 1
    prev = 1
    index = 2
    while fibo <= 10 ** n:
        prev = current
        current = fibo
        fibo = prev + current
        index += 1
    return index


start = time()
answer = fiboLen(1000)
end = time()
print("Answer: index {}".format(answer))
print("Took {} ms".format(round(1000*(end - start))))