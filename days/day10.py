#!/usr/bin/env python

def part1(data):
    score = {')':3, ']':57, '}':1197, '>':25137}
    ans = 0
    pair = dict(zip('>}])', '<{[('))
    for line in data.strip().splitlines():
        stack = list()
        for s in line:
            if (q := pair.get(s)):
                if (not stack) or (x := stack.pop()) != q:
                    ans += score[s]
                    break
            else:
                stack.append(s)
    return ans


def part2(data):
    score = {'(':1, '[':2, '{':3, '<':4}
    res = list()
    pair = dict(zip('>}])', '<{[('))
    for line in data.strip().splitlines():
        stack = list()
        for s in line:
            if (q := pair.get(s)):
                if (not stack) or (x := stack.pop()) != q:
                    break
            else:
                stack.append(s)
        else:
            ans = sum(5**i * score[s] for i,s in enumerate(stack))
            res.append(ans)
    ans = sorted(res)[len(res)//2]
    return ans


data = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''.strip()
assert part1(data) == 26397
assert part2(data) == 288957


data = open('day10.in').read()
print(part1(data))
print(part2(data))