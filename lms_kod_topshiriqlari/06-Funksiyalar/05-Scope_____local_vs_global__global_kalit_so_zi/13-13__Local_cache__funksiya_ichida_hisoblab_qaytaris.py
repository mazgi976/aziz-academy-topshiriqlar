def squares(n):
    local_list = [i ** 2 for i in range(1, n + 1)]
    return local_list

n = int(input())
result = squares(n)

print(*(result))