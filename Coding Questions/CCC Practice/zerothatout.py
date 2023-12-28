stack = []
head = int(input())
for i in range(head):
    stack.append(int(input()))
print(stack)
rev_list = []
for i in range(head):
    n = stack[i]
    if (n == 0):
        rev_list.pop()
    else:
        rev_list.append(n)

print(sum(rev_list))