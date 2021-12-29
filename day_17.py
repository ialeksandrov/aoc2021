from collections import defaultdict


data = open("input_17.txt").read().strip()
x_range, y_range = data.split(": ")[1].split(", ")
x_lower, x_upper = x_range.split("=")[1].split("..")
x_lower, x_upper = int(x_lower), int(x_upper)
y_lower, y_upper = y_range.split("=")[1].split("..")
y_lower, y_upper = int(y_lower), int(y_upper)


def poi(x_velo, y_velo, area):
    step = 0
    x, y = (0, 0)
    max_y = 0
    while True:
        if step > 0:
            if x_velo > 0:
                x_velo -= 1
            elif x_velo < 0:
                x_velo += 1
            else:
                x_velo = 0
            y_velo -= 1
        x += x_velo
        y += y_velo
        max_y = y if y > max_y else max_y

        if x < -area or x > x_upper:
            break
        if y < y_lower or y > area:
            break
        if x_lower <= x <= x_upper and y_lower <= y <= y_upper:
            return max_y

        step += 1


x_velo_min = 0
pos = 0
while pos < x_lower:
    x_velo_min += 1
    pos += x_velo_min

velos = defaultdict(int)
for x_velo in range(x_velo_min, x_upper + 1):
    for y_velo in range(-7500, 7500):
        hit = poi(x_velo, y_velo, 7500)
        if hit != None:
            velos[(x_velo, y_velo)] = hit

p1 = max(velos, key=velos.get)
print(f"Part 1: {velos[p1]} @ {p1}")
print(f"Part 2: {len(velos)}")