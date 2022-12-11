from aocd import lines, submit

# lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".splitlines()

lines = [(x[0], int(x[2:])) for x in lines]

h = (0,0)
t = (0,0)

visited = set()
visited.add(t)

def move_h(h, dir):
    if dir == 'U':
        return h[0], h[1] + 1
    elif dir == 'D':
        return h[0], h[1] - 1
    elif dir == 'L':
        return h[0] - 1, h[1]
    elif dir == 'R':
        return h[0] + 1, h[1]


def move_t(t, h):
    if abs(t[0] - h[0]) <= 1 and abs(t[1] - h[1]) <= 1:
        return t
    newt0 = t[0] + 1 if h[0] > t[0] else t[0] - 1 if h[0] < t[0] else t[0]
    newt1 = t[1] + 1 if h[1] > t[1] else t[1] - 1 if h[1] < t[1] else t[1]
    return (newt0, newt1)


for (dir, steps) in lines:
    while steps:
        h = move_h(h, dir)
        t = move_t(t, h)
        visited.add(t)
        steps -= 1

# submit(len(visited))

# part 2
visited.clear()
pos = [(0,0)] * 10
for (dir, steps) in lines:
    while steps:
        pos[0] = move_h(pos[0], dir)
        i = 1
        while i < len(pos):
            pos[i] = move_t(pos[i], pos[i-1])
            i += 1
        visited.add(pos[-1])
        steps -= 1

submit(len(visited))