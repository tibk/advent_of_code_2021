import argparse


def tick(grids, number):
    for grid in grids:
        for i in range(5):
            for j in range(5):
                if grid[i][j] == number:
                    grid[i][j] = -1
                    if (
                        grid[i] == [-1] * 5
                        or [grid[k][j] for k in range(5)] == [-1] * 5
                    ):
                        return grid


def get_result(grid, number):
    result = 0
    for i in range(5):
        for j in range(5):
            if grid[i][j] != -1:
                result += int(grid[i][j])
    result *= int(number)
    return result


def parse_input(input_file):
    with open(input_file) as f:
        inputs = f.readline().rstrip().split(",")
        grid_data = [l.strip() for l in f.readlines() if l.strip()]
        n = len(grid_data) // 5
        grids = [
            [
                grid_data[5 * idx].split(),
                grid_data[5 * idx + 1].split(),
                grid_data[5 * idx + 2].split(),
                grid_data[5 * idx + 3].split(),
                grid_data[5 * idx + 4].split(),
            ]
            for idx in range(n)
        ]
    return inputs, grids


def main(input_file, output_file):

    inputs, grids = parse_input(input_file)
    for number in inputs:
        completed_grid = tick(grids, number)
        if completed_grid is not None:
            result = get_result(completed_grid, number)
            break
    print(result)
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
