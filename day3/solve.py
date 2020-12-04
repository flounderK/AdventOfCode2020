#!/usr/bin/python3
from functools import reduce


def count_trees_on_slope(right, down, data):
    repeatable_size = len(data[0])
    trees = 0
    col = 0
    for row in range(0, len(data), down):
        if data[row][col % repeatable_size] == '#':
            trees += 1
        col += right
    return trees


with open("input.txt", "r") as f:
    c = f.read().splitlines()

print("Part 1: %d" % count_trees_on_slope(3, 1, c))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees_on_slopes = [count_trees_on_slope(right, down, c) for right, down in slopes]
part_2_result = reduce(lambda x, y: x*y, trees_on_slopes)
print("Part 2: %d" % part_2_result)

