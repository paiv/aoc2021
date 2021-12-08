#!/usr/bin/env python
import itertools
from collections import defaultdict


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