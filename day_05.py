from collections import Counter

data = open("input_05.txt").read().strip().split("\n")
pts1 = []
pts2 = []
for line in data:
    x1, y1 = tuple(int(x) for x in line.split(" -> ")[0].split(","))
    x2, y2 = tuple(int(x) for x in line.split(" -> ")[1].split(","))

    # part 1
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                pts1.append((x, y))
                pts2.append((x, y))
    # part 2
    else:
        xinc = 1 if x1 < x2 else -1
        yinc = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + xinc, xinc):
            pts2.append((x, y))
            y += yinc

p1_dupes = [pt for pt in Counter(pts1).values() if pt > 1]
print(f"Part 1: {len(p1_dupes)}")
p2_dupes = [pt for pt in Counter(pts2).values() if pt > 1]
print(f"Part 2: {len(p2_dupes)}")