from time import time
import cProfile

def isPower(n, base):
    result = n / base
    while result > 1:
        result /= base
    return result == 1


def powerOf(n, baseDict):
    for base in baseDict:
        if base ** 2 > n: # purely for performance
            return n
        if n % base == 0: # purely for performance
            if isPower(n, base):
                return base
    return n


def buildBaseDict(lower, higher):
    ''' both limits are inclusive'''
    baseDict = {}
    for i in range(lower, higher + 1):
        base = powerOf(i, baseDict)
        baseDict[base] = baseDict.get(base, 0) + 1
    return baseDict

def buildNewUniques(n, minExp, maxExp):
    ''' builds a dict with exponents as keys 
        and amount of new, unique, powers as values
        n: greatest multiple '''
    uniqueDict = {i:0 for i in range(1, n + 1)}
    expSet = set()
    for i in range(1, n + 1):
        for j in range(minExp, maxExp +1):
            exponent = j * i
            if not exponent in expSet:
                uniqueDict[i] += 1
                expSet.add(exponent)
    compoundedDict = {1:uniqueDict[1]}
    for i in range(2, n+1):
        compoundedDict[i] = uniqueDict[i] + compoundedDict[i-1]
    return compoundedDict

def uniqueCount(lower, higher):
    baseDict = buildBaseDict(lower, higher)
    highestExp = max(baseDict.values())
    uniqueDict = buildNewUniques(highestExp, lower, higher)
    result = 0
    for val in baseDict.values():
        result += uniqueDict[val]
    return result
        
def compute(limit):
    seen = set(a**b for a in range(2, limit + 1) for b in range(2, limit + 1))
    return str(len(seen))

def runCode():
    # start = time()
    low = 2
    high = 100
    answer = uniqueCount(low, high)
    # end = time()
    print("Limit: {}".format(high))
    print("Answer: {}".format(answer))
    print("Took {} ms".format(round(10 ** 3 * (end - start))))
    #Takes about 0.29 ms on my machine (tested using timeit)
    """ answer = compute(high)
    alt = time()
    print("Answer: {}".format(answer))
    print("Took {} ms".format(round(10 ** 3 * (alt - end)))) """

#cProfile.run('runCode()')
runCode()