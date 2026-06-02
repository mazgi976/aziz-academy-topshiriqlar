def parse_ints(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def print_line(items: list) -> str:
    return " ".join(map(str, items))


if __name__ == "__main__":
    line = input()
    nums = parse_ints(line)
    doubled_nums = [x * 2 for x in nums]
    print(print_line(doubled_nums))