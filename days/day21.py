#!/usr/bin/env python
import itertools
from collections import Counter


def part1(data, N=1000):
    pa, pb = map(int, (s.split()[-1] for s in data.strip().splitlines()))
    pa -= 1
    pb -= 1
    sa = sb = 0
    T = 0
    turn = 0
    while sa < N > sb:
        # T + 1 + T + 2 + T + 3
        roll = 3 * (T + 2)
        T += 3
        if turn:
            pb = (pb + roll) % 10
            sb += (pb + 1)
        else:
            pa = (pa + roll) % 10
            sa += (pa + 1)
        turn = 1 - turn

    if sa >= N:
        ans = sb * T
    else:
        ans = sa * T
    return ans


def part2(data, N=21):
    pa, pb = (int(s.split()[-1])-1 for s in data.strip().splitlines())
    rolls = Counter(sum(p) for p in itertools.product((1,2,3), repeat=3))

    wins = [0, 0]
    fringe = {((0, 0), (pa, pb), 0): 1}

    while fringe:
        for k, ns in sorted(fringe.items()):
            score, pos, turn = k
            fringe.pop(k)
            for roll, n in rolls.items():
                p = (pos[turn] + roll) % 10
                s = score[turn] + p + 1
                m = ns * n
                if s >= N:
                    wins[turn] += m
                    continue
                if turn:
                    q = ((score[0], s), (pos[0], p), 0)
                else:
                    q = ((s, score[1]), (p, pos[1]), 1)
                fringe[q] = fringe.get(q, 0) + m

    ans = max(wins)
    return ans


data = '''
Player 1 starting position: 4
Player 2 starting position: 8
'''.strip()
assert part1(data) == 739785
assert part2(data) == 444356092776315


data = open('day21.in').read()
print(part1(data))
print(part2(data))