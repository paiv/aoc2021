#!/usr/bin/env julia

@views function part1(data)
    xs = parse.(Int, split(data))
    sum(y > x for (x,y) in zip(xs, xs[2:end]))
end


@views function part2(data)
    xs = parse.(Int, split(data))
    sum(y > x for (x,y) in zip(xs, xs[4:end]))
end


data = """
199
200
208
210
200
207
240
269
260
263
"""
@assert(part1(data) == 7)
@assert(part2(data) == 5)


data = readchomp("day1.in")
println(part1(data))
println(part2(data))