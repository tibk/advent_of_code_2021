import argparse
from collections import defaultdict


def get_links(input_file):
    with open(input_file) as f:
        inputs = f.readlines()
    links = defaultdict(list)
    for line in inputs:
        origin, dest = line.strip().split("-")
        links[origin] = links[origin] + [dest]
        links[dest] = links[dest] + [origin]
    return links


def get_paths(current, links, visited={}, joker=True, exited=True):
    visited = set(visited)  # make a copy
    if current.islower() and current not in ["start", "end"]:
        if current in visited:
            if joker:
                joker = False
            else:
                return []
        visited.add(current)
    if current == "end":
        return [["end"]]
    if current == "start" and exited:
        return []

    paths = []
    for dest in links[current]:
        for from_dest in get_paths(dest, links, visited=visited, joker=joker):
            paths.append([current] + from_dest)
    return paths


def main(input_file, output_file):
    links = get_links(input_file)
    paths = get_paths("start", links, {}, exited=False)
    res = len(paths)
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
