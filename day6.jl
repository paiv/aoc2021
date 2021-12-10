#!/usr/bin/env julia


function solve(data, N)
    xs = parse.(Int, split(data, ','))
    x = zeros(Int, 9)
    @views x[xs.+1] .+= 1
    a = zeros(Int, 9, 9)
    for i = 1:8
        a[i, i+1] = 1
    end
    a[[7,9],1] .= 1
    sum(a ^ N * x)
end


part1(data) = solve(data, 80)
part2(data) = solve(data, 256)


data = """
3,4,3,1,2
"""
@assert(part1(data) == 5934)
@assert(part2(data) == 26984457539)


data = readchomp("day6.in")
println(part1(data))
println(part2(data))