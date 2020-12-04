#!/usr/bin/python3
import re

rexp = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
with open("input.txt", "r") as f:
    c = [re.search(rexp, i).groups() for i in f.read().splitlines()]

valid_part_1 = valid_part_2 = 0
for mn, mx, char, string in c:
    mn = int(mn)
    mx = int(mx)
    if mn <= string.count(char) <= mx:
        valid_part_1 += 1

    if (string[mn-1] == char) ^ (string[mx-1] == char):
        valid_part_2 += 1

print("Part 1: %d" % valid_part_1)
print("Part 2: %d" % valid_part_2)
