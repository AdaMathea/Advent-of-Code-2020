def slope(x,y):
    if y == 1:
        with open('input.txt') as f:
            f.readline()
            lines = f.readlines()
    
    elif y == 2:
        with open('input.txt') as f:
            lines = f.readlines()
        lines = lines[2::2]
    i = x
    trees = 0
    for line in lines:
        line = line.strip()
        if line[i % len(line)] == '#':
            trees += 1
        i += x
    return trees

print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))