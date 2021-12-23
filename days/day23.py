#!/usr/bin/env python
import heapq
import sys
import time

TracePaths = 0


def solve(data, patch):
    lines = data.strip().splitlines()
    if patch:
        y = next(y for y,s in enumerate(lines) if any(map(str.isalpha, s)))
        lines.insert(y+1, '  #D#B#A#C#')
        lines.insert(y+1, '  #D#C#B#A#')
    grid = {(y,x):('.' if c.isalpha() else c) for y,s in enumerate(lines) for x,c in enumerate(s) if not c.isspace()}
    hallway = {(y,x) for y,s in enumerate(lines) for x,c in enumerate(s) if c == '.'}
    rooms = {(y,x) for y,s in enumerate(lines) for x,c in enumerate(s) if c.isalpha()}
    halls = hallway | rooms
    roomsy = min(y for y,x in rooms)
    roomsx = dict(zip('ABCD', sorted(set(x for y,x in rooms))))
    restricted = {(roomsy-1,x) for y,x in rooms}
    pods = [((y,x),c) for y,s in enumerate(lines) for x,c in enumerate(s) if c.isalpha()]
    energies = dict(zip('ABCD', [1,10,100,1000]))
    names = [c for p,c in pods]
    pods = [p for p,c in pods]
    E = [energies[c] for c in names]
    G = [roomsx[c] for c in names]
    neib = [(0,1), (-1,0), (0,-1), (1,0)]

    def isgoal(pos):
        return all( ((p[0] >= roomsy) and (p[1] == G[i])) for i,p in enumerate(pos))

    def search_from(ix, start, pos):
        py,px = start
        if start in rooms:
            if (px == G[ix]) and all(G[i] == G[ix] for i,(y,x) in enumerate(pos) if (x == px) and (y > py)):
                return
            goals = hallway - restricted - set(pos)
        else:
            if any( ((x == G[ix]) and (G[i] != G[ix])) for i,(y,x) in enumerate(pos)):
                return
            goals = set((y,x) for y,x in rooms if x == G[ix]) - set(pos)
            if goals:
                goals = sorted(goals)[-1:]
        if not goals: return

        e = E[ix]
        fringe = [(0, start)]
        seen = set()
        walkable = halls - set(pos)
        while fringe:
            u,p = fringe.pop()
            if p in seen: continue
            seen.add(p)
            if p in goals:
                t = list(pos)
                t[ix] = p
                yield (u, tuple(t))
            y,x = p
            for dy,dx in neib:
                q = (y+dy, x+dx)
                if q not in walkable: continue
                fringe.append((u+e, q))

    def findpaths(pos):
        for i,p in enumerate(pos):
            yield from search_from(i, p, pos)

    pos = tuple(pods)
    seen = set()
    if TracePaths:
        display(grid, pods, names)
        fringe = [(0, pos, (pos,))]
        while fringe:
            eng,pos,path = heapq.heappop(fringe)
            if pos in seen: continue
            seen.add(pos)
            if isgoal(pos):
                display(grid, pos, names)
                print(path)
                print(eng)
                return eng
            for e,p in findpaths(pos):
                heapq.heappush(fringe, (eng+e, p, path+(p,)))
    else:
        fringe = [(0, pos)]
        while fringe:
            eng,pos = heapq.heappop(fringe)
            if pos in seen: continue
            seen.add(pos)
            if isgoal(pos):
                return eng
            for e,p in findpaths(pos):
                heapq.heappush(fringe, (eng+e, p))


def display(grid, pos, names):
    minx = min(x for y,x in grid)
    maxx = max(x for y,x in grid)
    miny = min(y for y,x in grid)
    maxy = max(y for y,x in grid)
    ps = set(pos)
    so = ''
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            k = (y,x)
            c = grid.get(k, ' ')
            if k in ps:
                c = names[pos.index(k)]
            so += c
        so += '\n'
    print(so)


def replay(data, patch, path):
    lines = data.strip().splitlines()
    if patch:
        y = next(y for y,s in enumerate(lines) if any(map(str.isalpha, s)))
        lines.insert(y+1, '  #D#B#A#C#')
        lines.insert(y+1, '  #D#C#B#A#')
    grid = {(y,x):('.' if c.isalpha() else c) for y,s in enumerate(lines) for x,c in enumerate(s) if not c.isspace()}
    pods = [((y,x),c) for y,s in enumerate(lines) for x,c in enumerate(s) if c.isalpha()]
    names = [c for p,c in pods]
    for p in path:
        display(grid, p, names)
        time.sleep(1)


def part1(data): return solve(data, False)
def part2(data): return solve(data, True)


if (len(sys.argv) > 1) and (sys.argv[1] == '-r'):
    data = open('day23.in').read()
    ps = eval(sys.stdin.read())
    replay(data, True, ps)
    exit(0)


data = '''
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
'''
if TracePaths:
    assert part1(data) == 12521
    assert part2(data) == 44169


data = open('day23.in').read()
print(part1(data))
print(part2(data))