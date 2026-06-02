def parse_ints(line):
    return [int(x) for x in line.split()]

def unique(nums):
    return list(set(nums))

def sort_nums(nums):
    return sorted(nums)

line = input()
nums = parse_ints(line)
uniq_nums = unique(nums)
sorted_nums = sort_nums(uniq_nums)

print(*(sorted_nums))