#!/usr/bin/env python
import re


def part1(data):
    xmin,xmax,ymin,ymax = map(int, re.findall(r'-?\d+', data))
    rx = range(xmin, xmax+1)
    ry = range(ymin, ymax+1)
    ans = 0
    for oy in range(ymin, -ymin*2):
        for ox in range(xmax+1):
            vx,vy = ox,oy
            px = py = 0
            top = py
            while py >= ymin and px <= xmax:
                px += vx
                py += vy
                top = max(top, py)
                if (px in rx) and (py in ry):
                    ans = max(ans, top)
                    break
                vx -= 1 if vx else 0
                vy -= 1
    return ans


def part2(data):
    xmin,xmax,ymin,ymax = map(int, re.findall(r'-?\d+', data))
    rx = range(xmin, xmax+1)
    ry = range(ymin, ymax+1)
    ans = 0
    for oy in range(ymin, -ymin*2):
        for ox in range(xmax+1):
            vx,vy = ox,oy
            px = py = 0
            while py >= ymin and px <= xmax:
                px += vx
                py += vy
                if (px in rx) and (py in ry):
                    ans += 1
                    break
                vx -= 1 if vx else 0
                vy -= 1
    return ans


data = '''
target area: x=20..30, y=-10..-5
'''.strip()
assert part1(data) == 45
assert part2(data) == 112


data = open('day17.in').read()
print(part1(data))
print(part2(data))