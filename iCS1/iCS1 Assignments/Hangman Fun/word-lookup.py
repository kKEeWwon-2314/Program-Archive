import array
import sys

x = sys.argv[1]

input_file = open('introcs-lexicon.txt')
lines = input_file.readlines()
num_lines = len(lines)
for i in range(num_lines):
    line_of_text = lines[i]
    line_of_text = line_of_text.replace('\n','')
    x = x.replace('\n','')
    #print(line_of_text)
    if x == line_of_text:
        print('According to our lexicon,',x,'is the', i+1,'rd most common word in contemporary American English.')

def convert(str): 
    return ''.join(sorted(str))  
str = x
print(convert(str))