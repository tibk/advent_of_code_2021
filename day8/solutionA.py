import argparse


def main(input_file, output_file):
    with open(input_file) as f:
        inputs = [l.strip().split(" | ")[1] for l in f.readlines()]

    count = 0
    for line in inputs:
        for digit in line.split(" "):
            if len(digit) in [2, 4, 3, 7]:  # (1,4,7,8 digits)
                count += 1
    print(count)
    with open(output_file, "w") as f:
        f.write(str(count))


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
