import argparse

SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
MAPPING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def main(input_file, output_file):

    with open(input_file) as f:
        inputs = [l.strip() for l in f.readlines()]

    scores = []
    for line in inputs:

        corrupted = False
        stack = []
        line_score = 0

        for char in line:
            if char in ["(", "[", "{", "<"]:  # new chunck
                stack.append(char)
            else:  # end of chunck
                expected = MAPPING[stack.pop()]
                if expected != char:
                    corrupted = True
                    break  # corrupted line
        if corrupted:
            continue
        while stack:
            line_score = 5 * line_score + SCORES[stack.pop()]
        scores.append(line_score)

    score = sorted(scores)[int(len(scores) / 2)]
    print(score)
    with open(output_file, "w") as f:
        f.write(str(score))


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
