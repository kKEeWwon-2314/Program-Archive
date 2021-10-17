# Recursive impletementation, capped at 998
 
import sys

def calulate_min(coins, min, V):
    if (V == 0):
        return 0

    n = sys.maxsize

    for i in range(0, min):
        if (coins[i] <= V):
            temp = calulate_min(coins, min, V-coins[i])
            if (temp != sys.maxsize and temp + 1 < n):
                n = temp + 1
    return n

coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
minimum = len(coins)
value = 564 # target value

print(calulate_min(coins, minimum, value))
 
# Source: GeeksforGeeks