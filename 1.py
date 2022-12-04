from aocd import data, submit


def total(s: str) -> int:
    return sum([int(x) for x in s.split('\n')])


elves = sorted([total(x) for x in data.split('\n\n')], reverse=True)
print(elves[0])
print(sum(elves[0:3]))
# submit(sum(elves[0:3]))
