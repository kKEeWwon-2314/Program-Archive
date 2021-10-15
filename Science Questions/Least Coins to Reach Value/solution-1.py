# Greedy algorithms solution

coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
value = int(input())

def calculate_min(coins, value):
    result = []
    for i in coins[::-1]:
        while (value >= i):
            value -= i
            result.append(i)
    return result

res = calculate_min(coins, value)
print('You will need a minimum of', len(res), 'coins.')
print(', '.join(str(i) for i in res))
