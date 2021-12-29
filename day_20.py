from itertools import product
from typing import Generator


def parse_input(filepath):
    with open(filepath, "r") as f:
        algorithm, image = f.read().split("\n\n")
        image_map = {}
        for y, row in enumerate(image.split("\n")):
            for x, col in enumerate(row):
                image_map[complex(x, y)] = col
    return algorithm, image_map


def binary_to_dec(bin_number):
    return int(bin_number, 2)


def str_to_bin(arr: list[str]) -> list[str]:
    return ["0" if i == "." else "1" for i in arr]


def get_edges(image_map: dict[complex, str]) -> tuple[int, ...]:
    x_min, y_min, x_max, y_max = (
        float("inf"),
        float("inf"),
        float("-inf"),
        float("-inf"),
    )
    for position in image_map:
        x = position.real
        y = position.imag
        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    return tuple(map(int, (x_min, y_min, x_max, y_max)))


def get_adjacent(
        coordinate: complex,
        window=(
                complex(-1, -1),
                complex(0, -1),
                complex(1, -1),
                complex(-1, 0),
                complex(0, 0),
                complex(1, 0),
                complex(-1, 1),
                complex(0, 1),
                complex(1, 1),
        ),
) -> Generator[complex, None, None]:
    for adjacent in window:
        yield coordinate + adjacent


def process_image(image, algorithm, nth_iteration=None):
    edges = get_edges(image)
    if nth_iteration:
        default = "#" if nth_iteration % 2 != 0 else "."
    else:
        default = "."
    new_map = {}
    for x, y in product(
            range(edges[0] - 1, edges[2] + 2), range(edges[1] - 1, edges[3] + 2)
    ):
        next_num = [image.get(coord, default) for coord in get_adjacent(complex(x, y))]
        next_num_bin = "".join(str_to_bin(next_num))
        algo_idx_int = binary_to_dec(next_num_bin)
        new_map[complex(x, y)] = algorithm[algo_idx_int]
    return new_map


def sum_image(img) -> int:
    n = 0
    for val in img.values():
        if val == "#":
            n += 1
    return n


def part_a():
    fp = r"input_20.txt"
    algo, img = parse_input(fp)

    for i in range(2):
        img = process_image(img, algo, i)
    return sum_image(img)


def part_b():
    fp = r"input_20.txt"
    algo, img = parse_input(fp)

    for i in range(50):
        img = process_image(img, algo, i)
    return sum_image(img)


if __name__ == "__main__":
    print(part_a())
    print(part_b())