import sys

n = int(input())
t = int(input())

hline = [-sys.maxsize]
yline = [-sys.maxsize]

ytable = {}
counter = 0

for i in range(n):
    x1, y1, x2, y2, val = list(map(int, input().split()))

    hline.append([x1,y1,y2,val])        #Incoming side
    hline.append([x2,y1,y2,-val])       #Outgoing side
    yline.append(y1)
    yline.append(y2)

hline.sort()
yline = list(set(yline)).sort()

for i in range(1, len(yline)):
    ytable[yline[i]] = i

yaxis = [0] * (len(yline) + 1)

for i in range(1, len(hline)):         
    for j in range(1, len(yline)):
        if (yaxis[j] >= t):
            counter += (yline[j + 1] - yline[j]) * (hline[i][0] - hline[i - 1][0])
    for j in range(ytable[hline[i][1]], ytable[hline[i][2]]):
        yaxis[j] += hline[i][3]

print(counter)