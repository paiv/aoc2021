#!/usr/bin/env python

def part1(data, N=80):
    xs = list(map(int, data.split(',')))
    for _ in range(N):
        n = xs.count(0)
        for i,x in enumerate(xs):
            xs[i] = x - 1 if x > 0 else 6
        xs.extend([8] * n)
    return len(xs)


def part2(data, N=256):
    data = list(map(int, data.split(',')))
    ps = [0] * 10
    for x in data:
        ps[x] += 1
    for _ in range(N):
        t = ps[0]
        for i in range(8):
            ps[i] = ps[i+1]
        ps[8] = t
        ps[6] += t
    return sum(ps)


data = '''
3,4,3,1,2
'''.strip()
assert part1(data) == 5934
assert part2(data) == 26984457539


data = open('day6.in').read()
print(part1(data))
print(part2(data))


def npsolve(data, N):
    import numpy as np
    xs = list(map(int, data.split(',')))
    x = np.zeros((9,), dtype=np.int64)
    for n in xs:
        x[n] += 1
    a = np.zeros((9,9), dtype=np.int64)
    for i in range(8):
        a[i,i+1] = 1
    a[6,0] = 1
    a[8,0] = 1
    a = np.linalg.matrix_power(a, N)
    return np.sum(a * x)


def analysis(data):
    Ns = list(range(0, 51, 1))
    print('N =', ' '.join(map(str, Ns)))
    for q in list(range(6)) + [8]:
        print([q], end=' ')
        for N in Ns:
            xs = list(map(int, data.split(',')))
            xs = [q]
            for _ in range(N):
                n = xs.count(0)
                for i,x in enumerate(xs):
                    xs[i] = x - 1 if x > 0 else 6
                xs.extend([8] * n)
            print(len(xs), end=' ')
        print()