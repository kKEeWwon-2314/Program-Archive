l = sorted([6, 8, 4, 5, 2, 3]) # [2, 3, 4, 5, 6, 8]

n1 = 0
n2 = 0
for i in range(len(l)):
    if (i % 2 != 0):
        n1 = n1 * 10 + l[i]
    else:
        n2 = n2 * 10 + l[i]

print(n1 + n2) 
