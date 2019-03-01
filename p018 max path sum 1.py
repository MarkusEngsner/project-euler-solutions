# Maximum path sum I, Problem 18
# Problem description:
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.

# Task: Find the maximum total from top to bottom of the triangle below:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# https://projecteuler.net/problem=18


def triangleFromFile(filename):
    ''' reads the triangle from filename into a list of lists '''
    triangle = []
    with open(filename, "r") as infile:
        line = infile.readline().strip()
        while line:
            sList = line.split(" ")
            numList = [int(s) for s in sList]
            triangle.append(numList)
            line = infile.readline().strip()
    return triangle


def maxPathSumHelper(triangle, memoTri, i, j):
    ''' returns path with highest value from current spot to top '''
    if i == -1 or j == -1 or j >= len(triangle[i]):
        return 0
    if memoTri[i][j] != 0:
        return memoTri[i][j]
    else:
        costLeft = maxPathSumHelper(triangle[:-1], memoTri, i-1, j-1)
        costRight = maxPathSumHelper(triangle[:-1], memoTri, i-1, j)
        if costLeft > costRight:
            memoTri[i][j] = costLeft + triangle[i][j]
        else:
            memoTri[i][j] = costRight + triangle[i][j]
    return memoTri[i][j]


def maxPathSum(triangle, memoTri):
    ''' finds value for every bottom spot to top,
        and returns the greatest one '''
    i = len(triangle) - 1
    highest = 0
    for j in range(len(triangle[-1])):
        current = maxPathSumHelper(triangle, memoTri, i, j)
        if current > highest:
            highest = current
    return highest


triangle = triangleFromFile("p018_triangle.txt")
memoTri = [[0 for j in range(len(triangle[i]))] for i in range(
    len(triangle))] #creates the triangle for values to be saved in, with same size as original triangle
score = maxPathSum(triangle, memoTri)
print("Answer: {}".format(score))