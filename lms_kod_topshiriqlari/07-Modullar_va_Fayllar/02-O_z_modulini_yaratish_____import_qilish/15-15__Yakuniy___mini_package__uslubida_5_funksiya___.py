def parse_ints(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def mean(nums: list[int]) -> float:
    return sum(nums) / len(nums)


def minmax(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)


def count_pos_neg(nums: list[int]) -> tuple[int, int]:
    pos_count = sum(1 for x in nums if x > 0)
    neg_count = sum(1 for x in nums if x < 0)
    return pos_count, neg_count


def report(nums: list[int]) -> str:
    n = len(nums)
    m = mean(nums)
    mn, mx = minmax(nums)
    p, g = count_pos_neg(nums)
    return f"count={n} mean={m:.2f} min={mn} max={mx} pos={p} neg={g}"


if __name__ == "__main__":
    line = input()
    nums = parse_ints(line)
    print(report(nums))