n = int(input("How many people are in the network? "))
invites = [1] * (n + 1)

for i in range(n - 1):
    inviter = int(input("Person "+ str(i + 1) +" was invited by person: "))
    invites[inviter] *= (invites[i + 1] + 1)

print(invites[n])