from aocd import data, submit

(piles, moves) = data.split('\n\n')
# Sometimes the manual solution is the correct one
piles = [list(x) for x in [
    'VCDRZGBW',
    'GWFCBSTV',
    'CBSNW',
    'QGMNJVCP',
    'TSLFDHB',
    'JVTWMN',
    'PFLCSTG',
    'BDZ',
    'MNZW'
]]

# moves = [[int(y) for y in x.split(' ')[1::2]] for x in moves.splitlines()]
# for (reps, frm, to) in moves:
#     while reps:
#         piles[to-1].append(piles[frm-1].pop())
#         reps -= 1
#
# submit(''.join([x[-1] for x in piles]))

moves = [[int(y) for y in x.split(' ')[1::2]] for x in moves.splitlines()]
for (reps, frm, to) in moves:
    piles[to-1].extend(piles[frm-1][-reps:])
    while reps:
        piles[frm-1].pop()
        reps -= 1

submit(''.join([x[-1] for x in piles]))
