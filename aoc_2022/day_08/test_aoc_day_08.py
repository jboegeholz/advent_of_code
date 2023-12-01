import pytest


@pytest.mark.parametrize(
    "data, expected",
    [
        ([[1]], 1),
        ([[1, 1], [1, 1]], 4),
        ([[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]], 8),
        ([[1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]], 9),
        ([[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]], 12),
        ([[1, 1, 1, 1],
          [1, 2, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]], 13),
        ([[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 2, 1, 1],
          [1, 1, 1, 1]], 13),
        ([[1, 1, 1, 1],
          [1, 2, 1, 1],
          [1, 1, 3, 1],
          [1, 1, 1, 1]], 14),
        ([[1, 1, 1, 1, 1],
          [1, 2, 1, 1, 1],
          [1, 1, 3, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]], 18),
        ([[1, 1, 1, 1, 1],
          [1, 1, 4, 1, 1],
          [1, 4, 3, 4, 1],
          [1, 1, 4, 1, 1],
          [1, 1, 1, 1, 1]], 20),
        ([[3, 0, 3, 7, 3],
          [2, 5, 5, 1, 2],
          [6, 5, 3, 3, 2],
          [3, 3, 5, 4, 9],
          [3, 5, 3, 9, 0]], 21)

    ]
)
def test_current_dir(data, expected):
    trees_visible = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if row == 0 or row == len(data[row]) - 1 or col == 0 or col == len(data[row]) - 1:
                trees_visible += 1
            else:
                current = data[row][col]
                is_visible_s = True
                is_visible_e = True
                is_visible_w = True
                is_visible_n = True
                for k in range(row+1, len(data)):  # south
                    if data[k][col] >= current:
                        is_visible_s = False
                        break
                for k in range(col+1, len(data[row])):  # east
                    if data[row][k] >= current:
                        is_visible_e = False
                        break
                for k in range(0, col):  # west
                    if data[row][k] >= current:
                        is_visible_w = False
                        break
                for k in range(0, row):  # north
                    if data[k][col] >= current:
                        is_visible_n = False
                        break
                if is_visible_s or is_visible_e or is_visible_w or is_visible_n:
                    trees_visible += 1
    assert trees_visible == expected


def test_solution():
    data = []
    with open("aoc_data_08.txt") as file:
        for line in file:
            data.append([int(x) for x in line.strip("\n")])

    trees_visible = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if row == 0 or row == len(data[row]) - 1 or col == 0 or col == len(data[row]) - 1:
                trees_visible += 1
            else:
                current = data[row][col]
                is_visible_s = True
                is_visible_e = True
                is_visible_w = True
                is_visible_n = True
                for k in range(row + 1, len(data)):  # south
                    if data[k][col] >= current:
                        is_visible_s = False
                        break
                for k in range(col + 1, len(data[row])):  # east
                    if data[row][k] >= current:
                        is_visible_e = False
                        break
                for k in range(0, col):  # west
                    if data[row][k] >= current:
                        is_visible_w = False
                        break
                for k in range(0, row):  # north
                    if data[k][col] >= current:
                        is_visible_n = False
                        break
                if is_visible_s or is_visible_e or is_visible_w or is_visible_n:
                    trees_visible += 1

    assert trees_visible == 1708