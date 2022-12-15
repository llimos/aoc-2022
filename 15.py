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

lines_with_distance = [[[x, y], abs(bx-x)+abs(by-y)] for ((x, y), (bx, by)) in lines]


def no_beacon(row):
    exclude = set()
    beacons = set()
    for ((x, y), (bx, by)) in lines:
        d = abs(bx - x) + abs(by - y)
        if by == row:
            beacons.add(bx)
        if abs(y-row) <= d:
            spare = d - abs(y-row)
            exclude.update(range(x-spare, x+spare+1))
    return len(exclude.difference(beacons))


submit(no_beacon(2000000))
