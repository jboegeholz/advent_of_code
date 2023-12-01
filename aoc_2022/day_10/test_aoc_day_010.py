import pytest


@pytest.mark.parametrize(
    "data, register_x_expected, cycle_counter_expected, signal_strength",
    [
        ("noop\naddx 3\naddx -5", -1, 5, -5),

    ]
)
def test_signal_strength(data, register_x_expected, cycle_counter_expected, signal_strength):
    register_x = 1
    cycle_counter = 0
    for op in data.split("\n"):
        if op == "noop":
            cycle_counter += 1
            continue
        if "addx" in op:
            cycle_counter += 2
            register_x += int(op.split(" ")[1])
    assert register_x == register_x_expected
    assert cycle_counter == cycle_counter_expected


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

def test_signal_strength_test_data():
    signal_probes = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    register_x = 1
    cycle_counter = 0
    for op in data.split("\n"):
        if op == "noop":
            cycle_counter += 1
            if cycle_counter in signal_probes:
                signal_strength += cycle_counter * register_x
            continue
        if "addx" in op:
            cycle_counter += 1
            if cycle_counter in signal_probes:
                signal_strength += cycle_counter * register_x
            cycle_counter += 1
            if cycle_counter in signal_probes:
                signal_strength += cycle_counter * register_x
            register_x += int(op.split(" ")[1])
    assert signal_strength == 13140

def test_signal_strength_test_data_from_file():
    with open("aoc_data_010.txt", "r") as f:
        data = f.read()
    signal_probes = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    register_x = 1
    cycle_counter = 0
    for op in data.split("\n"):
        if op == "noop":
            cycle_counter += 1
            if cycle_counter in signal_probes:
                signal_strength += cycle_counter * register_x
            continue
        if "addx" in op:
            cycle_counter += 1
            if cycle_counter in signal_probes:
                signal_strength += cycle_counter * register_x
            cycle_counter += 1
            if cycle_counter in signal_probes:
                signal_strength += cycle_counter * register_x
            register_x += int(op.split(" ")[1])
    assert signal_strength == 13140