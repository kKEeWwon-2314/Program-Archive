n = int(input())
s = 0

while (n >= 0):
    if (n % 5) == 0:
        s += 1
    n -= 4

print(s)