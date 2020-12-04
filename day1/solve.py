#!/usr/bin/python3

with open("input.txt", "r") as f:
    c = [int(i) for i in f.read().splitlines()]

[part1] = {x*y for x in c for y in c if x + y == 2020}
print("Part 1: %d" % part1)

[part2] = {x*y*z for x in c for y in c for z in c if x + y + z == 2020}
print("Part 2: %d" % part2)

