n = int(input())
questions = [input() for i in range(n * 2)]

counter = 0
for i in range(n):
    if questions[i] == questions[i + n]:
        counter += 1

print(counter)