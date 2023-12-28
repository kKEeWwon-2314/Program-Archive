n, k = map(int, input().split())
destinations = list(map(int, input().split()))

poss = [0] * n
days = 0

while (days * k < n):
    days += 1

for i in range(days):
    poss[i] += max()

print(max(poss))
