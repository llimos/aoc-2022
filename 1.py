from aocd import data, submit
def total(s):
    return sum([int(x) for x in s.split('\n')])

elves = [total(x) for x in data.split('\n\n')]
print(elves)
submit(max(elves))
