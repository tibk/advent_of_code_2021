import argparse


def main(input_file, output_file):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "input_test.txt"
        output_file = "output_test.txt"
    else:
        input_file = "input.txt"
        output_file = "output.txt"

    main(input_file, output_file)
