input_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""




def test_get_draw():
    draw = input_data.split("\n\n")[0]
    assert draw == "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"


def test_split_draw():
    draw = get_draw()
    assert draw == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def get_draw():
    draw = input_data.split("\n\n")[0]
    draw = draw.split(",")
    draw = [int(x) for x in draw]
    return draw


def test_get_first_board():
    boards = get_boards_from_data()
    board_one = convert_board(boards[1])

    assert board_one == [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7],
                         [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]]


def get_boards_from_data():
    boards = input_data.split("\n\n")
    return boards[1:] # ignore first


def convert_board(data):
    data = data.split("\n")
    board_one = []
    for n in data:
        row = n.split(" ")
        row = list(filter(None, row))
        row = [int(x) for x in row]
        board_one.append(row)
    return board_one


def test_draw_on_boards():
    boards = get_boards_from_data()
    converted_boards = []
    for board in boards:
        converted_boards.append(convert_board(board))

    draw = get_draw()

    for d in draw:
        for board in converted_boards:
            for row in board:
                for col in row:
                    if d == col:
                        print("found " + str(d))




if __name__ == '__main__':
    first, *draw = input_data.split("\n\n")
    print(first)
    #test_draw_on_boards()
