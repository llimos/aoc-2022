from itertools import product
from aocd import lines, submit

lines = [[[int(z) for z in y.split(',')] for y in x.split(' -> ')] for x in lines]
blocked = set()
floor = 0
for line in lines:
    prev = line[0]
    for curr in line:
        blocked.update(product(range(min(prev[0], curr[0]), max(prev[0], curr[0]) + 1), range(min(prev[1], curr[1]), max(prev[1], curr[1]) + 1)))
        floor = max(floor, curr[1] + 2)
        prev = curr
n = 0
while (500, 0) not in blocked:
    n += 1
    (x, y) = (500, 0)
    while y < floor - 1 and not {(x, y+1), (x-1, y+1), (x+1, y+1)} < blocked:
        (x, y) = next(filter(lambda z: z not in blocked, ((x, y+1), (x-1, y+1), (x+1, y+1))))
    blocked.add((x, y))
submit(n)
