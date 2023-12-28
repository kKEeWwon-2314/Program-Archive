def if_nasty(n):
    saved = []

    for i in range(1, n):
        if (n % i == 0):
            num1 = n / i
            num2 = i
            if (num1 > num2):
                saved.append([int(num1), num2])

    for i in range(len(saved)):
        for j in range(len(saved)):
            if (saved[i][0] - saved[i][1] == saved[j][0] + saved[j][1]):
                return (str(n) + ' is nasty')
    
    return (str(n) + ' is not nasty')

n = int(input())
for i in range(n):
    print(if_nasty(int(input())))
