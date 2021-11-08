cost = 0
units = []

milk, n = map(int, input().split())
for i in range(n):
    units.append(list(map(int, input().split())))
units = sorted(units)

for i in units:
    if i:
        price, amount = i[0], i[1]
        if (milk == 0):
            break
        if (milk >= amount):
            milk -= amount
            cost += price * amount
        else:
            cost += price * milk
            milk = 0

print(cost)
