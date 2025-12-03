# Read File
from pathlib import Path

def count_zero_passes(filename, start=50):
    """
    Count how many times the dial passes over 0 (including landings) while
    applying moves from filename. Each line is like 'L5' or 'R12'.
    """
    zeros = 0
    combo = start

    path = Path(filename)
    with path.open("r") as file:
        for line in file:
            direction = line[0]
            amount = int(line[1:])

            if direction == "L":
                first_hit = combo if combo != 0 else 100  # steps to next 0 moving left
                zero_hits = 1 + (amount - first_hit) // 100 if amount >= first_hit else 0
                combo = (combo - amount) % 100
            else:
                first_hit = (100 - combo) % 100
                first_hit = first_hit or 100  # steps to next 0 moving right
                zero_hits = 1 + (amount - first_hit) // 100 if amount >= first_hit else 0
                combo = (combo + amount) % 100

            zeros += zero_hits

    return zeros


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    print(count_zero_passes(here / "input.txt"))
