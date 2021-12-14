import argparse


def is_lowest(i, j, carto):
    size_x = len(carto)
    size_y = len(carto[0])
    neighbors_coords = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    neighbors_coords = [
        (n, m)
        for (n, m) in neighbors_coords
        if n >= 0 and m >= 0 and n < size_x and m < size_y
    ]
    for neighbor_coords in neighbors_coords:
        if int(carto[neighbor_coords[0]][neighbor_coords[1]]) <= int(carto[i][j]):
            return False
    return True


def main(input_file, output_file):
    with open(input_file) as f:
        carto = [l.strip() for l in f.readlines()]
    res = 0
    for i, row in enumerate(carto):
        for j, height in enumerate(row):
            if is_lowest(i, j, carto):
                res += int(height) + 1
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
