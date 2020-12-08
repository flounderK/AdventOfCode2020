#!/usr/bin/python3

with open("input.txt", "r") as f:
    data = [i for i in f.read().split('\n\n')]


anyone_answered_yes_groups = []
everyone_answered_yes_groups = []
for group_response in data:
    anyone_answered_yes = set(group_response.replace('\n', ''))
    anyone_answered_yes_groups.append(anyone_answered_yes)
    everyone_answered_yes = []
    for answered_q in anyone_answered_yes:
        if all([(answered_q in i) for i in group_response.splitlines()]):
            everyone_answered_yes.append(answered_q)
    everyone_answered_yes_groups.append(everyone_answered_yes)

part_1_res = sum([len(i) for i in anyone_answered_yes_groups])
print("Part 1: %d" % part_1_res)
part_2_res = sum([len(i) for i in everyone_answered_yes_groups])
print("Part 2: %d" % part_2_res)
