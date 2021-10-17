import array
import random

n = random.randrange(0, 3999)

input_file = open('introcs-lexicon.txt')
lines = input_file.readlines()
num_lines = len(lines)

line_of_random = lines[n]
put = len(line_of_random)
print(line_of_random)

#number_max = put-1 
guess_number = 0
guess_mem = ['_'] * put 
bad_guess = 

for i in range(8):
    guess = input('\nInput in you next guess: ')
    guess_flag = 0
    for j in range(put-1):
        if guess[0] == line_of_random[j]:
            #print('Nice Guess!')
            print(guess, end='')
            guess_mem[j] = guess
            guess_flag= 1
        else:
            if guess_mem[j] != '_':
                print(guess_mem[j],end='')
            else:
             print('_' ,end='')
             guess_mem[j] = '_'
    if guess_flag == 0:
        guess_number = guess_number+1
        print('\n', guess, end='')
    
    #print(guess_mem)
    if guess_number > 8:
        exit()