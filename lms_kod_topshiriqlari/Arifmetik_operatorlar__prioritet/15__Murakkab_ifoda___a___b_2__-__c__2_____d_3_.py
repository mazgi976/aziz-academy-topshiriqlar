a, b, c, d = map(int, input().split())
res = (a + b) - (c // 2) + (d % 3) + 2
print(f"Result: {res}")