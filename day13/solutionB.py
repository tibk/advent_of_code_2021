import argparse


def parse(input_file):
    dots = set()
    folds = []
    first_half = True
    with open(input_file) as f:
        for line in f.readlines():
            if line == "\n":
                first_half = False
                continue
            if first_half:
                x, y = line.strip().split(",")
                dots.add((int(x), int(y)))
            else:
                axis, value = line.strip().split("fold along ")[1].split("=")
                axis = 0 if axis == "x" else 1
                folds.append((axis, int(value)))
    return dots, folds


def make_folds(dots, folds):
    for (axis, value) in folds:
        new_dots = set()
        for dot in dots:
            new_dot = list(dot)
            if dot[axis] > value:
                new_dot[axis] = 2 * value - dot[axis]
            new_dots.add(tuple(new_dot))
        dots = new_dots
    return dots


def print_msg(dots):
    max_x = max([x for x, _ in dots])
    max_y = max([y for y, _ in dots])
    for y in range(max_y + 1):
        row = ["#" if (x, y) in dots else "." for x in range(max_x + 1)]
        print(" ".join(row))


def main(input_file, output_file):
    dots, folds = parse(input_file)
    print(folds)
    dots = make_folds(dots, folds)
    print("Res:")
    print_msg(dots)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputA.txt"
        print("Running test mode...")
    else:
        input_file = "input.txt"
        output_file = "outputA.txt"
        print("Running full mode...")

    main(input_file, output_file)
