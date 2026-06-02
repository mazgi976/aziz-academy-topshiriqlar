def unique(nums: list[int]) -> list[int]:
    return list(set(nums))


def sorted_unique(nums: list[int]) -> list[int]:
    return sorted(unique(nums))


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = sorted_unique(nums)
    print(" ".join(map(str, result)))