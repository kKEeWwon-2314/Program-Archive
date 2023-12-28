import itertools

n = int(input())

pages = []
pathways = [1]
counter = len(pathways)

shortest_path = 0
complete = ''

for i in range(n):
    m1 = list(map(int, input().split()))[1:]
    pages.append(m1)


for i in itertools.count():
    for page in pathways.copy():
        options = pages[page - 1]

        if not options and shortest_path == 0:
            shortest_path = i + 1

        for option in options:
            if option not in pathways:
                pathways.append(option)

    if (len(pathways) == counter):
        complete = 'Y' if (len(pathways) == n) else 'N'
        break

    counter = len(pathways)

print(complete)
print(shortest_path)