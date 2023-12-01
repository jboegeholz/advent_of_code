import pytest

data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

expected_output = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""


def test_signal_strength_test_data():
    crt_line = ""
    sprite_position = 1
    cycle_counter = 0
    for op in data.split("\n"):

        if op == "noop":

            if cycle_counter == 40:
                crt_line += '\n'
                cycle_counter = 0
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1
        if "addx" in op:
            if cycle_counter == 40:
                crt_line += '\n'
                cycle_counter = 0
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1
            if cycle_counter == 40:
                crt_line += '\n'
                cycle_counter = 0
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1

            sprite_position += int(op.split(" ")[1])
    assert crt_line == expected_output


@pytest.mark.parametrize(
    "data, expected_crt_line",
    [
        ("addx 15", "##"),
        ("addx 15\naddx -11", "##.."),
        ("addx 15\naddx -11\naddx 6", "##..##"),
        ("addx 15\naddx -11\naddx 6\naddx -3", "##..##.."),
        ("addx 15\naddx -11\naddx 6\naddx -3\naddx 5", "##..##..##"),
        ("addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop", "##..##..##"),

    ]
)
def test_signal_strength(data, expected_crt_line):
    crt_line = ""
    sprite_position = 1
    cycle_counter = 0
    for op in data.split("\n"):
        if op == "noop":
            cycle_counter += 1
            # check match
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'

        if "addx" in op:

            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1
            sprite_position += int(op.split(" ")[1])
    assert crt_line == expected_crt_line


def test_signal_strength_test_data_from_file():
    with open("aoc_data_010.txt", "r") as f:
        data = f.read()

    crt_line = ""
    sprite_position = 1
    cycle_counter = 0
    for op in data.split("\n"):

        if op == "noop":

            if cycle_counter == 40:
                crt_line += '\n'
                cycle_counter = 0
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1
        if "addx" in op:
            if cycle_counter == 40:
                crt_line += '\n'
                cycle_counter = 0
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1
            if cycle_counter == 40:
                crt_line += '\n'
                cycle_counter = 0
            if cycle_counter in [sprite_position-1, sprite_position, sprite_position+1]:
                crt_line += '#'
            else:
                crt_line += '.'
            cycle_counter += 1

            sprite_position += int(op.split(" ")[1])
    assert crt_line == """###..####.###...##..####.####...##.###..
                        #..#....#.#..#.#..#....#.#.......#.#..#.
                        #..#...#..###..#......#..###.....#.###..
                        ###...#...#..#.#.##..#...#.......#.#..#.
                        #....#....#..#.#..#.#....#....#..#.#..#.
                        #....####.###...###.####.####..##..###.."""
