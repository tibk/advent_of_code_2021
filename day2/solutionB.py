import argparse


def main(input_file, output_file):
    with open(input_file) as f:
        inputs = f.readlines()
    current_pos = [0, 0]  # (horizontal, depth)
    aim = 0
    for cmd in inputs:
        direction, amount = cmd.split(" ")
        amount = int(amount)
        if direction == "forward":
            current_pos[0] += amount
            current_pos[1] += aim * amount
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount
    print(current_pos)

    result = current_pos[0] * current_pos[1]
    with open(output_file, "w") as f:
        f.write(str(result))
    print(result)


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
