#!/usr/bin/env python

def part1(data):
    data = data.strip().splitlines()
    ns = [(s.count('0'), s.count('1')) for s in zip(*data)]
    gamma = sum((int(x < y) << i) for i,(x, y) in enumerate(ns[::-1]))
    epsilon = sum((int(x > y) << i) for i,(x, y) in enumerate(ns[::-1]))
    return gamma * epsilon


def part2(data):
    data = data.strip().splitlines()
    oxy = data.copy()
    co2 = data.copy()

    for i in range(len(data[0])):
        if len(oxy) > 1:
            q = '10'[2 * sum(s[i]=='0' for s in oxy) > len(oxy)]
            oxy = [s for s in oxy if s[i] == q]
        if len(co2) > 1:
            q = '01'[2 * sum(s[i]=='0' for s in co2) > len(co2)]
            co2 = [s for s in co2 if s[i] == q]

    oxy = int(''.join(oxy[0]), 2)
    co2 = int(''.join(co2[0]), 2)
    return oxy * co2


data = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''.strip()
assert part1(data) == 198
assert part2(data) == 230


data = open('day3.in').read()
print(part1(data))
print(part2(data))