from collections import defaultdict

import pytest

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

@pytest.mark.parametrize(
    "data, expected",
    [
        ("""$ cd /""", ["/"]),
        ("""$ cd /\n$ cd a""", ["/", "a"]),
        ("""$ cd /\n$ cd a\n$ cd ..""", ["/"]),
        (input, ["/", "d"]),
    ]
)
def test_current_dir(data, expected):
    current_dir = []
    commands = data.split("\n")
    for command in commands:
        if "cd" in command:
            folder = command.split("$ cd ")[1]
            if folder == "..":
                current_dir.pop()
            else:
                current_dir.append(folder)
    assert current_dir == expected

@pytest.mark.parametrize(
    "data, expected",
    [
        ("""$ cd /""", {"/": {}}),
        ("""$ cd /\n$ ls\ndir a""", {"/": {"dir a": {}}}),
        ("""$ ls\ndir a\ndir b""", {"/": {"dir a": {}, "dir b": {}}}),
        ("""$ ls\n14848514 b.txt""", {"/": {"b.txt": 14848514}}),

    ]
)
def test_parse_commands(data, expected):
    dir_tree = {"/": {}}
    current_dir = []
    commands = data.split("\n")
    for command in commands:

        if "cd" in command:
            folder = command.split("$ cd ")[1]
            if folder == "..":
                current_dir.pop()
            else:
                current_dir.append(folder)
        elif "dir" in command:
            dir_tree["/"][command] = {}
        elif "ls" in command:
            continue
        else:
            file_size = command.split(" ")[0]
            file_name = command.split(" ")[1]
            dir_tree["/"][file_name] = int(file_size)
    assert dir_tree == expected

