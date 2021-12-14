import argparse


def get_neighbors(i, j, carto):
    size_x = len(carto)
    size_y = len(carto[0])
    neighbors_coords = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    neighbors_coords = [
        (n, m)
        for (n, m) in neighbors_coords
        if n >= 0 and m >= 0 and n < size_x and m < size_y
    ]
    return neighbors_coords


def follow_flow(i, j, carto, path, basin):
    # finds dir of flow, adding it to path until low point is found
    # when low point is found basin is updated

    if carto[i][j] == "9":
        return  # ignore those
    path.append((i, j))

    if (i, j) in basin:
        for point in path:
            basin[tuple(point)] = basin[(i, j)]
            return

    neighbors_coords = get_neighbors(i, j, carto)
    lowest = None
    lowest_coords = None
    for neighbor_coords in neighbors_coords:
        neighbor_height = int(carto[neighbor_coords[0]][neighbor_coords[1]])
        if lowest is None or neighbor_height <= lowest:
            lowest = neighbor_height
            lowest_coords = neighbor_coords
    if lowest >= int(carto[i][j]):  # lowest point is current
        # path.append([i, j])
        for point in path:
            basin[tuple(point)] = (i, j)
            return
    # path.append(lowest_coords)
    follow_flow(lowest_coords[0], lowest_coords[1], carto, path, basin)


def main(input_file, output_file):
    with open(input_file) as f:
        carto = [l.strip() for l in f.readlines()]
    res = 0
    basin = {}
    for i, row in enumerate(carto):
        for j, height in enumerate(row):
            follow_flow(i, j, carto, [], basin)

    rev_basin = {}
    for k, v in basin.items():
        rev_basin[v] = rev_basin.get(v, []) + [k]
    basin_sizes = [len(v) for v in rev_basin.values()]
    basin_sizes = sorted(basin_sizes, reverse=True)[:3]
    res = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(res)
    with open(output_file, "w") as f:
        f.write(str(res))


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
