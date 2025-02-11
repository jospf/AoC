#!/usr/bin/env python3
#AoC 2024 Day 2 Python
from pathlib import Path

file_path = Path("day2input.txt")  # Adjust to your file's location
valid_count = 0

def process_line(line):
    numbers = list(map(int, line.split()))

    increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    valid_differences = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

    return increasing or decreasing, valid_differences

with Path(file_path).open() as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()
        is_sorted, valid_diff = process_line(line)

        if is_sorted and valid_diff:
            valid_count +=1

print(valid_count)

