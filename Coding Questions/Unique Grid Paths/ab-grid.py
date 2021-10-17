# This code finds all possible ways to go from point A (top-left corner) to point B (bottom-right corner) on an m * n grid.
# Contribution from https://learncodingfast.com/unique-paths/ 

m = int(input())
n = int(input())

def findAllPaths(m, n):
    s = m + n - 2
    p = 1

    for i in range(min(m, n) - 1):
        p = p * s / (i + 1)
        s -= 1
    return int(p)

print('Number of paths:', findAllPaths(m, n))
