if __name__ == '__main__':
    dial_value = 50
    zero_counter = 0
    with open('data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        assert len(lines) == 4392
        for line in lines:
            rot_value = int(line[1:])
            if line[0] == "L":
                dial_value = dial_value - rot_value
                if dial_value < 0:
                    zero_counter += 1
                dial_value = dial_value % 100
            elif line[0] == "R":
                dial_value = dial_value + rot_value
                if dial_value > 100:
                    zero_counter += 1
                dial_value = dial_value % 100
            else:
                print("should not happen")
            if dial_value == 0:
                zero_counter += 1
            print(dial_value)
    print(zero_counter)
    assert zero_counter == 5530
