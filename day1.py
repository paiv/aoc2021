#!/usr/bin/env python

def part1(data):
    xs = list(map(int, data.split()))
    return sum(y > x for x,y in zip(xs, xs[1:]))


def part2(data):
    xs = list(map(int, data.split()))
    ys = [sum(xs[i:i+3]) for i in range(len(xs)-2)]
    return sum(y > x for x,y in zip(ys, ys[1:]))


data = '''
199
200
208
210
200
207
240
269
260
263
'''.strip()
assert part1(data) == 7
assert part2(data) == 5


data = open('day1.in').read()
print(part1(data))
print(part2(data))