import argparse


def try_flash(octo, i, j, step_flashed):
    if octo[i][j] <= 9 or (i, j) in step_flashed:
        return 0
    # flashes
    n = len(octo)
    step_flashed.add((i, j))
    for k in [i - 1, i, i + 1]:
        if k < 0 or k >= n:
            continue
        for l in [j - 1, j, j + 1]:
            if l < 0 or l >= n or (k == i and l == j):
                continue  # out or same
            octo[k][l] += 1
    return 1


def boost_octo(octo):
    n = len(octo)
    for i in range(n):
        for j in range(n):
            octo[i][j] += 1


def main(input_file, output_file):
    with open(input_file) as f:
        octo = [list(map(int, list(l.strip()))) for l in f.readlines()]

    flashes = 0
    n = len(octo)

    for step in range(1, 101):

        step_flashed = set()
        # increase all by 1
        boost_octo(octo)
        # check flashed > 9 and not flashed yet (while)
        cont = True
        while cont:  # iter
            iter_flashed = 0
            for i in range(n):
                for j in range(n):
                    iter_flashed += try_flash(octo, i, j, step_flashed)
            if iter_flashed == 0:
                cont = False  # no more flashes
        # update count
        flashes += len(step_flashed)
        # reset to 0
        for (i, j) in step_flashed:
            octo[i][j] = 0

    print(flashes)
    with open(output_file, "w") as f:
        f.write(str(flashes))


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
