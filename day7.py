#!/usr/bin/env python

def part1(data):
    xs = list(map(int, data.split(',')))
    best = float('inf')
    for q in set(xs):
        m = sum(abs(q-x) for x in xs)
        best = min(best, m)
    return best


def part2(data):
    xs = list(map(int, data.split(',')))
    r = sum(xs) // len(xs)
    best = float('inf')
    for q in range(r - 2, r + 3):
        m = sum((p+1)*p//2 for x in xs for p in [abs(q-x)])
        best = min(best, m)
    return best


data = '''
16,1,2,0,4,2,7,1,2,14
'''.strip()
assert part1(data) == 37
assert part2(data) == 168


data = open('day7.in').read()
print(part1(data))
print(part2(data))