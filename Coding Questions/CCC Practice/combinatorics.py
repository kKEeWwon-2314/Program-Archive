from itertools import *

def permutate(s, repeats = False):
    l = [''.join(n) for n in permutations(s)]
    if (repeats):
        return l
    else:
        return list(set(l))

def combinate(s, repeats = False):
    l = [''.join(n) for n in combinations(s, len(s))]
    if (repeats):
        return l
    else:
        return list(set(l))
