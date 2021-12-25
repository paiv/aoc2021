#!/usr/bin/env python
import math
from itertools import islice


def parse_packet(bits):
    def iint(g, w):
        x = 0
        for i in islice(g, w):
            x = (x << 1) | i
        return x

    while True:
        ver = iint(bits, 3)
        pid = iint(bits, 3)
        if pid == 4:
            x = 0
            while True:
                s = iint(bits, 1)
                c = iint(bits, 4)
                x = (x << 4) | c
                if not s: break
            yield (ver, pid, x)
        else:
            if iint(bits, 1):
                nsub = iint(bits, 11)
                ps = list(islice(parse_packet(bits), nsub))
                yield (ver, pid, ps)
            else:
                plen = iint(bits, 15)
                if not plen: break
                ps = list(parse_packet(islice(bits, plen)))
                yield (ver, pid, ps)


def bitstream(hx):
    return ((v>>i)&1 for s in hx.strip()
        for v in[int(s,16)] for i in range(3,-1,-1))


def dump_packet(text):
    print(text)
    print(''.join(map(str, bitstream(text))))
    p = next(parse_packet(bitstream(text)))
    print(p)


def part1(data):
    def inner(ps):
        ans = 0
        for v,p,pps in ps:
            ans += v
            if p != 4:
                ans += inner(pps)
        return ans

    ans = inner([*parse_packet(bitstream(data))])
    return ans


def part2(data):
    def eval(ps):
        v,p,pps = ps
        if p == 4:
            return pps
        elif p == 0:
            return sum(map(eval, pps))
        elif p == 1:
            return math.prod(map(eval, pps))
        elif p == 2:
            return min(map(eval, pps))
        elif p == 3:
            return max(map(eval, pps))
        elif p == 5:
            a,b = pps
            return 1 if eval(a) > eval(b) else 0
        elif p == 6:
            a,b = pps
            return 1 if eval(a) < eval(b) else 0
        elif p == 7:
            a,b = pps
            return 1 if eval(a) == eval(b) else 0

    ans = eval(next(parse_packet(bitstream(data))))
    return ans


assert part1('38006F45291200') == 9
assert part1('EE00D40C823060') == 14
assert part1('8A004A801A8002F478') == 16
assert part1('620080001611562C8802118E34') == 12
assert part1('C0015000016115A2E0802F182340') == 23
assert part1('A0016C880162017C3686B18A3D4780') == 31


assert part2('C200B40A82') == 3
assert part2('04005AC33890') == 54
assert part2('880086C3E88112') == 7
assert part2('CE00C43D881120') == 9
assert part2('D8005AC2A8F0') == 1
assert part2('F600BC2D8F') == 0
assert part2('9C005AC2F8F0') == 0
assert part2('9C0141080250320F1802104A08') == 1


data = open('day16.in').read()
print(part1(data))
print(part2(data))