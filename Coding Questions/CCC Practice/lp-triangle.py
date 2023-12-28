n, m = list(map(int, input().split()))

def palindrome(s):
    if (s[::-1] == s):
        return True
    else:
        return False

for i in range(n):
    line = input()
    if not palindrome(line):
        print(-1)