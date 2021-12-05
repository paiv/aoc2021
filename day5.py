#!/usr/bin/env python
import re
from collections import defaultdict


def part1(data):
    data = [list(map(int, re.findall(r'\d+', s))) for s in data.splitlines()]
    pois = defaultdict(int)
    for xa,ya, xb,yb in data:
        if xa == xb:
            for y in range(min(ya, yb), max(ya,yb)+1):
                pois[(xa,y)] += 1
        elif ya == yb:
            for x in range(min(xa, xb), max(xa,xb)+1):
                pois[(x,ya)] += 1
    return sum(v > 1 for v in pois.values())


def part2(data):
    data = [list(map(int, re.findall(r'\d+', s))) for s in data.splitlines()]
    def sig(x): return 1 if x > 0 else -1 if x < 0 else 0
    pois = defaultdict(int)
    for x,y, xb,yb in data:
        dx,dy = sig(xb-x), sig(yb-y)
        for _ in range(max(abs(xb-x), abs(yb-y))+1):
            pois[(x,y)] += 1
            x += dx
            y += dy
    return sum(v > 1 for v in pois.values())


data = '''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''.strip()
assert part1(data) == 5
assert part2(data) == 12


data = open('day5.in').read()
print(part1(data))
print(part2(data))