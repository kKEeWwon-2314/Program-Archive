# Dynamic programming solution

import sys

def calulate_min(coins, min, value):
    table = [0 for i in range(value + 1)]
    table[0] = 0

    for i in range(1, value + 1):
        table[i] = sys.maxsize

    for i in range(1, value + 1):
        for j in range(min):
            if (coins[j] <= i):
                temp = table[i - coins[j]]
                if (temp != sys.maxsize and
                    temp + 1 < table[i]):
                    table[i] = temp + 1
     
    if table[value] == sys.maxsize:
        return -1

    return table[value]
 
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
minimum = len(coins)
value = 5436 # target value

print(calulate_min(coins, minimum, value))

# Source: GeeksforGeeks