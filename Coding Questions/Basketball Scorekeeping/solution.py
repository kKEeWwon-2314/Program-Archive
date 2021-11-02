sc = [] # ['6','5','2','D','C','+','+']
for i in input().split():
    sc.append(i)

while 'C' in sc:
    try:
        sc.pop(sc.index('C') - 1)
        sc.pop(sc.index('C'))
    except ValueError:
        break

while 'D' in sc:
    try:
        sc = [int(sc[sc.index('D') - 1]) * 2 if i == 'D' else i for i in sc]
    except ValueError:
        break

while '+' in sc:
    try:
        sc = [int(sc[sc.index('+') - 1]) + int(sc[sc.index('+') - 2]) if i == '+' else i for i in sc]
    except ValueError:
        break

print(sum(list(map(int, sc))))
