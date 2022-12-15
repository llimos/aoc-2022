from aocd import lines, submit

# lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

lines = [[[int(part.split('=')[1]) for part in parts.split(', ')] for parts in line.split(':')] for line in lines]
lines = [((x, y), (bx, by), abs(bx - x) + abs(by - y)) for ((x, y), (bx, by)) in lines]
limit = 4000000

def no_beacon(row):
    exclude: set[tuple[int, int]] = set()
    for ((x, y), _, d) in lines:
        if abs(y-row) <= d:
            spare = d - abs(y-row)
            excl_from = max(0, x-spare)
            excl_to = min(limit, x+spare)
            overlapping = [(x1, x2) for (x1, x2) in exclude if not (x2 < excl_from - 1 or x1 > excl_to + 1)]
            merged = (min([x1 for (x1, x2) in overlapping] + [excl_from]), max([x2 for (x1, x2) in overlapping] + [excl_to]))
            exclude = exclude.difference(overlapping) | {merged}
    if len(exclude) == 2:
        [first, second] = list(exclude)
        return first[1] + 1 if first[0] < second[0] else second[1] + 1
    else:
        [start, end] = list(exclude)[0]
        if start > 0:
            return 0
        if end < limit:
            return limit




# submit(no_beacon(2000000))

# Part 2


# exclude = set()
# for ((x, y), (bx, by)) in lines:
#     d = abs(bx - x) + abs(by - y)
#     for tx in range(max(0, x-d), min(limit, x+d)+1):
#         spare = d - abs(tx - x)
#         for ty in range(max(0, y - spare), min(limit, y + spare) + 1):
#             exclude.add((tx, ty))

# submit(next(x * 4000000 + y for x in range(0, limit+1) for y in range(0, limit+1) if (x, y) not in exclude))

for row in range(limit + 1):
    if row % 5000 == 0:
        print(row)
    x = no_beacon(row)
    if x is not None:
        print((x, row))
        break

