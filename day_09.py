def get_neighbvals(i, j, numbers):
    m, n = len(numbers) - 1, len(numbers[0]) - 1
    return [numbers[i - 1][j] if i > 0 else 9,
            numbers[i][j + 1] if j < n else 9,
            numbers[i + 1][j] if i < m else 9,
            numbers[i][j - 1] if j > 0 else 9]


def get_neighbours(i, j, numbers):
    m, n = len(numbers) - 1, len(numbers[0]) - 1
    neigh = {(i - 1, j) if (i > 0 and numbers[i - 1][j] != 9) else None,
             (i, j + 1) if (j < n and numbers[i][j + 1] != 9) else None,
             (i + 1, j) if (i < m and numbers[i + 1][j] != 9) else None,
             (i, j - 1) if (j > 0 and numbers[i][j - 1] != 9) else None}
    return neigh.difference({None})


def part_one(numbers):
    m, n = len(numbers) - 1, len(numbers[0]) - 1
    result = 0
    lowpoints = []
    for i, line in enumerate(numbers):
        for j, num in enumerate(line):
            if num == 9:
                continue
            neigh = get_neighbvals(i, j, numbers)
            if all(num < val for val in neigh):
                result += num + 1
                lowpoints.append((i, j))
    return result, lowpoints


def count_basin(i, j, numbers, basin, unexplored):
    # Get the neighbours to this value
    neigh = get_neighbours(i, j, numbers)

    # Remove existing neighbours and add unexplored
    newneigh = neigh.difference(basin)
    newneigh.update(unexplored)

    # Update the basin with new neighbours
    basin.update(newneigh)

    # End recursion
    if len(newneigh) == 0:
        return len(basin)

    # Choose the next smallest value
    minneigh = 9
    for ind, (i, j) in enumerate(newneigh):
        if numbers[i][j] < minneigh:
            minneigh = numbers[i][j]

    newneigh.remove((i, j))
    return count_basin(i, j, numbers, basin, newneigh)


def part_two(numbers):
    # Extract the minimum points from part one
    _, lowpoints = part_one(numbers)

    basins = set()
    for i, j in lowpoints:
        size = count_basin(i, j, numbers, {(i, j)}, [])
        basins.add(size)

    # Get the product of the three max O(n*size) (avoid sorting)
    result = 1
    for i in range(3):
        maxbasin = max(basins)
        basins.remove(maxbasin)
        result *= maxbasin
    return result


if __name__ == '__main__':
    with open('input_09.txt') as f:
        numbers = [list(map(int, line.strip())) for line in f]
    result, _ = part_one(numbers)
    print(result)
    result = part_two(numbers)
    print(result)
