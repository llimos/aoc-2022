from aocd import lines, submit


"""
A % 3 = 2
X % 3 = 1
You win if your % 3 is one greater than his
You lose if it's one less
You tie if it's 0
"""


def get_score(line: [str, str]) -> int:
    score = ord(line[1]) % 3 or 3
    his = (ord(line[0]) - 1) % 3
    mine = ord(line[1]) % 3
    if mine - his == 1 or his - mine == 2:
        score += 6
    if mine == his:
        score += 3
    return score

scores = [get_score(x.split(' ')) for x in lines]
# submit(sum(scores))

# b

def get_score2(line: [str, str]) -> int:
    his = ((ord(line[0]) + 1) % 3) + 1  # 1 = rock, 2 = paper, 3 = scissors
    # win - one up, lose - one down, tie - same
    if line[1] == 'X':
        return (his - 1) or 3
    if line[1] == 'Y':
        return his + 3
    return (1 if his == 3 else his + 1) + 6

scores2 = [get_score2(x.split(' ')) for x in lines]
submit(sum(scores2))
