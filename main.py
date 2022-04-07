
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("score_L2.lvm", "r")

    data = [], []

    for line in file:
        line = line.replace(",",".")
        size = len(line)
        numbers = line[:size - 1]
        numbers = numbers.split("	")

        data[0].append(float(numbers[0]))
        data[1].append(float(numbers[1]))


