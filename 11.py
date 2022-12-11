from typing import Callable
from aocd import data, submit


# data = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
#
# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0
#
# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3
#
# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""

class Monkey:
    def __init__(self, monkeys: list,
                 items: list[int],
                 op: Callable[[int], int],
                 test: int,
                 if_true: int,
                 if_false: int):
        self.monkeys = monkeys
        self.items = items
        self.op = op
        self.test = lambda x: if_true if x % test == 0 else if_false
        self.inspections = 0

    def receive(self, item: int):
        self.items.append(item)

    def throw(self, item: int, to: int):
        self.monkeys[to].receive(item)

    def turn(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.do_item(item)

    def do_item(self, item):
        item = self.op(item)
        item = int(item/3)
        self.inspections += 1
        self.throw(item, self.test(item))


monkeys = []

for monkeyData in data.split('\n\n'):
    monkeyData = monkeyData.splitlines()
    index = int(monkeyData.pop(0).split(' ')[1][0])
    items = [int(x) for x in monkeyData.pop(0).split(': ')[1].split(', ')]
    op_parts = monkeyData.pop(0).split(' ')[-2:]
    if op_parts[0] == '*':
        if op_parts[1] == 'old':
            op = lambda x: x * x
        else:
            op = lambda x, m = int(op_parts[1]): x * m
    elif op_parts[0] == '+':
        op = lambda x, m = int(op_parts[1]): x + m
    test = int(monkeyData.pop(0).split(' ')[-1])
    if_true = int(monkeyData.pop(0).split(' ')[-1])
    if_false = int(monkeyData.pop(0).split(' ')[-1])
    monkeys.append(Monkey(monkeys, items, op, test, if_true, if_false))

for i in range(20):
    # print("Round", i)
    for (j, monkey) in enumerate(monkeys):
        monkey.turn()
        # print("Monkey", j, [(i, x.items) for (i, x) in enumerate(monkeys)])
    # print("\n")

inspections = sorted((x.inspections for x in monkeys), reverse=True)[0:2]
submit(inspections[0]*inspections[1])
