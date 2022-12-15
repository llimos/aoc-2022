from aocd import lines, submit

lines = [[[int(part.split('=')[1]) for part in parts.split(', ')] for parts in line.split(':')] for line in lines]
lines = [((x, y), (bx, by), abs(bx - x) + abs(by - y)) for ((x, y), (bx, by)) in lines]
limit = 4000000

def no_beacon(row):
    exclude: list[tuple[int, int]] = list()
    for ((x, y), _, d) in lines:
        if abs(y-row) <= d:
            spare = d - abs(y-row)
            excl_from = max(0, x-spare)
            excl_to = min(limit, x+spare)
            new_exclude = list()
            for (x1, x2) in exclude:
                if x2 < excl_from - 1 or x1 > excl_to + 1:
                    new_exclude.append((x1, x2))
                else:
                    excl_from = min(excl_from, x1)
                    excl_to = max(excl_to, x2)
            new_exclude.append((excl_from, excl_to))
            exclude = new_exclude
    if len(exclude) == 2:
        [first, second] = exclude
        return first[1] + 1 if first[0] < second[0] else second[1] + 1
    elif exclude[0][0] > 0:
        return 0
    elif exclude[0][1] < limit:
        return limit


for row in range(limit + 1):
    x = no_beacon(row)
    if x is not None:
        print((x, row))
        submit(x * limit + row)
        break

