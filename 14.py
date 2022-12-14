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
    sand = (500, 0)
    n += 1
    while sand not in blocked:
        try:
            sand = next((sand[0] + x, sand[1] + 1)
                        for x in [0, -1, 1] if sand[1] + 1 < floor and (sand[0] + x, sand[1] + 1) not in blocked)
        except StopIteration:
            blocked.add(sand)
submit(n)
