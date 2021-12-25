#!/usr/bin/env python
from collections import Counter


def part1(data, N=10):
    tpl, rules = data.split('\n\n')
    rules = dict([[x.strip() for x in s.split('->')] for s in rules.strip().splitlines()])
    for _ in range(N):
        so = ''
        for a,b in zip(tpl, tpl[1:]):
            so += a
            k = a + b
            if (q := rules.get(k)):
                so += q
        tpl = so + b
    c = Counter(tpl)
    m = c.most_common()
    ans = m[0][1] - m[-1][1]
    return ans


def part2(data, N=40):
    tpl, rules = data.split('\n\n')
    rules = dict([[x.strip() for x in s.split('->')] for s in rules.strip().splitlines()])
    terms = set(x for k,v in rules.items() for x in k + v)
    terms = {k:i for i,k in enumerate(terms)}
    irules = {(terms[k[0]], terms[k[1]]):terms[s] for k, s in rules.items()}

    adj = [[0] * len(terms) for _ in range(len(terms))]
    for a,b in zip(tpl, tpl[1:]):
        adj[terms[a]][terms[b]] += 1

    for _ in range(N):
        z = [r.copy() for r in adj]
        for k, s in irules.items():
            a,b = k
            n = adj[a][b]
            z[a][b] -= n
            z[a][s] += n
            z[s][b] += n
        adj = z

    xs = [sum(r) for r in zip(*adj)]
    xs[terms[tpl[0]]] += 1
    a, b = min(xs), max(xs)
    ans = b - a
    return ans


data = '''
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''.strip()
assert part1(data) == 1588
assert part2(data) == 2188189693529


data = open('day14.in').read()
print(part1(data))
print(part2(data))