n = int(input())
namel1 = input().split()
namel2 = input().split()

is_good = True; i = 0
while ((i < n) and is_good):
    position = namel1.index(namel2[i])
    if ((namel1[i] != namel2[position]) or (position == i)):
        is_good = False
    i += 1

print('good') if is_good else print('bad')