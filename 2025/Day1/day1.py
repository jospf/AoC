# Read File
zeros = 0
combo = 50

with open('input.txt', 'r') as file:
    for line in file:      # Loop through file, reading each line
        if line[0] == 'L':
            combo = (combo - int(line[1:])) % 100
            if combo == 0:
                zeros += 1
        else:
            combo = (combo + int(line[1:])) % 100
            if combo == 0:
                zeros += 1
print(zeros)

# Count 0


