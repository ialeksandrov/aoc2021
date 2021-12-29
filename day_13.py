def make_board(max_x, max_y, dots):
    board = [["."] * (max_x + 1) for x in range(max_y + 1)]
    for x, y in dots:
        board[y][x] = "#"
    return board


def draw_board(board, blank="."):
    for line in board:
        print("".join([blank if x == "." else "#" for x in line]))


data = open("input_13.txt").read().strip().split("\n")
max_x = max_y = 0
dots = []
folds = []
for line in data:
    if line.startswith("fold"):
        dirc, amt = line.split(" ")[-1].split("=")
        folds.append((dirc, int(amt)))
    elif line != "":
        x, y = line.split(",")
        max_x = int(x) if int(x) > max_x else max_x
        max_y = int(y) if int(y) > max_y else max_y
        dots.append((int(x), int(y)))

board = make_board(max_x, max_y, dots)
fold = 0
for dirc, amt in folds:
    fold += 1
    if dirc == "y":
        split = board[amt + 1 :][::-1]
        board = board[:amt]
        # adjust for uneven folds
        if len(split) > len(board):
            board = [["."] * len(split[0])] * (len(split) - len(board)) + board
        elif len(board) > len(split):
            split = [["."] * len(board[0])] * (len(board) - len(split)) + split
    else:
        split = [x[amt + 1 :][::-1] for x in board]
        board = [x[:amt] for x in board]
        # adjust for uneven folds
        if len(split[0]) > len(board[0]):
            x = ["x"] * 3 + x
            board = [["."] * len(split[0]) - len(board[0]) + board for x in board]
        elif len(board) > len(split):
            split = [["."] * len(board[0]) - len(split[0]) + split for x in split]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if split[y][x] == "#":
                board[y][x] = "#"
    if fold == 1:
        print(f"Part 1: {sum([line.count('#') for line in board])}")
print(f"Part 2:")
draw_board(board, blank=" ")