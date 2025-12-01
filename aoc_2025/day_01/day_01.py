if __name__ == '__main__':
    dial_value = 50
    zero_counter = 0
    with open('data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
            if line[0] == "L":
                dial_value = dial_value - int(line[1:])
                dial_value += 100
                dial_value = dial_value % 100
            elif line[0] == "R":
                dial_value = dial_value + int(line[1:])
                dial_value = dial_value % 100
            else:
                print("should not happen")
            if dial_value == 0:
                zero_counter += 1
    print(zero_counter)
