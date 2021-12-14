import argparse

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
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
    score = 0
    for line in inputs:
        stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:  # new chunck
                stack.append(char)
            else:  # end of chunck
                expected = MAPPING[stack.pop()]
                if expected != char:
                    score += SCORES[char]
                    break  # next line
    print(score)
    with open(output_file, "w") as f:
        f.write(str(score))


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
