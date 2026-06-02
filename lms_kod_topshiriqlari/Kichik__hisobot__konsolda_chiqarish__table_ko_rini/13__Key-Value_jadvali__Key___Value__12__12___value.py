n = int(input())

data = []

for _ in range(n):
    key, value = input().split()
    data.append((key, value))
    
print(f"{'Key':<12} | {'Value':>12}")
print("------------+------------")

for key, value in data:
    print(f"{key:<12} | {value:>11}")