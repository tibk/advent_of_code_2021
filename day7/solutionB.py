import argparse


def main(input_file, output_file):
    with open(input_file) as f:
        inputs = list(map(int, f.readline().strip().split(",")))
    best_fuel = None
    for center in range(min(inputs), max(inputs) + 1):
        fuel = sum([(abs(i - center) * (abs(i - center) + 1)) / 2 for i in inputs])
        if best_fuel is None or fuel < best_fuel:
            best_fuel = fuel
    print(best_fuel)
    with open(output_file, "w") as f:
        f.write(str(best_fuel))


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

    main(input_file, output_file)
