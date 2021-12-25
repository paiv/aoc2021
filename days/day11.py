#!/usr/bin/env python

def part1(data, N=100):
    data = data.strip().splitlines()
    data = {(x+1j*y):int(c) for y, row in enumerate(data) for x,c in enumerate(row)}
    neib = (1, 1-1j, -1j, -1-1j, -1, -1+1j, 1j, 1+1j)
    ans = 0
    for _ in range(N):
        fringe = list()
        for k,v in data.items():
            data[k] = v + 1
            if v >= 9:
                fringe.append(k)
        seen = set()
        while fringe:
            k = fringe.pop()
            if k in seen: continue
            seen.add(k)
            data[k] += 1
            for s in neib:
                q = k + s
                if (v := data.get(q)) is not None:
                    data[q] = v + 1
                    if v >= 9:
                        fringe.append(q)
        ans += len(seen)
        for k,v in data.items():
            if v > 9: data[k] = 0
    return ans


def part2(data):
    data = data.strip().splitlines()
    data = {(x+1j*y):int(c) for y, row in enumerate(data) for x,c in enumerate(row)}
    neib = (1, 1-1j, -1j, -1-1j, -1, -1+1j, 1j, 1+1j)
    t = 0
    while True:
        t += 1
        fringe = list()
        for k,v in data.items():
            data[k] = v + 1
            if v >= 9:
                fringe.append(k)
        seen = set()
        while fringe:
            k = fringe.pop()
            if k in seen: continue
            seen.add(k)
            data[k] += 1
            for s in neib:
                q = k + s
                if (v := data.get(q)) is not None:
                    data[q] = v + 1
                    if v >= 9:
                        fringe.append(q)
        ans = 0
        for k,v in data.items():
            if v > 9:
                data[k] = 0
                ans += 1
        if ans == len(data):
            break
    return t


data = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''.strip()
assert part1(data) == 1656
assert part2(data) == 195


data = open('day11.in').read()
print(part1(data))
print(part2(data))