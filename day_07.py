with open('input_07.txt', 'r') as f:
    arr = [int(i) for i in f.read().split(',')]
    start, end = min(arr), max(arr) + 1


def get_cost(a, b):
    n = abs(a - b)
    return (n*(n+1))//2


def part1():
    costs = []
    for pos in range(start, end):
        costs.append(sum(abs(i - pos) for i in arr))
    return min(costs)


def part2():
    costs = []
    for pos in range(start, end):
        costs.append(sum(get_cost(i, pos) for i in arr))
    return min(costs)


print(part1())
print(part2())
