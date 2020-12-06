#!/usr/bin/python3
import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

parsed_data = []
seat_ids = []
for i in data:
    line = re.sub('[FL]', '0', i)
    line = re.sub('[BR]', '1', line)
    row = int(line[:7], 2)
    col = int(line[7:], 2)
    parsed_data.append((row, col))
    seat_ids.append((row*8) + col)

print("Part 1: %d" % max(seat_ids))

seat_ids.sort()
last_seat = None
for s in range(0, len(seat_ids)):
    if last_seat is None:
        last_seat = seat_ids[s]
        continue

    if last_seat + 1 != seat_ids[s]:
        found_seat = last_seat + 1
        break

    last_seat = seat_ids[s]

print("Part 2: %d" % found_seat)

