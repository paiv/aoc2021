#!/usr/bin/env python
import itertools
import re


def part1(data):
    parts = dict()
    for n, s in re.findall(r'^(\w+):\s*(.*?)$', data, re.M):
        parts[n] = tuple((p,int(x)) for x, p in re.findall(r'(\d+)\s+(\w+)', s))

    def count(p):
        xs = parts.get(p)
        if not xs: return 1
        return sum(x * count(q) for q, x in xs)

    return max(map(count, parts))


def part2(data, T=20):
    N = int(re.search(r'\d+', data)[0])
    print(N, T)

    parts = dict()
    for n, s in re.findall(r'^(\w+):\s*(.*?)$', data, re.M):
        parts[n] = tuple((p,int(x)) for x, p in re.findall(r'(\d+)\s+(\w+)', s))
        print(n)
        for p,x in parts[n]:
            print(' ', x, p)

    toys = set(parts) - set(p for ps in parts.values() for p,_ in ps)
    toys = {p:v for p,v in parts.items() if p in toys}
    print('toys', toys)

    def count(p):
        xs = parts.get(p)
        if not xs: return 1
        return sum(x * count(q) for q, x in xs)

    xs = sorted(((count(p),p) for p in toys), reverse=True)
    print(xs)

    for ps in itertools.combinations_with_replacement(xs, T):
        n = sum(x for x,_ in ps)
        if n == N:
            ans = ''.join(sorted(p[0] for _,p in ps))
            print(ans)
            # return ans
    return ans


data = '''
35 onderdelen missen
Zoink: 9 Oink, 5 Dink
Floep: 2 Flap, 4 Dink
Flap: 4 Oink, 3 Dink
'''.strip()
assert part1(data) == 18
# assert part2(data, 3) == 'FZZ'


data = open('input.txt').read()
print(part1(data))
print(part2(data))