import re

occurence = 0
valid = 0
f = open('input.txt')
for l in f:
    line_array = re.split('-| |: |\n', l)
    index1 = int(line_array[0])-1
    index2 = int(line_array[1])-1
    if line_array[3][index1] != line_array[3][index2]:
        if line_array[3][index1] == line_array[2] or line_array[3][index2] == line_array[2]:
            print(index1, index2, line_array[2], line_array[3])
            valid += 1

print(f'There are {valid} valid passwords')