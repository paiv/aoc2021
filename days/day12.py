#!/usr/bin/env python
from collections import defaultdict, deque


def part1(data):
    grid = defaultdict(set)
    for a,b in (s.split('-') for s in data.strip().splitlines()):
        grid[a].add(b)
        grid[b].add(a)
    ans = 0
    fringe = deque([('start', set())])
    while fringe:
        s,seen = fringe.popleft()
        if s == 'end':
            ans += 1
            continue
        if s in seen: continue
        if s.islower(): seen.add(s)
        for d in grid[s]:
            fringe.append((d, seen.copy()))
    return ans


def part2(data):
    grid = defaultdict(set)
    for a,b in (s.split('-') for s in data.strip().splitlines()):
        if b != 'start':
            grid[a].add(b)
        if a != 'start':
            grid[b].add(a)
    ans = 0
    fringe = deque([('start', set(), False)])
    while fringe:
        s,seen,p = fringe.popleft()
        if s == 'end':
            ans += 1
            continue
        if s in seen:
            if p: continue
            p = True
        if s.islower(): seen.add(s)
        for d in grid[s]:
            fringe.append((d, seen.copy(), p))
    return ans


data = '''
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''.strip()
assert part1(data) == 10
assert part2(data) == 36

data = '''
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''.strip()
assert part1(data) == 19
assert part2(data) == 103

data = '''
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''.strip()
assert part1(data) == 226
assert part2(data) == 3509


data = open('day12.in').read()
print(part1(data))
print(part2(data))