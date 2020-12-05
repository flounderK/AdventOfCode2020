#!/usr/bin/python3
import re


with open("input.txt", "r") as f:
    data = [i.replace("\n", " ") for i in f.read().strip().split("\n\n")]

optional_fields = {'cid'}
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
rexp = re.compile(r'([a-z]{3}):([^ ]+)')

valid = 0

for passport in data:
    matched_data = {i.groups() for i in re.finditer(rexp, passport)}
    passport_data = {k: v for k, v in matched_data}

    if set(passport_data.keys()).issuperset(required_fields):
        valid += 1


print("Part 1: %d" % valid)



