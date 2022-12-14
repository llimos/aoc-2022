from aocd import lines, submit

lines = [[[int(z) for z in y.split(',')] for y in x.split(' -> ')] for x in lines]
blocked = set()
floor = 0
for line in lines:
    prev = line[0]
    for coord in line:
        blocked.update({(x, y)
                        for x in range(min(prev[0], coord[0]), max(prev[0], coord[0]) + 1)
                        for y in range(min(prev[1], coord[1]), max(prev[1], coord[1]) + 1)})
        floor = max(floor, coord[1] + 2)
        prev = coord

n = 0
while (500, 0) not in blocked:
    n += 1
    (x, y) = (500, 0)
    while y + 1 < floor and not blocked.issuperset({(x, y+1), (x-1, y+1), (x+1, y+1)}):
        (x, y) = next(filter(lambda z: z not in blocked, ((x, y+1), (x-1, y+1), (x+1, y+1))))
    blocked.add((x, y))
submit(n)
