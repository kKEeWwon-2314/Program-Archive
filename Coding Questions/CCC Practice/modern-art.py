m = int(input())
n = int(input())

rows = [0] * m
cols = [0] * n

k = int(input())
for i in range(k):
    direction, canvas_index = input().split()
    if (direction == 'R'):
        rows[int(canvas_index) - 1] ^= 1
    else:
        cols[int(canvas_index) - 1] ^= 1

print(rows.count(1) * len(cols) + cols.count(1) * len(rows) - 2 * rows.count(1) * cols.count(1))