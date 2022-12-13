from json import loads
from typing import Any
from aocd import data, submit
from functools import cmp_to_key


def inorder(left: Any, right: Any) -> int:
    return left - right if isinstance(left, int) and isinstance(right, int) \
        else inorder([left], right) if isinstance(left, int) \
        else inorder(left, [right]) if isinstance(right, int) \
        else len(left) - len(right) if len(left) == 0 or len(right) == 0 \
        else inorder(left[0], right[0]) or inorder(left[1:], right[1:])


print(sum([i + 1 for (i, pair) in enumerate(data.split('\n\n')) if inorder(*[loads(x) for x in pair.split('\n')]) < 0]))

packets = sorted([loads(packet) for packet in data.split('\n') if packet != '']+[[[2]], [[6]]], key=cmp_to_key(inorder))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
