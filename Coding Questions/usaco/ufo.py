import numpy

comet_name = list(input().lower())
group_name = list(input().lower())

comp1 = [] 
comp2 = []

for i in comet_name:
    comp1.append(ord(i) - 96)
for i in group_name:
    comp2.append(ord(i) - 96)


if ((numpy.prod(comp1) % 47) == (numpy.prod(comp2) % 47)):
    print('GO')
else:
    print('STAY')
