def part1(data):
    result = {"increased": 0, "decreased": 0}

    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            result["increased"] += 1
        elif data[i] < data[i-1]:
            result["decreased"] += 1

    return result


def part2(data):
    result = {"increased": 0, "decreased": 0}

    for i in range(0, len(data)-3):
        window_1 = sum(data[i: i+3])
        window_2 = sum(data[i+1: i+4])

        if window_2 > window_1:
            result["increased"] += 1
        elif window_2 < window_1:
            result["decreased"] += 1

    return result


def main():
    data = [int(_.strip("\n")) for _ in open("../resources/Day01.txt").readlines()]
    print("part 1: ", part1(data))
    print("part 2: ", part2(data))


if __name__ == "__main__":
    main()
