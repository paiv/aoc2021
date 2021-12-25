#!/usr/bin/env python


def display(grid):
    minx = int(min(p.real for p in grid.keys()))
    maxx = int(max(p.real for p in grid.keys()))
    miny = int(min(p.imag for p in grid.keys()))
    maxy = int(max(p.imag for p in grid.keys()))
    so = ''
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            so += '.#'[grid.get((x+y*1j),0)]
        so += '\n'
    print(so)


def solve(data, N):
    alg,img = data.split('\n\n')
    alg = {x for x,c in enumerate(''.join(alg.split())) if c == '#'}
    flashing = 0 in alg
    grid = {(x+y*1j):(c == '#') for y,r in enumerate(img.strip().splitlines()) for x,c in enumerate(r)}
    neib = (-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j)
    def sig(k, grid, bg):
        i = 0
        for s in neib:
            i = (i << 1) | grid.get((k+s),bg)
        return i
    for t in range(N):
        dawn = dict()
        fringe = set(grid.keys())
        seen = set()
        while fringe:
            k = fringe.pop()
            if k in seen: continue
            seen.add(k)
            q = sig(k, grid, (t%2 if flashing else 0))
            dawn[k] = q in alg
            if k in grid:
                for s in neib:
                    fringe.add(k + s)
        grid = dawn
    ans = sum(grid.values())
    return ans


part1 = lambda data: solve(data, 2)
part2 = lambda data: solve(data, 50)


data = '''
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''.strip()
assert part1(data) == 35
assert part2(data) == 3351


data = open('day20.in').read()
print(part1(data))
print(part2(data))