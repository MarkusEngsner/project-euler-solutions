from string import ascii_uppercase


def mergeSort(lst):
    ''' Sorts a list of strings'''
    if len(lst) <= 1:
        return lst
    split = len(lst) // 2
    L1 = mergeSort(lst[:split])
    L2 = mergeSort(lst[split:])
    resultLst = []
    while len(L1) > 0 and len(L2) > 0:
        if L1[0] < L2[0]:
            resultLst.append(L1[0])
            del L1[0]
        else:
            resultLst.append(L2[0])
            del L2[0]
    resultLst.extend(L1)
    resultLst.extend(L2)
    return resultLst


def calculateNameScore(index, name):
    total = 0
    for c in name:
        total += letterScores[c]
    total *= index + 1
    return total


def calcTotalScore(nameLst):
    total = 0
    for i in range(len(nameLst)):
        total += calculateNameScore(i, nameLst[i])
    return total


with open("p022_names.txt", "r") as readfile:
    content = readfile.read()
nameLst = [name.replace('"', '') for name in content.split(",")]
nameLst = mergeSort(nameLst)
letterScores = {c: ascii_uppercase.find(c)+1 for c in ascii_uppercase}
answer = calcTotalScore(nameLst)
print("Answer: {}".format(answer))