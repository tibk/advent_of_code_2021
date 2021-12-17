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


def main(input_file, output_file):
    dots, folds = parse(input_file)
    axis, value = folds[0]  # first instructin only
    print(dots, axis, folds)
    new_dots = set()
    for dot in dots:
        new_dot = list(dot)
        if dot[axis] > value:
            new_dot[axis] = 2 * value - dot[axis]
        new_dots.add(tuple(new_dot))
    res = len(new_dots)
    print(res)
    with open(output_file, "w") as f:
        f.write(str(res))


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
