from aocd import lines, submit
from math import inf

# lines = """30373
# 25512
# 65332
# 33549
# 35390""".splitlines()

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
    peaks = []
    x = 0
    while x < len(line):
        if x == 0:
            matrix[y][x] = 0
            peaks.append([x, line[x]])
        elif line[x] > line[x-1]:  # If it's <= do nothing (*1)
            last_bigger_peak = next((i for (i, h) in peaks if h >= line[x]), 0)
            matrix[y][x] *= x - last_bigger_peak
            peaks.insert(0, [x, line[x]])
        x += 1

    peaks = []
    x = len(line) - 1
    while x >= 0:
        if x == len(line) - 1:
            matrix[y][x] = 0
            peaks.append([x, line[x]])
        elif line[x] > line[x+1]:
            last_bigger_peak = next((i for (i, h) in peaks if h >= line[x]), len(line) - 1)
            matrix[y][x] *= last_bigger_peak - x
            peaks.insert(0, [x, line[x]])
        x -= 1

# Vertical
x = 0
while x < len(lines[0]):
    peaks = []
    y = 0
    while y < len(lines):
        if y == 0:
            matrix[y][x] = 0
            peaks.append([y, lines[y][x]])
        elif lines[y][x] > lines[y-1][x]:
            last_bigger_peak = next((i for (i, h) in peaks if h >= lines[y][x]), 0)
            matrix[y][x] *= y - last_bigger_peak
            peaks.insert(0, [y, lines[y][x]])
        y += 1

    peaks = []
    y = len(lines) - 1
    while y > 0:
        if y == len(lines) - 1:
            matrix[y][x] = 0
            peaks.append([y, lines[y][x]])
        elif lines[y][x] > lines[y+1][x]:
            last_bigger_peak = next((i for (i, h) in peaks if h >= lines[y][x]), len(lines) - 1)
            matrix[y][x] *= last_bigger_peak - y
            peaks.insert(0, [y, lines[y][x]])
        y -= 1

    x += 1

print('\n'.join('\t'.join(str(n) for n in y) for y in matrix))
print(max(max(y) for y in matrix))
