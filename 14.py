from aocd import lines, submit

# lines = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

lines = [[[int(z) for z in y.split(',')] for y in x.split(' -> ')] for x in lines]
blocked: set[tuple[int, int]] = set()
abyss = 0
for line in lines:
    prev = line[0]
    for coord in line:
        (startx, starty) = prev
        (endx, endy) = coord
        for x in range(min(startx, endx), max(startx, endx) + 1):
            for y in range(min(starty, endy), max(starty, endy) + 1):
                blocked.add((x, y))
        abyss = max(abyss, endy + 1)
        prev = coord
in_abyss = False
n = 0
while not in_abyss:
    sand = (500, 0)
    while not in_abyss:
        if (sand[0], sand[1]+1) not in blocked:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in blocked:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in blocked:
            sand = (sand[0]+1, sand[1]+1)
        else:
            blocked.add(sand)
            # print("Rests at", sand)
            break
        # print(sand)
        if sand[1] > abyss:
            # print("In abyss")
            in_abyss = True
    if not in_abyss:
        n += 1
submit(n)



