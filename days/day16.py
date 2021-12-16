#!/usr/bin/env python
from binascii import unhexlify
from functools import reduce


def parse_packet(bits):
    i = 0
    while i + 6 < len(bits):
        ver = int(bits[i:i+3], 2)
        i += 3
        pid = int(bits[i:i+3], 2)
        i += 3
        if pid == 4:
            x = 0
            while True:
                s,c = bits[i], bits[i+1:i+5]
                i += 5
                x = (x << 4) | int(c, 2)
                if s != '1': break
            yield (ver, pid, x, i)
        else:
            t = int(bits[i])
            i += 1
            if t == 0:
                if i + 15 >= len(bits): break
                plen = int(bits[i:i+15], 2)
                i += 15
                pps = list(parse_packet(bits[i:i+plen]))
                i += plen
                yield (ver, pid, pps, i)
            else:
                nsub = int(bits[i:i+11], 2)
                i += 11
                pps = list()
                for _ in range(nsub):
                    sv, sp, ss, j = next(parse_packet(bits[i:]))
                    pps.append((sv, sp, ss, i + j))
                    i += j
                yield (ver, pid, pps, i)


def part1(data):
    bits = ''.join(f'{x:08b}' for x in unhexlify(data.strip()))

    def inner(ps):
        ans = 0
        for v,p,pps,_ in ps:
            ans += v
            if p != 4:
                ans += inner(pps)
        return ans

    ans = inner([*parse_packet(bits)])
    return ans


def part2(data):
    bits = ''.join(f'{x:08b}' for x in unhexlify(data.strip()))

    def eval(ps):
        v,p,pps,_ = ps
        if p == 4:
            return pps
        elif p == 0:
            return sum(map(eval, pps))
        elif p == 1:
            return reduce(int.__mul__, map(eval, pps))
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

    ans = eval(next(parse_packet(bits)))
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