with open('input_02.txt', 'r') as file:
    lines = file.readlines()

horizontal_position = 0
depth = 0

for line in lines:
    instruction, value = line.split()

    if instruction == "forward":
        horizontal_position += int(value)
    elif instruction == "down":
        depth += int(value)
    elif instruction == "up":
        depth -= int(value)

print(horizontal_position * depth)


horizontal = 0
depth = 0
aim = 0

for line in lines:
    instruction, value = line.split()

    if instruction == "forward":
        horizontal += int(value)
        depth += aim * int(value)
    elif instruction == "down":
        aim += int(value)
    elif instruction == "up":
        aim -= int(value)

print(horizontal * depth)
