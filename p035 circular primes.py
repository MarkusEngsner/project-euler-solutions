# Circular primes, 35
# Problem description:
# The number, 197, is called a circular prime because
# all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# Task: How many circular primes are there below one million?
# https://projecteuler.net/problem=35


from math import log10


def primes(limit):
    prime_list = [True] * limit # faster than list comprehension
    prime_list[0] = False
    prime_list[1] = False
    for n, is_prime in enumerate(prime_list):
        if is_prime:
            yield n
            for i in range(2*n, limit, n):
                prime_list[i] = False


def has_impossible_perms(p):
    last_digit = 0
    while p > 0:
        last_digit = p % 10
        if last_digit % 2 == 0 or last_digit % 5 == 0:
            return True
        p = p // 10
    return False


def filter_primes(input_primes):
    result = set()
    for p in input_primes:
        if not has_impossible_perms(p) or p < 10:
            result.add(p)
    return result


def rotations(n):
    most_significant = int(log10(n))
    current_val = n
    for i in range(most_significant):
        smallest_val = current_val % 10
        current_val = current_val // 10 + smallest_val * 10 ** most_significant
        yield current_val



def circular_prime_count(limit=10 ** 6):
    filtered_primes = filter_primes(primes(limit))
    prime_count = 0
    while filtered_primes:
        prime = filtered_primes.pop()
        # have to add back prime to both this set and the permutations one,
        # to deal with primes that are circulars of themselves ie 11
        filtered_primes.add(prime) 
        current_circle_size = 1
        permutations = set(rotations(prime))
        permutations.add(prime)
        for perm in permutations:
            current_circle_size += 1
            if not perm in filtered_primes:
                break
        else:
            prime_count += current_circle_size
        filtered_primes -= permutations
    return prime_count


ans = circular_prime_count()
print("Answer: {}".format(ans))
