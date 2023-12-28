n = int(input())
sunflowers = []

for i in range(n):
    sunflowers.append(list(map(int, input().split(' '))))

if ((sunflowers[0][0] < sunflowers[0][1]) and (sunflowers[0][0] < sunflowers[1][0])):
    for i in range(len(sunflowers)):
        for j in range(len(sunflowers)):
            print(sunflowers[i][j], end=' ')
        print()

elif ((sunflowers[0][0] > sunflowers[0][1]) and (sunflowers[0][0] > sunflowers[1][0])):
    for i in range(len(sunflowers)):
        for j in range(len(sunflowers)):
            print(sunflowers[n - i - 1][n - j - 1], end=' ')
        print()

elif ((sunflowers[0][0] < sunflowers[0][1]) and (sunflowers[0][0] > sunflowers[1][0])):
    for i in range(len(sunflowers)):
        for j in range(len(sunflowers)):
            print(sunflowers[n - j - 1][i], end=' ')
        print()

else:
    for i in range(len(sunflowers)):
        for j in range(len(sunflowers)):
            print(sunflowers[j][n - i - 1], end=' ')
        print()
