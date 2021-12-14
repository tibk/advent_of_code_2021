import argparse
import itertools


digit_mapping = {
    0: {"a", "c", "f", "g", "e", "b"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"c", "b", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}


def map_digit(segment_mapping, digit):
    mapped_digit = {segment_mapping[s] for s in digit}
    return mapped_digit


def validate_mapping(segment_mapping, digits):
    for digit in digits:
        mapped_digit = map_digit(segment_mapping, digit)
        if mapped_digit not in digit_mapping.values():
            return False
    return True


def get_mapping(digits):
    segments = ["a", "b", "c", "d", "e", "f", "g"]
    for perm in itertools.permutations(segments):
        segment_mapping = {perm[i]: segments[i] for i in range(7)}
        if validate_mapping(segment_mapping, digits):
            return segment_mapping
    raise (f"No mapping found for digits: {digits}")


def decode(segment_mapping, code):
    decoded = ""
    for digit in code:
        mapped_digit = map_digit(segment_mapping, digit)
        for k, v in digit_mapping.items():
            if v == mapped_digit:
                decoded += str(k)
    return int(decoded)


def main(input_file, output_file):
    with open(input_file) as f:
        inputs = [l.strip().split(" | ") for l in f.readlines()]

    count = 0
    for (digits, code) in inputs:
        digits = digits.split()
        code = code.split()
        segment_mapping = get_mapping(digits)
        count += decode(segment_mapping, code)

    print(count)
    with open(output_file, "w") as f:
        f.write(str(count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputB.txt"
        print("Running test mode...")
    else:
        input_file = "input.txt"
        output_file = "outputB.txt"
        print("Running full mode...")

    main(input_file, output_file)
