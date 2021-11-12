temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
n = [-1] * len(temperatures)
s = []

for i in range(len(temperatures)):
    while(len(s) != 0 and temperatures[s[-1]] < temperatures[i]):
        n[s[-1]] = i - s[-1]
        s.pop(-1)
    s.append(i)

l = []
for i in range(len(temperatures)):
    l.append(n[i]) if n[i] > 0 else l.append(0)
print(l)
