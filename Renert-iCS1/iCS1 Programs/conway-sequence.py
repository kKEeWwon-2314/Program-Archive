import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())
array = [r]

for i in range(1, l):
    a = []
    n, last = 0, -1
    
    for j in array:
        if (j != last):
            if (n != 0):
                a.append(n)
                a.append(last)
            n = 1
        else:
            n += 1
        last = j
    a.append(n)
    a.append(last)
    array = a

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(' '.join(str(j) for j in array))
