data = """.....
.S-7.
.|.|.
.L-J.
....."""


def test_get_maze():
    maze = []
    for line in data.split("\n"):
        maze.append(list(line))
    assert maze == [['.', '.', '.', '.', '.'],
                    ['.', 'S', '-', '7', '.'],
                    ['.', '|', '.', '|', '.'],
                    ['.', 'L', '-', 'J', '.'],
                    ['.', '.', '.', '.', '.']]


def test_get_max_steps():
    max_steps = 0

    assert max_steps == 4
