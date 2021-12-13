import argparse


def parse_input(input_file):
    with open(input_file) as f:
        lines = [
            [tuple(map(int, e.split(","))) for e in l.strip().split(" -> ")]
            for l in f.readlines()
        ]
    return lines


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    return 0


def get_windy_points(wind):
    # [['0', '9'], ['5', '9']]
    windy_points = []
    dx, dy = wind[1][0] - wind[0][0], wind[1][1] - wind[0][1]
    if dx == 0:  # horizontal
        i = wind[0][0]
        windy_points = [
            (i, j) for j in range(wind[0][1], wind[1][1] + sign(dy), sign(dy))
        ]
    elif dy == 0:  # vertical
        j = wind[0][1]
        windy_points = [
            (i, j) for i in range(wind[0][0], wind[1][0] + sign(dx), sign(dx))
        ]
    else:  # diagonal by hypothesis
        i = wind[0][0]
        j = wind[0][1]
        windy_points = [
            (i + k * sign(dx), j + k * sign(dy)) for k in range(abs(dx) + 1)
        ]
    return windy_points


def main(input_file, output_file):
    winds = parse_input(input_file)
    danger1 = set()
    danger2 = set()
    for wind in winds:
        windy_points = get_windy_points(wind)
        for windy_point in windy_points:
            if windy_point not in danger2 and windy_point in danger1:
                danger2.add(windy_point)
            elif windy_point not in danger1:
                danger1.add(windy_point)
    result = len(danger2)
    print(result)
    with open(output_file, "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputB.txt"
    else:
        input_file = "input.txt"
        output_file = "outputB.txt"

    main(input_file, output_file)
