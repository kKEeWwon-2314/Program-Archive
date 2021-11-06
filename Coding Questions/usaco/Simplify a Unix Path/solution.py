path = str(input())

s =  [i for x in path.split('/') for i in (x, '/')]
s.pop()
s = [x for x in s if x]

while s[-1] == '/':
    try:
        s.pop()
    except ValueError:
        break

if '.' in s:
    s.pop(s.index('.') - 1)
    s.pop(s.index('.'))

while ".." in path:
    try:
        s.pop(s.index('..') + 1)
        s.pop(s.index('..') - 2)
        s.pop(s.index('..') - 1)
        s.pop(s.index('..'))
    except ValueError:
        break

print(''.join(s))
