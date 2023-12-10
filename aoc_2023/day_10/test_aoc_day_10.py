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


def test_transform_maze():
    start_pos = ()
    maze = get_maze()
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == 'S':
                start_pos = [i, j]
                break

    maze[start_pos[0]][start_pos[1]] = '0'
    # follow right
    current_pos = start_pos
    current_pos[1] += 1
    if maze[current_pos[0]][current_pos[1]] == '-':
        maze[current_pos[0]][current_pos[1]] = '1'
        current_pos[1] += 1
    assert current_pos == [1, 3]

    if maze[current_pos[0]][current_pos[1]] == '7':
        maze[current_pos[0]][current_pos[1]] = '2'
        current_pos[0] += 1
    assert current_pos == [2, 3]

    if maze[current_pos[0]][current_pos[1]] == '|':
        maze[current_pos[0]][current_pos[1]] = '3'
        current_pos[0] += 1
    assert current_pos == [3, 3]

    if maze[current_pos[0]][current_pos[1]] == 'J':
        stop = True
        maze[current_pos[0]][current_pos[1]] = '4'

    output = [['.', '.', '.', '.', '.'],
    ['.', '0', '1', '2', '.'],
    ['.', '|', '.', '3', '.'],
    ['.', 'L', '-', '4', '.'],
    ['.', '.', '.', '.', '.']]
    assert maze == output


def test_get_max_steps():
    max_steps = 0

    assert max_steps == 4
