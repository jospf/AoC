#!/usr/bin/env python3

# Part 1
file_name = "day1input.txt"

col1 = []
col2 = []

with open(file_name, 'r') as file:
    for line in file:
        values = line.split()
        col1.append(int(values[0]))
        col2.append(int(values[1]))

#sort the columns
col1_sorted = sorted(col1)
col2_sorted = sorted(col2)

running_tally = 0
for a, b, in zip(col1_sorted, col2_sorted):
    running_tally += abs(int(a) - int(b))

print(running_tally)

#Part 2
cumulative_sum = 0
for element in col1_sorted:
    count = col2_sorted.count(element)
    cumulative_sum += element * count

print(cumulative_sum)
