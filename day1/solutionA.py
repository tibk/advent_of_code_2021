import argparse


def main(input_file, output_file):
    with open(input_file) as f:
        inputs = [int(d) for d in f.readlines()]
    increased_count = 0
    for index in range(1, len(inputs)):
        if inputs[index] >= inputs[index - 1]:
            increased_count += 1

    with open(output_file, "w") as f:
        f.write(str(increased_count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        print("Running test mode...")
        input_file = "test_input.txt"
        output_file = "test_output.txt"
    else:
        input_file = "input.txt"
        output_file = "output.txt"

    main(input_file, output_file)
