bingo_board = [[1, 2], [3, 4]]
bingo_board_check = [[0, 0], [0, 0]]
draw = [1, 2, 3, 4]


def test_bingo():
    for d in draw:
        for i, row in enumerate(bingo_board):
            for j, col in enumerate(row):
                if d == col:
                    print("found")
                    bingo_board_check[i][j] = 1


    print(bingo_board_check)


if __name__ == '__main__':
    test_bingo()