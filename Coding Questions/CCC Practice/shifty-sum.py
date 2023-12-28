n = int(input())
k = int(input())

def shift_sum(n, k):
    if (k == 0):
        return n
    else:
        if (k > 0):
            return n + shift_sum(n * 10, k - 1)

print(shift_sum(n, k))