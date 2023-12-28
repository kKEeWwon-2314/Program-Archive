def dist(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)

sheep_x = []
sheep_y = []
n = int(input())
for i in range(n):
    sx = float(input())
    sy = float(input())
    sheep_x.append(sx)
    sheep_y.append(sy)

for i in range(n):
    if (sheep_y[i] == min(sheep_y)):
        print('The sheep at ('+ sheep_x[i] +'), ('+ sheep_y[i] + ') might be eaten.')
