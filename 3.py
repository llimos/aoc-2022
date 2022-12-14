from aocd import lines, submit


def find_dupe(s: str) -> str:
    half = int(len(s)/2)
    first = set(s[0:half])
    second = set(s[half:])
    return first.intersection(second).pop()


def get_priority(c: str) -> int:
    return ord(c) - ord('A') + 27 if c.isupper() else ord(c) - ord('a') + 1


#submit(sum([get_priority(find_dupe(x)) for x in lines]))

# b
priority = 0
for (i, line) in enumerate(lines):
    if i % 3 == 0:
        contents = set(line)
    else:
        contents.intersection_update(line)
        if i % 3 == 2:
            priority += get_priority(contents.pop())

submit(priority)
