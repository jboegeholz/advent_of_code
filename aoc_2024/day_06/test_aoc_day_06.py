import pytest



def test_convert_input():
    data = "..\n.."
    converted = convert_input_to_2d_array(data)
    assert [['.', '.'], ['.', '.']] == converted


def convert_input_to_2d_array(data):
    converted = []
    for line in data.split("\n"):
        converted.append(list(line))
    return converted

def test_move_upward():
    map = [['.', '.'],
           ['.', '^']]
    for i, row in enumerate(map):
        for j, col in enumerate(map[i]):
            if col == '^':
                map[i-1][j] = '^'
                map[i][j] = 'X'
    assert map == [['.', '^'],
                   ['.', 'X']]

@pytest.mark.parametrize(
    "input_data, expected",
    [
      #  ([['.', '.'], ['.', '^']], [['.', '^'], ['.', 'X']]),
        ([['.', '.'], ['>', '.']], [['.', '.'], ['X', '>']]),


    ]
)
def test_is_correct_order(input_data, expected):
    map = input_data
    rows = len(map)
    columns = len(map[0])
    for i in range(rows):
        for j in range(columns):
            if map[i][j] == '^':
                map[i][j] = 'X'
                if i < rows:
                    map[i-1][j] = '^'
            if map[i][j] == '>':
                map[i][j] = 'X'
                if j < columns-1:
                    map[i][j+1] = '>'

    assert map == expected





