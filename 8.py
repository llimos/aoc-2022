from aocd import lines, submit

lines = [[int(x) for x in y] for y in lines]
# Make a matrix
matrix = [[False for x in y] for y in lines]
# Start going through it
# Horizontal
for (y, line) in enumerate(lines):
    maxL = -1
    maxR = -1
    length = len(line)
    i = 0
    while i < length:
        if line[i] > maxL:
            matrix[y][i] = True
            maxL = line[i]
        if line[length - i - 1] > maxR:
            matrix[y][length - i - 1] = True
            maxR = line[length - i - 1]
        i += 1

# Vertical
x = 0
while x < len(lines[0]):
    maxT = -1
    maxB = -1
    height = len(lines)
    i = 0
    while i < height:
        if lines[i][x] > maxT:
            matrix[i][x] = True
            maxT = lines[i][x]
        if lines[height - 1 - i][x] > maxB:
            matrix[height - 1 - i][x] = True
            maxB = lines[height - 1 - i][x]
        i += 1
    x += 1

print(sum([sum([1 for y in x if y is True]) for x in matrix]))

# part 2
matrix = [[1 for x in y] for y in lines]

# Iterate in each direction. The decreasing streak is the score
# Horizontal
for (y, line) in enumerate(lines):
    last = [0] * 10
    x = 0
    while x < len(line):
        matrix[y][x] *= x - max(last[line[x]:], default=0)
        last[line[x]] = x
        x += 1

    last = [len(line)-1] * 10
    x = len(line) - 1
    while x >= 0:
        matrix[y][x] *= min(last[line[x]:], default=len(line)-1) - x
        last[line[x]] = x
        x -= 1

# Vertical
x = 0
while x < len(lines[0]):
    last = [0] * 10
    y = 0
    while y < len(lines):
        matrix[y][x] *= y - max(last[lines[y][x]:], default=0)
        last[lines[y][x]] = y
        y += 1

    last = [len(lines)-1] * 10
    y = len(lines) - 1
    while y >= 0:
        matrix[y][x] *= min(last[lines[y][x]:], default=len(lines)-1) - y
        last[lines[y][x]] = y
        y -= 1
    x += 1

# print('\n'.join('\t'.join(str(n) for n in y) for y in matrix))
print(max(max(y) for y in matrix))
