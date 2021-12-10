#!/usr/bin/env python
import itertools
from collections import Counter


def part1(data):
    data = data.strip().splitlines()
    ans = 0
    for line in data:
        si,so = map(str.split, line.split('|'))
        ans += sum(len(s) in (2,3,4,7) for s in so)
    return ans


def part2(data):
    abc = 'abcdefg'
    book = list()
    for p in itertools.permutations(abc):
        a,b,c,d,e,f,g = p
        nums = [
            {a,b,c,e,f,g},
            {c,f},
            {a,c,d,e,g},
            {a,c,d,f,g},
            {b,c,d,f},
            {a,b,d,f,g},
            {a,b,d,e,f,g},
            {a,c,f},
            {a,b,c,d,e,f,g},
            {a,b,c,d,f,g},
        ]
        book.append(nums)

    data = data.strip().splitlines()
    ans = 0
    for line in data:
        si,so = map(str.split, line.split('|'))
        xs = list(map(set, si))
        for nums in book:
            if all(s in nums for s in xs):
                r = 0
                g = (next(i for i,n in enumerate(nums) if set(s) == n) for s in so)
                for x in g:
                    r = r * 10 + x
                ans += r
                break
    return ans


def display7(n1, n2, segments, theme='·#'):
    wires = [
        [(0,1), (0,2), (0,3), (0,4)],
        [(1,0), (2,0)],
        [(1,5), (2,5)],
        [(3,1), (3,2), (3,3), (3,4)],
        [(4,0), (5,0)],
        [(4,5), (5,5)],
        [(6,1), (6,2), (6,3), (6,4)],
    ]
    tr = {c:x for x,c in enumerate(segments)}
    U,V = theme[0], theme[1]
    def s7(n):
        m = [[U for _ in range(6)] for _ in range(7)]
        for c in n:
            for y,x in wires[tr[c]]:
                m[y][x] = c if U == V else V
        return [''.join(s) for s in m]
    xs = [s7(s) for s in n1 + [''] + n2]
    so = '\n'.join(' '.join(p) for p in zip(*xs))
    return so + '\n'


def part2(data):
    data = data.strip().splitlines()
    ans = 0
    for line in data:
        si,so = map(str.split, line.split('|'))
        xs = list(map(frozenset, si))
        x1 = next(x for x in xs if len(x) == 2)
        x4 = next(x for x in xs if len(x) == 4)
        x7 = next(x for x in xs if len(x) == 3)
        x8 = next(x for x in xs if len(x) == 7)
        xa = list(x7 - x1)
        xcf = list(x7 & x1)
        xbd = list(x4 - x1)
        xeg = list(x8 - x7 - x4)

        for x,y,z in itertools.product([0,1], repeat=3):
            a,c,f,b,d,e,g = xa[0], xcf[x], xcf[1-x], xbd[y], xbd[1-y], xeg[z], xeg[1-z]
            nums = {
                frozenset({a,b,c,e,f,g}):0,
                frozenset({c,f}):1,
                frozenset({a,c,d,e,g}):2,
                frozenset({a,c,d,f,g}):3,
                frozenset({b,c,d,f}):4,
                frozenset({a,b,d,f,g}):5,
                frozenset({a,b,d,e,f,g}):6,
                frozenset({a,c,f}):7,
                frozenset({a,b,c,d,e,f,g}):8,
                frozenset({a,b,c,d,f,g}):9,
            }
            # seg = (a,b,c,d,e,f,g)
            # print(display7(si, so, seg))
            if all(x in nums for x in xs):
                r = 0
                for s in map(frozenset, so):
                    r = r * 10 + nums[s]
                ans += r
                break
    return ans


def part2(data):
    data = data.strip().splitlines()
    ans = 0
    for line in data:
        si,so = map(str.split, line.split('|'))
        xs = sorted(map(frozenset, si), key=len)
        x1, x4, x7, x8 = xs[0], xs[2], xs[1], xs[9]
        fives, sixes = set(xs[3:6]), set(xs[6:9])
        for s in fives:
            if x1.issubset(s):
                x3 = s; fives.remove(s); break
        for s in sixes:
            if x3.issubset(s):
                x9 = s
            if not x1.issubset(s):
                x6 = s
        x0 = (sixes - {x6, x9}).pop()
        for s in fives:
            if s.issubset(x6):
                x5 = s
            else:
                x2 = s
        nums = {k:i for i,k in enumerate([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9])}
        r = 0
        for s in map(frozenset, so):
            r = r * 10 + nums[s]
        ans += r
    return ans


def part2(data):
    abc = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'
    cs = Counter(x for s in abc.split() for x in s)
    tr = {sum(cs[c] for c in s):i for i,s in enumerate(abc.split())}
    data = data.strip().splitlines()
    ans = 0
    for line in data:
        si,so = map(str.split, line.split('|'))
        cs = Counter(x for s in si for x in s)
        r = sum(10**i * tr[sum(cs[x] for x in s)] for i,s in enumerate(reversed(so)))
        ans += r
    return ans


data = '''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''.strip()
assert part1(data) == 26
assert part2(data) == 61229

data = '''
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
'''.strip()
assert part2(data) == 5353


data = open('day8.in').read()
print(part1(data))
print(part2(data))