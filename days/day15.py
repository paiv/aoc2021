#!/usr/bin/env python
import heapq


def part1(data):
    data = data.strip().splitlines()
    w,h = len(data[0]), len(data)
    data = {(y,x):int(c) for y, row in enumerate(data) for x,c in enumerate(row)}
    neib = ((0,1), (-1,0), (0,-1), (1,0))
    goal = (h-1, w-1)
    fringe = [(0, (0,0))]
    seen = set()
    while fringe:
        n, k = heapq.heappop(fringe)
        if k == goal:
            return n
        if k in seen: continue
        seen.add(k)
        for sy,sx in neib:
            q = (k[0] + sy, k[1] + sx)
            if (v := data.get(q)) is not None:
                heapq.heappush(fringe, (n + v, q))


def part2(data):
    data = data.strip().splitlines()
    w,h = len(data[0]), len(data)
    data = {(y,x):int(c) for y, row in enumerate(data) for x,c in enumerate(row)}
    for ny in range(5):
        for nx in range(5):
            if not (ny or nx): continue
            for y in range(h):
                for x in range(w):
                    v = data[(y,x)]
                    v = (((v-1) + ny + nx) % 9) + 1
                    q = (ny * h + y, nx * w + x)
                    data[q] = v
    neib = ((0,1), (-1,0), (0,-1), (1,0))
    goal = (h*5-1, w*5-1)
    fringe = [(0, (0,0))]
    seen = set()
    while fringe:
        n, k = heapq.heappop(fringe)
        if k == goal:
            return n
        if k in seen: continue
        seen.add(k)
        for sy,sx in neib:
            q = (k[0] + sy, k[1] + sx)
            if (v := data.get(q)) is not None:
                heapq.heappush(fringe, (n + v, q))


data = '''
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''.strip()
assert part1(data) == 40
assert part2(data) == 315


data = open('day15.in').read()
print(part1(data))
print(part2(data))