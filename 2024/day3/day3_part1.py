#!/usr/bin/env python3

import re
from pathlib import Path

def parse_and_sum_mul_expressions(file_path):

    pattern = re.compile(r"mul\((\d{1,3}),\s*(\d{1,3})\)")

    total_sum = 0  # To store the sum of all products

    with Path(file_path).open() as file:
        for line_number, line in enumerate(file, start=1):
            matches = pattern.findall(line)  # Find all matches in the current line
            for x, y in matches:
                product = int(x) * int(y)  # Multiply X and Y
                total_sum += product  # Add the product to the running total
                print(f"mul({x}, {y}) on line {line_number} -> Product: {product}")

    return total_sum

file_path = "day3input.txt"
total = parse_and_sum_mul_expressions(file_path)
print("Total sum of all products:", total)
