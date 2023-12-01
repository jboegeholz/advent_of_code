def test_sliding_window():

    data = []
    with open("./aoc_day_01_test_data.txt") as f:
        for line in f:
            data.append(int(line.rstrip()))

    triplet_sums = []

    for i, v in enumerate(data):
        if i < (len(data) - 2):
            triplet_sum = data[i] + data[i+1] + data[i+2]
            triplet_sums.append(triplet_sum)
    print(triplet_sums)

    sums_larger_than_previous_sums = 0
    for i, v in enumerate(triplet_sums):
        if i < (len(triplet_sums) - 1):
            if triplet_sums[i] < triplet_sums[i+1]:
                sums_larger_than_previous_sums += 1

    print(sums_larger_than_previous_sums)

