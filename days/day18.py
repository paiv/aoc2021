#!/usr/bin/env python
import itertools
from functools import reduce


def explode(xs):
    def inner(xs, lvl):
        if isinstance(xs, int):
            return False, xs, None, None
        a,b = xs
        if lvl == 4:
            return True, 0, a, b
        t, a, u, v = inner(a, lvl+1)
        if t: return t, [a, add_left(b, v)], u, None
        t, b, u, v = inner(b, lvl+1)
        if t: return t, [add_right(a, u), b], None, v
        return False, xs, None, None

    def add_left(xs, x):
        if x is None:
            return xs
        if isinstance(xs, int):
            return xs + x
        a,b = xs
        return [add_left(a, x), b]

    def add_right(xs, x):
        if x is None:
            return xs
        if isinstance(xs, int):
            return xs + x
        a,b = xs
        return [a, add_right(b, x)]

    t, res, _,_ = inner(xs, 0)
    return t,res


assert explode([0,0]) == (False, [0,0])
assert explode([[[[[9,8],1],2],3],4]) == (True, [[[[0,9],2],3],4])
assert explode([7,[6,[5,[4,[3,2]]]]]) == (True, [7,[6,[5,[7,0]]]])
assert explode([[6,[5,[4,[3,2]]]],1]) == (True, [[6,[5,[7,0]]],3])
assert explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == (True, [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
assert explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == (True, [[3,[2,[8,0]]],[9,[5,[7,0]]]])


def split(xs):
    if isinstance(xs, int):
        if xs > 9:
            return True, [xs // 2, (xs + 1) // 2]
        return False, xs
    a,b = xs
    t, a = split(a)
    if not t:
        t, b = split(b)
    return t, [a,b]


assert split([0,9]) == (False, [0,9])
assert split([0,10]) == (True, [0,[5,5]])
assert split([0,11]) == (True, [0,[5,6]])
assert split([0,12]) == (True, [0,[6,6]])


def snail_reduce(xs):
    while True:
        t,xs = explode(xs)
        if not t:
            t,xs = split(xs)
        if not t: break
    return xs


assert snail_reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]


def snail_sum(a, b):
    return snail_reduce([a, b])


def magnitude(xs):
    if isinstance(xs, int):
        return xs
    a,b = xs
    return 3 * magnitude(a) + 2 * magnitude(b)


def part1(data):
    xs = reduce(snail_sum, map(eval, data.strip().splitlines()))
    ans = magnitude(xs)
    return ans


def part2(data):
    xs = list(map(eval, data.strip().splitlines()))
    ans = 0
    for a,b in itertools.combinations(xs, 2):
        ans = max(ans, magnitude(snail_sum(a,b)))
        ans = max(ans, magnitude(snail_sum(b,a)))
    return ans


assert part1('[[1,2],[[3,4],5]]') == 143
assert part1('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]') == 3488


data = '''
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
'''.strip()
assert part1(data) == 4140
assert part2(data) == 3993


data = open('day18.in').read()
print(part1(data))
print(part2(data))