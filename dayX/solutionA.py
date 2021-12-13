import argparse


def main(input_file, output_file):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputA.txt"
    else:
        input_file = "input.txt"
        output_file = "outputA.txt"

    main(input_file, output_file)
