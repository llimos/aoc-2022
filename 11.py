from typing import Callable
from aocd import data, submit


data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

class Monkey:
    def __init__(self, monkeys: list, monkeydata: str):
        self.monkeys = monkeys
        monkeydata = monkeydata.splitlines()[1:]
        self.items = [int(x) for x in monkeydata.pop(0).split(': ')[1].split(', ')]
        op_parts = monkeydata.pop(0).split(' ')[-2:]
        if op_parts[0] == '*':
            if op_parts[1] == 'old':
                self.op = lambda x: x * x
            else:
                self.op = lambda x, m=int(op_parts[1]): x * m
        elif op_parts[0] == '+':
            self.op = lambda x, m=int(op_parts[1]): x + m
        test = int(monkeydata.pop(0).split(' ')[-1])
        if_true = int(monkeydata.pop(0).split(' ')[-1])
        if_false = int(monkeydata.pop(0).split(' ')[-1])
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
        item = item % 5681 # 9699690
        item = int(item/3)
        self.inspections += 1
        self.throw(item, self.test(item))


monkeys = []
monkeys.extend([Monkey(monkeys, x) for x in data.split('\n\n')])

for i in range(20 ):
    # print("Round", i)
    for (j, monkey) in enumerate(monkeys):
        monkey.turn()
        # print("Monkey", j, [(i, x.items) for (i, x) in enumerate(monkeys)])
    # print("\n")
print([x.inspections for x in monkeys])
inspections = sorted((x.inspections for x in monkeys), reverse=True)[0:2]
print(inspections[0]*inspections[1])


class Item:
    def __init__(self, init):
        self.factors = {}
        total = 1
        for n in (2,3,5,7,11,13,17,19):
            self.factors[n] = 0
            while init % n == 0:
                self.factors[n] += 1
                total *= self.factors[n]
                init /= n
        self.remainder = init - total

    def multiply(self, by):
        self.factors[by] += 1
        self.remainder *= by
        self.remainder %= 9699690

    def add(self, amt):
        self.remainder += amt
        self.remainder %= 9699690

    def square(self):
        for k in self.factors:
            self.factors[k] *= 2

    def is_divisible(self, by):
        return self.factors[by] and self.remainder % by == 0

# Go through each item
