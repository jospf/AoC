from bisect import bisect_left, bisect_right

with open("input.txt", "r", encoding="utf-8") as infile:
    parts = infile.read().strip().split(",")

ranges = []
max_end = 0

for part in parts:
    if not part:
        continue
    start_str, end_str = part.split("-")
    start, end = int(start_str), int(end_str)
    ranges.append((start, end))
    if end > max_end:
        max_end = end

repeated_set = set()
max_digits = len(str(max_end))

for block_len in range(1, max_digits + 1):
    max_repeats = max_digits // block_len
    if max_repeats < 2:
        continue
    pow_block = 10 ** block_len
    block_start = pow_block // 10
    for repeats in range(2, max_repeats + 1):
        pow_total = 10 ** (block_len * repeats)
        multiplier = (pow_total - 1) // (pow_block - 1)
        limit_block = min(pow_block - 1, max_end // multiplier)
        if block_start > limit_block:
            continue
        for block in range(block_start, limit_block + 1):
            repeated_set.add(block * multiplier)

repeated_numbers = sorted(repeated_set)

prefix_sums = [0]
for num in repeated_numbers:
    prefix_sums.append(prefix_sums[-1] + num)

total = 0
for start, end in ranges:
    left = bisect_left(repeated_numbers, start)
    right = bisect_right(repeated_numbers, end)
    total += prefix_sums[right] - prefix_sums[left]

print(total)
