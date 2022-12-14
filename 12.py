from aocd import lines, submit


def level(letter):
    return ord('a' if letter == 'S' else 'z' if letter == 'E' else letter)


end = next((y, x) for (y, line) in enumerate(lines) for (x, l) in enumerate(line) if l == 'E')
candidates = {(y, x) for (y, line) in enumerate(lines) for (x, l) in enumerate(line) if l in ['S', 'a']}
seen = candidates.copy()
i = 0
while end not in candidates:
    candidates = {(ty, tx) for (y, x) in candidates for (ty, tx) in ((y-1, x), (y+1, x), (y, x-1), (y, x+1))
                  if 0 <= ty < len(lines) and 0 <= tx < len(lines[ty])
                  and (ty, tx) not in seen and level(lines[ty][tx]) <= level(lines[y][x]) + 1}
    seen.update(candidates)
    i += 1
print(i)
