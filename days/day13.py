#!/usr/bin/env python

def part1(data):
    dots, ops = data.split('\n\n')
    dots = [[*map(int, s.split(','))] for s in dots.split()]
    grid = dict()
    for x,y in dots:
        grid[(x,y)] = 1
    for op in ops.strip().splitlines():
        axis, n = op.split()[-1].split('=')
        n = int(n)
        folded = dict()
        for (x,y),v in grid.items():
            if axis == 'x':
                k = (min(x, 2 * n - x), y)
            else:
                k = (x, min(y, 2 * n - y))
            folded[k] = 1
        grid = folded
        break
    ans = sum(grid.values())
    return ans


def display(grid):
    minx = min(x for x,y in grid.keys())
    maxx = max(x for x,y in grid.keys())
    miny = min(y for x,y in grid.keys())
    maxy = max(y for x,y in grid.keys())
    so = ''
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            so += '.#'[grid.get((x,y),0)]
        so += '\n'
    print(so)


def part2(data):
    dots, ops = data.split('\n\n')
    dots = [[*map(int, s.split(','))] for s in dots.split()]
    grid = dict()
    for x,y in dots:
        grid[(x,y)] = 1
    for op in ops.strip().splitlines():
        axis, n = op.split()[-1].split('=')
        n = int(n)
        folded = dict()
        for (x,y),v in grid.items():
            if axis == 'x':
                k = (min(x, 2 * n - x), y)
            else:
                k = (x, min(y, 2 * n - y))
            folded[k] = 1
        grid = folded
    display(grid)
    return 0


data = '''
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''.strip()
assert part1(data) == 17
assert part2(data) == 0


data = open('day13.in').read()
print(part1(data))
print(part2(data))


def generate(image, N=10):
    import random
    rr = random.randrange
    dots = [(x,y) for y,s in enumerate(image.strip().splitlines())
        for x,c in enumerate(s) if c == '#']
    minx = min(x for x,y in dots)
    maxx = max(x for x,y in dots)
    miny = min(y for x,y in dots)
    maxy = max(y for x,y in dots)
    ops = list()
    for i in range(N):
        if (i > 1) and (i % 2):
            q = maxx + 1
            ops.append(('x', q))
            dots = [(2 * q - x, y) if rr(2) else (x,y) for x,y in dots]
            maxx = 2 * q - minx
        else:
            q = maxy + 1
            ops.append(('y', q))
            dots = [(x, 2 * q - y) if rr(2) else (x,y) for x,y in dots]
            maxy = 2 * q - miny
    sa = '\n'.join(','.join(map(str, p)) for p in dots)
    sb = '\n'.join('fold along ' + '='.join(map(str, p)) for p in reversed(ops))
    print(sa + '\n\n' + sb)


# generate('''
# ..#.....#.....#.....#.....#.....#..
# ...#...#.......#...#.......#...#...
# ..#######.....#######.....#######..
# .##.###.##...##.###.##...##.###.##.
# ###########.###########.###########
# #.#######.#.#.#######.#.#.#######.#
# #.#.....#.#.#.#.....#.#.#.#.....#.#
# ...##.##.......##.##.......##.##...
# ''')