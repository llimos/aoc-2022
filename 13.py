from json import loads
from aocd import data, submit
from functools import cmp_to_key


def inorder(left, right) -> int:
    if isinstance(left, int):
        if isinstance(right, int):
            return left - right
        return inorder([left], right)
    if isinstance(right, int):
        return inorder(left, [right])
    if len(left) == 0:
        return 0 - len(right)
    if len(right) == 0:
        return 1
    return inorder(left[0], right[0]) or inorder(left[1:], right[1:])


print(sum([i + 1
           for (i, pair) in enumerate(data.split('\n\n'))
           if inorder(loads(pair.split('\n')[0]), loads(pair.split('\n')[1])) < 0]))

# part 2
packets = [loads(packet) for packet in data.splitlines() if packet != '']
packets.extend(([[2]], [[6]]))
packets = sorted(packets, key=cmp_to_key(inorder))
submit((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
