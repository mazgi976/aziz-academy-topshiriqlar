n = int(input())

for i in range(1, n + 1):
    sum_row = 0
    for j in range(1, i + 1):
        sum_row += j
    print(sum_row)