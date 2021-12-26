#!/usr/bin/env python
import itertools
import readline
from collections import deque


def run_program(program, stdin=None):
    regs = regs = {'w':0, 'x':0, 'y':0, 'z':0}
    if not isinstance(stdin, deque):
        stdin = deque(stdin or [])
    stdout = deque()

    def var(x):
        if isinstance(x, int):
            return x
        return regs[x]

    def op_add(x, y):
        regs[x] = var(x) + var(y)

    def op_mul(x, y):
        regs[x] = var(x) * var(y)

    def op_div(x, y):
        regs[x] = var(x) // var(y)

    def op_mod(x, y):
        regs[x] = var(x) % var(y)

    def op_eql(x, y):
        regs[x] = 1 if var(x) == var(y) else 0

    def op_inp(x, y):
        if stdin:
            regs[x] = stdin.popleft()
        else:
            regs[x] = int(input('> '))

    opcodes = {
        'inp': op_inp,
        'mul': op_mul,
        'eql': op_eql,
        'add': op_add,
        'div': op_div,
        'mod': op_mod,
    }

    for op,x,y in program:
        opcodes[op](x, y)

    return regs


def parse_program(data):
    prog = list()
    for s in data.strip().splitlines():
        op, *args = s.split()
        if len(args) < 2:
            args.append(None)
        elif args[-1][-1].isdigit():
            args[-1] = int(args[-1])
        prog.append((op, *args))
    return prog


def run_test(data, input, ans):
    program = parse_program(data)
    regs = run_program(program, input)
    return regs[ans]


data = '''
inp x
mul x -1
'''
assert run_test(data, [3], 'x') == -3
assert run_test(data, [0], 'x') == 0
assert run_test(data, [-11], 'x') == 11

data = '''
inp z
inp x
mul z 3
eql z x
'''
assert run_test(data, [1, 3], 'z') == 1
assert run_test(data, [1, 2], 'z') == 0
assert run_test(data, [3, 9], 'z') == 1

data = '''
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
'''
assert run_test(data, [0], 'z') == 0
assert run_test(data, [1], 'z') == 1
assert run_test(data, [1], 'y') == 0
assert run_test(data, [2], 'z') == 0
assert run_test(data, [2], 'y') == 1
assert run_test(data, [3], 'z') == 1
assert run_test(data, [3], 'y') == 1
assert run_test(data, [3], 'x') == 0
assert run_test(data, [4], 'x') == 1
assert run_test(data, [4], 'w') == 0
assert run_test(data, [8], 'w') == 1


def brute(data, reverse=False):
    lines = data.strip().splitlines()
    params = [[lines[i+4], lines[i+5], lines[i+15]] for i in range(0, len(lines), 18)]
    params = [[int(s.split()[-1]) for s in p] for p in params]
    u,t,q = zip(*params)

    iq = set(i for i,x in enumerate(u) if x == 26)
    seed = list(range(1,10))
    if reverse:
        seed = seed[::-1]
    for p in itertools.product(seed, repeat=(len(u)-len(iq))):
        xs = list()
        z = 0
        pi = 0
        for i in range(len(u)):
            if i in iq:
                w = z % 26 + t[i]
                if not (0 < w < 10):
                    break
            else:
                w = p[pi]
                pi += 1
            x = (z % 26 + t[i]) != w
            z = (z // u[i]) * (25 * x + 1) + (w + q[i]) * x
            xs.append(w)
        else:
            if z == 0:
                return xs


def solve(data, reverse):
    p = brute(data, reverse)
    z = run_test(data, p, 'z')
    assert z == 0, (z, p)
    return sum((10**i * x) for i,x in enumerate(reversed(p)))


def solve(data, reverse):
    lines = data.strip().splitlines()
    params = [[lines[i+4], lines[i+5], lines[i+15]] for i in range(0, len(lines), 18)]
    params = [[int(s.split()[-1]) for s in p] for p in params]

    p = [None] * len(params)
    stack = list()
    for i,(u,t,q) in enumerate(params):
        if u == 1:
            stack.append((i,q))
        else:
            j,q = stack.pop()
            if reverse:
                p[j] = 9 - max(0, q+t)
                p[i] = 9 + min(0, q+t)
            else:
                p[j] = 1 - min(0, q+t)
                p[i] = 1 + max(0, q+t)

    z = run_test(data, p, 'z')
    assert z == 0, (z, p)
    return sum((10**i * x) for i,x in enumerate(reversed(p)))


def sat_solve(data, reverse):
    import z3
    lines = data.strip().splitlines()
    params = [[lines[i+4], lines[i+5], lines[i+15]] for i in range(0, len(lines), 18)]
    params = [[int(s.split()[-1]) for s in p] for p in params]

    opt = z3.Optimize()
    v = 0
    z = 0
    for i, (a,b,c) in enumerate(params):
        w = z3.Int(f'w{i}')
        v = v * 10 + w
        opt.add(z3.And(0 < w, w < 10))
        z = z3.If(z % 26 + b != w, z / a * 26 + w + c, z / a)
    opt.add(z == 0)
    f = (opt.maximize if reverse else opt.minimize)
    f(v)
    assert opt.check() == z3.sat
    return opt.model().eval(v)


def part1(data): return solve(data, True)
def part2(data): return solve(data, False)


data = open('day24.in').read()
print(part1(data))
print(part2(data))