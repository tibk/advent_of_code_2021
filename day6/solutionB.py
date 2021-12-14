import argparse
from collections import defaultdict


def counter(l):
    # could use counter module :)
    c = defaultdict(int)  # 0 default
    for e in l:
        c[int(e)] = c[int(e)] + 1
    return c


def main(input_file, output_file, days):
    with open(input_file) as f:
        fishes = f.readline().strip().split(",")
    fishes = counter(fishes)

    for _ in range(days):
        fishes_copy = {k: fishes[k] for k in range(9)}
        fishes[8] = fishes_copy[0]
        fishes[7] = fishes_copy[8]
        fishes[6] = fishes_copy[0] + fishes_copy[7]
        fishes[5] = fishes_copy[6]
        fishes[4] = fishes_copy[5]
        fishes[3] = fishes_copy[4]
        fishes[2] = fishes_copy[3]
        fishes[1] = fishes_copy[2]
        fishes[0] = fishes_copy[1]
    result = sum(nf_fish for nf_fish in fishes.values())
    print(result)
    with open(output_file, "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputB.txt"
        days = 18
        print("Running test mode...")
    else:
        input_file = "input.txt"
        output_file = "outputB.txt"
        days = 256

    main(input_file, output_file, days)
