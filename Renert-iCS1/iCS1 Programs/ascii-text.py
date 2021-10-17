import sys
import math

l = int(input())
h = int(input())
text = input()

a = [str(input()) for i in range(h)]

for i in range(h):
    for c in text:
        if c >= 'a' and c <= 'z':
            x = ord(c) - ord('a')
        elif c >= 'A' and c <= 'Z':
            x = ord(c) - ord('A')
        else:
            x = ord('z') - ord('a') + 1
            
        for j in range(l):
            print(a[i][x * l + j], end="")
            
    print("")