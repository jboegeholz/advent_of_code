test_stacks = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"]
]

test_moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_move_all_container():
    for move_input in test_moves.split("\n"):
        move = [int(x) for x in move_input.split(" ") if x.isdigit()]
        amount = move[0]
        src = move[1] - 1
        dst = move[2] - 1
        items = []
        for i in range(amount):
            items.append(test_stacks[src].pop())
        items.reverse()
        test_stacks[dst].extend(items)
    end = [
        ["M"],
        ["C"],
        ["P", "Z", "N", "D"]
    ]
    assert test_stacks == end


stacks = [
    ["N", "S", "D", "C", "V", "Q", "T"],
    ["M", "F", "V"],
    ["F", "Q", "W", "D", "P", "N", "H", "M"],
    ["D", "Q", "R", "T", "F"],
    ["R", "F", "M", "N", "Q", "H", "V", "B"],
    ["C", "F", "G", "N", "P", "W", "Q"],
    ["W", "F", "R", "L", "C", "T"],
    ["T", "Z", "N", "S"],
    ["M", "S", "D", "J", "R", "Q", "H", "N"],
]


def test_move_all_container_from_file():
    with open("aoc_data_05.txt", "r") as f:
        moves = f.read()
    for move_input in moves.split("\n"):
        move = [int(x) for x in move_input.split(" ") if x.isdigit()]
        amount = move[0]
        src = move[1] - 1
        dst = move[2] - 1
        items = []
        for i in range(amount):
            items.append(stacks[src].pop())
        items.reverse()
        stacks[dst].extend(items)

    top_crates = ""
    for stack in stacks:
        top_crates += stack.pop()
    assert top_crates == "HRFTQVWNN"