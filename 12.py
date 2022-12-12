from aocd import lines, submit

# lines = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".splitlines()

def level(letter):
    if letter == 'S':
        letter = 'a'
    if letter == 'E':
        letter = 'z'
    return ord(letter)


def get_candidates(coord):
    (y,x) = coord
    candidates = []
    for ty in range(max(y-1, 0), min(y+2, len(lines))):
        for tx in range(max(x-1, 0), min(x+2, len(lines[0]))):
            if abs(tx) == abs(ty):
                continue
            if level(lines[ty][tx]) <= level(lines[y][x]) + 1:
                candidates.append((ty, tx))
    return candidates


# BFS
# Find start point
candidates = set()
starty = 0
startx = 0
while starty < len(lines) and startx < len(lines[0]):
    if lines[starty][startx] in ['S', 'a']:
        candidates.add((starty, startx))
    if startx < len(lines[0]) - 2:
        startx += 1
    else:
        startx = 0
        starty += 1

# BFS
visited = set(candidates)
steps = 0
i = 0
while len(candidates):
    new_candidates = set()
    for (y, x) in candidates:
        if lines[y][x] == 'E':
            submit(i)
            exit(0)
        for ty in range(max(y - 1, 0), min(y + 2, len(lines))):
            for tx in range(max(x - 1, 0), min(x + 2, len(lines[0]))):
                if abs(tx-x) == abs(ty-y) or (ty, tx) in visited:
                    continue
                if level(lines[ty][tx]) <= level(lines[y][x]) + 1:
                    new_candidates.add((ty, tx))
    # candidates = {new_candidates for coord in candidates for new_candidates in get_candidates(coord) if new_candidates not in visited}
    candidates = new_candidates
    visited.update(candidates)
    # print(candidates)
    i += 1
