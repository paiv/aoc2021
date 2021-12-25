#!/usr/bin/env python


def part1(data):
    lines = data.strip().splitlines()
    w,h = len(lines[0]), len(lines)
    mm = {'v':(1,0), '>':(0,1)}
    grid = {(y,x): mm[c] for y,s in enumerate(lines) for x,c in enumerate(s) if c in 'v>'}

    t = 0
    while True:
        t += 1
        # display(grid)

        dusk = grid
        dawn = dict()
        for (y,x),(dy,dx) in grid.items():
            ty,tx = (y+dy)%h, (x+dx)%w
            k = (ty,tx)
            if dx:
                if grid.get(k) is None:
                    dawn[k] = (dy,dx)
                else:
                    dawn[(y,x)] = (dy,dx)
            else:
                dawn[(y,x)] = (dy,dx)
        day = dict()
        for (y,x),(dy,dx) in dawn.items():
            ty,tx = (y+dy)%h, (x+dx)%w
            k = (ty,tx)
            if dy:
                if dawn.get(k) is None:
                    day[k] = (dy,dx)
                else:
                    day[(y,x)] = (dy,dx)
            else:
                day[(y,x)] = (dy,dx)
        grid = day
        if day == dusk: break

    return t


def display(grid):
    minx = min(x for y,x in grid)
    maxx = max(x for y,x in grid)
    miny = min(y for y,x in grid)
    maxy = max(y for y,x in grid)
    so = ''
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            k = (y,x)
            if (q := grid.get(k)):
                c = 'v' if q[0] else '>'
            else:
                c = '.'
            so += c
        so += '\n'
    print(so)


data = '''
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''
assert part1(data) == 58


data = open('day25.in').read()
print(part1(data))