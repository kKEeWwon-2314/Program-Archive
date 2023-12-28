n = int(input())
sw_runs = list(map(int, input().split()))
se_runs = list(map(int, input().split()))

sw_sum = 0
se_sum = 0

when_equal = 0

for i in range(n):
    sw_sum += sw_runs[i]
    se_sum += se_runs[i]
    if (sw_sum == se_sum):
        when_equal = i + 1

print(when_equal)