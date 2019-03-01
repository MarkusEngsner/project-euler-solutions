# Names scores, Problem 22
# Problem description:
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# Task: What is the total of all the name scores in the file?
# https://projecteuler.net/problem=22

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
