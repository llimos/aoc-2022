from operator import mul
from typing import Union
from aocd import data, submit


class Monkey:
    items: list[Union[int, dict[int, int]]]

    def __init__(self, monkeys: list, monkeydata: str):
        self.monkeys = monkeys
        monkeydata = monkeydata.splitlines()[1:]
        self.items = [int(x) for x in monkeydata.pop(0).split(': ')[1].split(', ')]
        op_parts = monkeydata.pop(0).split(' ')[-2:]
        self.op = (lambda x: x + int(op_parts[1])) if op_parts[0] == '+' else \
            (lambda y: y * y) if op_parts[1] == 'old' else (lambda z: z * int(op_parts[1]))
        self.divisor = int(monkeydata.pop(0).split(' ')[-1])
        self.if_true = int(monkeydata.pop(0).split(' ')[-1])
        self.if_false = int(monkeydata.pop(0).split(' ')[-1])
        self.inspections = 0

    def receive(self, item: dict[int, int]):
        self.items.append(item)

    def throw(self, item: dict[int, int], to: int):
        self.monkeys[to].receive(item)

    def test(self, item: dict[int, int]):
        return self.if_true if item[self.divisor] == 0 else self.if_false

    def do_item(self, item: dict[int, int]):
        self.inspections += 1
        item = {n: self.op(x) % n for (n, x) in item.items()}
        self.throw(item, self.test(item))

    def turn(self):
        while len(self.items) > 0:
            self.do_item(self.items.pop(0))


monkeys = []
monkeys.extend([Monkey(monkeys, x) for x in data.split('\n\n')])
divisors = [m.divisor for m in monkeys]
for m in monkeys:
    m.items = [{z: x % z for z in divisors} for x in m.items if isinstance(x, int)]

for i in range(10000):
    for monkey in monkeys:
        monkey.turn()

submit(mul(* sorted((x.inspections for x in monkeys), reverse=True)[0:2]))
