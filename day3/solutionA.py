import argparse


def to_int(counter):
    gamma, epsilon = 0, 0
    n = len(counter)
    power = 1
    for count in reversed(counter):
        if count > 0:
            gamma += power
        elif count < 0:
            epsilon += power
        else:
            raise ("No majority")
        power *= 2
    return gamma, epsilon


def main(input_file, output_file):
    counter = None
    with open(input_file) as f:
        inputs = f.readlines()
    for input_row in inputs:
        input_row = input_row.rstrip()
        if counter is None:
            counter = [0 for _ in range(len(input_row))]
        for idx, digit in enumerate(input_row):
            if digit == "1":
                counter[idx] += 1
            else:
                counter[idx] -= 1
    print(counter)
    gamma, epsilon = to_int(counter)
    print(gamma, epsilon)
    result = gamma * epsilon
    print(f"result: {result}")
    with open(output_file, "w") as f:
        f.write(str(result))


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
