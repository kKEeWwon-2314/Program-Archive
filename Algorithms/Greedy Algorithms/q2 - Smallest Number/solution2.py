m = 5
s = 2
l = []

def findSmallest1(m, s, result=''):
    if m > 0 and s >= 0:
        d = ord('0')

        if result == "":
            d = ord('1')

        while d <= ord('9'):
            findSmallest1(m - 1, s - (d - ord('0')), result + chr(d))
            d += 1

    elif m == 0 and s == 0:
        l.append(int(result))

findSmallest1(m, s)
print(min(l))