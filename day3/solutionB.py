import argparse


def to_int(binar):
    result = 0
    power = 1
    for digit in reversed(binar):
        if digit == "1":
            result += power
        power *= 2
    return result


def get_count(idx, rows):
    count = 0
    for row in rows:
        if row[idx] == "1":
            count += 1
        else:
            count -= 1
    return count


def get_filtered_rows(idx, rows, rev=False):
    count = get_count(idx, rows)
    if rev:
        count *= -1
    if count > 0 or (count == 0 and rev is False):
        return [r for r in rows if r[idx] == "1"]
    elif count < 0 or (count == 0 and rev is True):
        return [r for r in rows if r[idx] == "0"]


def main(input_file, output_file):
    with open(input_file) as f:
        inputs = [l.rstrip() for l in f.readlines()]
    idx = 0
    majo_rows = [l for l in inputs]
    mino_rows = [l for l in inputs]
    majo, mino = None, None
    while True:
        if len(majo_rows) == 1:
            [majo] = majo_rows
        if len(mino_rows) == 1:
            [mino] = mino_rows
        if majo is not None and mino is not None:
            break
        if majo is None:
            majo_rows = get_filtered_rows(idx, majo_rows, rev=False)
        if mino is None:
            mino_rows = get_filtered_rows(idx, mino_rows, rev=True)
        idx += 1

    oxy, co2 = to_int(majo), to_int(mino)
    print(f"oxy: {oxy}, co2: {co2}")
    result = oxy * co2
    print(f"result: {result}")
    with open(output_file, "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        input_file = "test_input.txt"
        output_file = "test_outputB.txt"
    else:
        input_file = "input.txt"
        output_file = "outputB.txt"

    main(input_file, output_file)
