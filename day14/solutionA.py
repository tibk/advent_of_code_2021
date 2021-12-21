import argparse
from collections import Counter


def parse(input_file):
    with open(input_file) as f:
        poly = f.readline().strip()
        _ = f.readline()
        rules = [l.strip().split(" -> ") for l in f.readlines()]
        rules = {rule[0]: rule[1] for rule in rules}
    return poly, rules


def make_poly(poly, rules, steps_count):
    for _ in range(steps_count):
        n = len(poly)
        insertions = []
        # find where to insert
        for i in range(n - 1):
            segment = poly[i : i + 2]
            if segment in rules:
                insertions.append((i, rules[segment]))
        insertions.sort(key=lambda x: x[0])
        # insert atoms
        offset = 0
        for pos, atom in insertions:
            true_pos = pos + offset
            poly = poly[0 : true_pos + 1] + atom + poly[true_pos + 1 :]
            offset += 1
    return poly


def get_result(poly):
    counter = Counter(poly)
    counts = sorted([v for v in counter.values()])
    print(counts)
    return counts[-1] - counts[0]


def main(input_file, output_file):
    poly, rules = parse(input_file)
    new_poly = make_poly(poly, rules, 10)
    res = get_result(new_poly)
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
