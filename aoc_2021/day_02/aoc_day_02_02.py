"""
     a   d
f 5  0   0
d 5  5
f 8  5  40
u 3  2
d 8  10
f 2  10  20

After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

"""

if __name__ == '__main__':

    with open("./aoc_day_02_data.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    horizontal = 0
    current_aim = 0
    depth = 0
    for line in lines:
        print(line)
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            horizontal += value
            depth += value * current_aim
        if command == "down":
            current_aim += value
        if command == "up":
            current_aim += value * -1

    print(f"horizontal: {horizontal}")
    print(f"depth: {depth}")
    print(horizontal * depth)
