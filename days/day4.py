#!/usr/bin/env python
from functools import reduce


def part1(data):
    draw, *boards = data.split('\n\n')
    draw = list(map(int, draw.split(',')))
    boards = [[[*map(int, l.split())] for l in s.splitlines()] for s in boards]
    boards = [[[set(row) for row in q] for q in [b, zip(*b)]] for b in boards]

    called = set()
    for x in draw:
        called.add(x)
        for ps in boards:
            for rows in ps:
                if any(r.issubset(called) for r in rows):
                    ns = reduce(set.union, rows)
                    unmarked = sum(ns - called)
                    return x * unmarked


def part2(data):
    draw, *boards = data.split('\n\n')
    draw = list(map(int, draw.split(',')))
    boards = [[[*map(int, l.split())] for l in s.splitlines()] for s in boards]
    boards = [[[set(row) for row in q] for q in [b, zip(*b)]] for b in boards]

    ans = 0
    wins = set()
    called = set()
    for x in draw:
        called.add(x)
        for i, ps in enumerate(boards):
            if i in wins: continue
            for rows in ps:
                if any(r.issubset(called) for r in rows):
                    wins.add(i)
                    ns = reduce(set.union, rows)
                    unmarked = sum(ns - called)
                    ans = x * unmarked
    return ans


data = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.strip()
assert part1(data) == 4512
assert part2(data) == 1924


data = open('day4.in').read()
print(part1(data))
print(part2(data))