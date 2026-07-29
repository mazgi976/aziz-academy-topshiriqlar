n = int(input())
print(len({input().strip() for _ in range(n)}))