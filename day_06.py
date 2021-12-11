from collections import deque

with open('input_06.txt', 'r') as f:
    state = [int(i) for i in f.read().split(',')]

def part1_and_part2(days):
    totals = deque(state.count(i) for i in range(9))
    for _ in range(days):
        totals.rotate(-1)
        totals[6] += totals[8]
    return sum(totals)

print(part1_and_part2(80))
print(part1_and_part2(256))