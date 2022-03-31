"""
Knapsack Question - Recursion

Given weights and profits of N items, fill 
a backpack with a specific limit of weight 
and storage such that the maximum profit is
achieved.

Time Complexity: O(2^n)
"""
def solve(weights, profit, capacity):
    return find_max_profit(weights, profit, capacity, 0)

def find_max_profit(weights, profits, capacity, index):
    # base case
    if (index >= len(weights) or capacity <= 0):
        return 0

    # recursive case
    profit1 = 0
    if (weights[index] <= capacity):
        # add each item to backpack, recursively check profit
        profit1 = profits[index] + find_max_profit(weights, profits, (capacity - weights[index]), index + 1)

    # exclude the item from backpack, recursively check profit for rest of itmes
    profit2 = find_max_profit(weights, profits, capacity, index + 1)

    # compare the profits
    return max(profit1, profit2)

n = int(input('How many items are we evaluating today? '))
capacity = int(input('What is the limit of the backpack? '))

weights = []
profits = []

for index in range(n):
    weight = int(input('Weight for item {0}: '.format(index + 1)))
    profit = int(input('Profit for item {0}: '.format(index + 1)))
    weights.append(weight)
    profits.append(profit)

print(solve(weights, profits, capacity))
