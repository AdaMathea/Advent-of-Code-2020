import re

occurence = 0
valid = 0
f = open('input.txt')
for l in f:
    line_array = re.split('-| |: |\n', l)
    for i in range(len(line_array[3])):
        if line_array[3][i] == line_array[2]:
            occurence += 1

    if int(line_array[0]) <= occurence <= int(line_array[1]):
        valid += 1
    occurence = 0

print(f'There are {valid} valid passwords')