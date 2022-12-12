from aocd import lines, submit


def level(letter):
    return ord('a' if letter == 'S' else 'z' if letter == 'E' else letter)


# Find start and end points
end = next((y, x) for (y, line) in enumerate(lines) for (x, l) in enumerate(line) if l == 'E')
candidates = {(y, x) for (y, line) in enumerate(lines) for (x, l) in enumerate(line) if l in ['S', 'a']}
# BFS
seen = set(candidates)
i = 0
while end not in candidates:
    candidates = {(ty, tx)
                  for (y, x) in candidates
                  for ty in range(max(y-1, 0), min(y+2, len(lines)))
                  for tx in range(max(x-1, 0), min(x+2, len(lines[ty])))
                  if abs(tx-x) != abs(ty-y) and (ty, tx) not in seen and level(lines[ty][tx]) <= level(lines[y][x]) + 1}
    seen.update(candidates)
    i += 1
print(i)
