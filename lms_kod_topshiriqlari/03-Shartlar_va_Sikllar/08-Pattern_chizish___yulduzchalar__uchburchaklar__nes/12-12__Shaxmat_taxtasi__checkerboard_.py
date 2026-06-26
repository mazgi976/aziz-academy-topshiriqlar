n, m = map(int, input().split())

for i in range(n):
    line = ""
    for j in range(m):
        if (i + j) % 2 == 0:
            line += "*"
        else:
            line += "."
    print(line)