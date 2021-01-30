# creating elementary "seed" hashes using the built-in Python3 function hash(integer/string/tuple)

def integer_hash_unchanged():
    # outputs original integer given an integer
    
    x = int(input(''))
    print('Hash for',x,'is:', hash(x))

def integer_hash_string():
    # outputs seed hash given a string

    y = input('')
    print('Hash for',y,'is:', hash(y))

def integer_hash_tuple():
    # change tuple in here not through input

    z = ('a', 'e', 'i', 'o', 'u')
    print('Hash for',z,'is:', hash(z))

integer_hash_unchanged()
integer_hash_string()
integer_hash_tuple()
