from time import time

def isPower(n, base):
    exponent = 1
    result = base ** exponent
    while result < n:
        result = base ** exponent
        if result == n:
            return True
        exponent += 1
    return False


def powerOf(n, baseDict):
    for base in baseDict:
        if base ** 2 > n:
            return 0
        if isPower(n, base):
            return base
    return 0


def buildBaseDict(lower, higher):
    ''' both limits are inclusive'''
    baseDict = {}
    for i in range(lower, higher + 1):
        base = powerOf(i, baseDict)
        if base == 0:
            baseDict[i] = 1
        else:
            baseDict[base] += 1
    return baseDict

def buildNewUniques(n, minExp, maxExp):
    ''' builds a dict with exponents as keys 
        and amount of new, unique, powers as values
        n: greatest multiple '''
    base = 2 # could be any base
    uniqueDict = {i:0 for i in range(1, n + 1)}
    powerSet = set()
    for i in range(1, n + 1):
        for j in range(minExp, maxExp +1):
            power = base ** (j * i)
            if not power in powerSet:
                uniqueDict[i] += 1
                powerSet.add(power)
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

start = time()
low = 2
high = 2000
answer = uniqueCount(low, high)
end = time()
print("Answer: {}".format(answer))
print("Took {} ms".format(round(1000*(end - start))))

answer = compute(high)
alt = time()
print("Answer: {}".format(answer))
print("Took {} ms".format(round(1000*(alt - end))))
# Takes about 4 ms on my machine