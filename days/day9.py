#!/usr/bin/env python

def part1(data):
    data = data.strip().splitlines()
    data = {(x+1j*y):int(c) for y, row in enumerate(data) for x,c in enumerate(row)}
    neib = (1, -1, 1j, -1j)
    inf = float('inf')
    ans = sum(x+1 for p,x in data.items() if all(x < data.get(p+s, inf) for s in neib))
    return ans


def part2(data):
    data = data.strip().splitlines()
    data = {(x+1j*y):int(c) for y, row in enumerate(data) for x,c in enumerate(row)}
    neib = (1, -1, 1j, -1j)
    inf,ninf = float('inf'), float('-inf')
    mins = [(p,x) for p,x in data.items() if all(x < data.get(p+s,inf) for s in neib)]
    res = list()
    for p,x in mins:
        fringe = [(p,x)]
        seen = set()
        while fringe:
            p,x = fringe.pop()
            if x == 9 or p in seen: continue
            seen.add(p)
            for s in neib:
                if (y := data.get(p+s, ninf)) > x:
                    fringe.append((p+s, y))
        res.append(len(seen))
    x,y,z = sorted(res)[-3:]
    ans = x * y * z
    return ans


data = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''.strip()
assert part1(data) == 15
assert part2(data) == 1134


data = open('day9.in').read()
print(part1(data))
print(part2(data))