def findSmallest(m, s):
    if (s == 0):
        if (m == 1):
            print(0)
        else:
            TypeError
        return
      
    if (s > 9 * m):
        TypeError
        return
    
    l = [0 for i in range(m + 1)]
    s -= 1
    
    # Backwards loop
    for i in range(m - 1, 0, -1):
        if (s > 9):
            l[i] = 9
            s -= 9
        else:
            l[i] = s
            s = 0    
    
    l[0] = s + 1
    for i in range(m):
        print(l[i],end='')

s = 9
m = 2
findSmallest(m, s)
