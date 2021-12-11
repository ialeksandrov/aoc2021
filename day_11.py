import numpy as np


def adj(loc):
    adj_loc = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                pass
            elif (loc[0] + i) < 0 or (loc[1] + j) < 0 or (loc[0] + i) > 9 or (loc[1] + j) > 9:
                pass
            else:
                adj_loc.append([loc[0] + i, loc[1] + j])

    return adj_loc


def flash_count(file_path, sync):
    o_map = np.genfromtxt(file_path, dtype='int', delimiter=1)

    flash_count = 0

    for step in range(1, 1000):
        o_map += 1
        while o_map.max() > 9:
            flash = np.argwhere(o_map > 9)
            for loc in flash:
                o_map[loc[0], loc[1]] = 0
                for adj_loc in adj(loc):
                    if o_map[adj_loc[0], adj_loc[1]] != 0:
                        o_map[adj_loc[0], adj_loc[1]] += 1

        flash_count += np.count_nonzero(o_map == 0)

        if np.count_nonzero(o_map == 0) == 100:
            return step

        if step == 100 and not sync:
            return flash_count


def main():
    print(flash_count('input_11.txt', False))

    print(flash_count('input_11.txt', True))


if __name__ == '__main__':
    main()
