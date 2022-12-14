from aocd import lines, submit

matrix = [[None] * 40 for i in range(6)]
cycle = 0
X = 1
strength = 0
def draw():
    global cycle, X, matrix
    if cycle >= 240:
        return
    matrix[int(cycle/40)][cycle % 40] = '#' if X-1 <= cycle % 40 <= X+1 else '.'

for line in lines:
    draw()
    cycle += 1
    op = line[0:4]
    if op == 'addx':
        draw()
        cycle += 1
        X += int(line[5:])
    if cycle >= 40*6:
        break

print('\n'.join([''.join(x) for x in matrix]))
