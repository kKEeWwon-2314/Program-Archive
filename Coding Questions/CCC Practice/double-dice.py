"""
https://dmoj.ca/problem/ccc14j3
"""
antonia_points = 100
david_points = 100

n = int(input())
for i in range(n):
    a, d = list(map(int, input().split()))
    if (a == d):
        pass
    elif (a > d):
        david_points -= a
    elif (d > a):
        antonia_points -= d

print(antonia_points)
print(david_points)