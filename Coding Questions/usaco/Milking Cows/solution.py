start = 0
end = 0

times = []
milk_time = []
idle_time = []

for i in range(int(input())):
    times.append(list(map(int, input().split())))

times = sorted(times)

start = times[0][0]
end = times[0][1]

milk_time.append(end - start)
idle_time.append(0)

for i in range(len(times)):
    if (times[i][0] <= end):
        if (times[i][1] <= end):
            pass
        else:
            end = times[i][1]
            milk_time.append(end - start)
    else:
        start = times[i][0]

        idle_time.append(start - end)
        
        end = times[i][1]
        
        milk_time.append(start - end)

print(max(milk_time), max(idle_time))
