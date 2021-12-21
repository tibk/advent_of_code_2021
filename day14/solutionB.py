import argparse
import json
from collections import Counter

from tqdm import tqdm


def parse(input_file):
    with open(input_file) as f:
        poly = f.readline().strip()
        _ = f.readline()
        rules = [l.strip().split(" -> ") for l in f.readlines()]
        rules = {rule[0]: rule[0][0] + rule[1] + rule[0][1] for rule in rules}
    return poly, rules


def make_poly(poly, rules, steps_count):

    for _ in range(steps_count):
        n = len(poly)
        new_poly = str(poly)
        offset = 0
        for i in range(n - 1):
            segment = poly[i : i + 2]
            if segment in rules:
                sub_poly = rules[segment]
                new_poly = (
                    new_poly[: i + offset] + sub_poly + new_poly[i + offset + 2 :]
                )
                offset += len(sub_poly) - 2  # replaced poly[i:i+2] bysub_poly
        poly = new_poly
    return poly


def get_result(poly, rules_devider):
    rules_counts = {s: (v[-1], Counter(v)) for s, v in rules_devider.items()}
    n = len(poly)
    counter = Counter()
    for i in tqdm(range(n - 1)):
        segment = poly[i : i + 2]
        if segment in rules_counts.keys():
            if i == n - 2:
                last_char = poly[-1]
                counter[last_char] = counter[last_char] + 1
            last_char, counts = rules_counts[segment]
            counter.update(counts)
            counter[last_char] = counter[last_char] - 1
        else:
            counter.update(poly[i])
            if i == n - 2:
                counter.update(poly[-1])  # last one skipped
    print(counter)
    counts = sorted([v for v in counter.values()])
    return counts[-1] - counts[0]


def retrieve_or_compute_rules_devider(rules, devider):
    rules_devider = {}
    for s, v in rules.items():
        try:
            with open(f"./rules_devider_{mode}_{str(nb_steps)}/{s}") as f:
                v_devider = json.load(f)
                print(f"Retrieved {s} from previous try")
        except:
            print(f"Computing for {s}...")
            v_devider = make_poly(v, rules, devider - 1)
            with open(f"./rules_devider_{mode}_{str(nb_steps)}/{s}", "w") as f:
                json.dump(v_devider, f)
            print(f"Dumped {s} for next try")
        rules_devider[s] = v_devider
    return rules_devider


def main(input_file, output_file, nb_steps, mode):
    devider = nb_steps // 2
    poly, rules = parse(input_file)
    rules_devider = retrieve_or_compute_rules_devider(rules, devider)
    new_poly = make_poly(poly, rules_devider, 1)
    res = get_result(new_poly, rules_devider)  # last iteration just count
    print(res)
    with open(output_file, "w") as f:
        f.write(str(res))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("steps", type=int)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputB.txt"
        nb_steps = args.steps
        mode = "test"
        print("Running test mode...")
    else:
        input_file = "input.txt"
        output_file = "outputB.txt"
        nb_steps = args.steps
        mode = "full"
        print("Running full mode...")

    main(input_file, output_file, nb_steps, mode)
