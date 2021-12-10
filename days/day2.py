#!/usr/bin/env python

def part1(data):
    pos = dep = 0
    for s in data.splitlines():
        op, v = s.split()
        v = int(v)
        if op == 'forward':
            pos += v
        elif op == 'down':
            dep += v
        elif op == 'up':
            dep -= v
    return pos * dep


def part2(data):
    pos = aim = dep = 0
    for s in data.splitlines():
        op, v = s.split()
        v = int(v)
        if op == 'forward':
            pos += v
            dep += aim * v
        elif op == 'down':
            aim += v
        elif op == 'up':
            aim -= v
    return pos * dep


data = '''
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''.strip()
assert part1(data) == 150
assert part2(data) == 900


data = open('day2.in').read()
print(part1(data))
print(part2(data))