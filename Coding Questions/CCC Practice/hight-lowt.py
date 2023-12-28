import math

n = int(input())
measurements = sorted(list(map(int, input().split())))

break_point = math.ceil(n / 2)

low_tides = sorted(measurements[:break_point], reverse=True)
high_tides = measurements[break_point:]

for i in range(break_point):
    print(low_tides[i], end=' ')
    print(high_tides[i], end=' ')