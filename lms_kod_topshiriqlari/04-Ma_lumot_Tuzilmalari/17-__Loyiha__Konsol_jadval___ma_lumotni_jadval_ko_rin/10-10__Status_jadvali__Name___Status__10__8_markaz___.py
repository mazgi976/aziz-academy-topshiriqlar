n = int(input())
for _ in range(n):
    line = input().split()
    name = line[0]
    flag = int(line[1])
    status = 'present' if flag == 1 else 'absent'
    print(f"{name}|{status}")