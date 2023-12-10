data = """.....
.S-7.
.|.|.
.L-J.
....."""

def get_maze():
    maze = []
    for line in data.split("\n"):
        maze.append(list(line))
    return maze

def test_get_maze():
    maze = get_maze()
    assert maze == [['.', '.', '.', '.', '.'],
                    ['.', 'S', '-', '7', '.'],
                    ['.', '|', '.', '|', '.'],
                    ['.', 'L', '-', 'J', '.'],
                    ['.', '.', '.', '.', '.']]


def test_get_start_pos():
    start_pos = ()
    maze = get_maze()
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == 'S':
                start_pos = (i, j)
                break
    assert start_pos == (1, 1)




def test_get_max_steps():
    max_steps = 0

    assert max_steps == 4
