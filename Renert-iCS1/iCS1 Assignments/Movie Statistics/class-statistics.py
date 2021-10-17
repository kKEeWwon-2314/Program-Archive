import array

input_file1 = open('ics1-class-ratings.txt')
lines1 = input_file1.readlines()
num_lines1 = len(lines1)

input_file2 = open('ics1-movies.txt')
lines2 = input_file2.readlines()
num_lines2 = len(lines2)

for i in range(num_lines2):
    if (i % 2) != 0:
        line_of_text2 = lines2[i]

# most popular movie
popular_counter = [0] *100
for i in range(num_lines1):
    if (i % 2) != 0:
        line_of_text1 = lines1[i]
        for j in range(200):
            if (j % 2) == 0:
                if line_of_text1[j] != '0':
                    ii=j//2
                    popular_counter[ii] = popular_counter[ii] + 1
max_v = [0]*1
max_p = 0

for k in range(1, 100): 
        if popular_counter[k] > max_v[0]: 
            max_v[0] = popular_counter[k]
            max_p = k
print(lines2[max_p])

# average
total_counter = 0
for i in range(num_lines1):
    if (i % 2) != 0:
        line_of_text1 = lines1[i]
        for j in range(200):
            if (j % 2) == 0:
                if line_of_text1[j] != '0':
                    total_counter = total_counter + 1       
print(total_counter//21)

# highest rated
rated_counter = [0] *100
for i in range(num_lines1):
    if (i % 2) != 0:
        line_of_text1 = lines1[i]
        for j in range(200):
            if (j % 2) == 0:
                if line_of_text1[j] == '5':
                    ii=j//2
                    rated_counter[ii] = rated_counter[ii] + 1 
max_v = [0]*1
max_p = 0

for k in range(1, 100): 
        if rated_counter[k] > max_v[0]: 
            max_v[0] = rated_counter[k]
            max_p = k
print(lines2[max_p])

# lowest rated

rated_counter = [0] *100
for i in range(num_lines1):
    if (i % 2) != 0:
        line_of_text1 = lines1[i]
        for j in range(200):
            if (j % 2) == 0:
                if line_of_text1[j] == '1':
                    ii=j//2
                    rated_counter[ii] = rated_counter[ii] + 1 
max_v2 = [0]*1
max_p2 = 0

for k in range(1, 100): 
        if rated_counter[k] > max_v2[0]: 
            max_v2[0] = rated_counter[k]
            max_p2 = k
print(lines2[max_p2])

# least popular movies

popular_counter = [0] *100
for i in range(num_lines1):
    if (i % 2) != 0:
        line_of_text1 = lines1[i]
        for j in range(200):
            if (j % 2) == 0:
                if line_of_text1[j] == '0':
                    ii=j//2
                    popular_counter[ii] = popular_counter[ii] + 1
max_v = [0]*1
max_p = 0

for k in range(1, 100): 
        if popular_counter[k] > max_v[0]: 
            max_v[0] = popular_counter[k]
            max_p = k
print(lines2[max_p])