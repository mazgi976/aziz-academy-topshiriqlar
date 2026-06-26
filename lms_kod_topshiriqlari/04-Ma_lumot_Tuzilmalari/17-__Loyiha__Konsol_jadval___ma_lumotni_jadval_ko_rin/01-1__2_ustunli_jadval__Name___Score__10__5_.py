n = int(input())

print("Name       | Score")
print("----------+-----")

for _ in range(n):
    name, score = input().split()
    print(f"{name:<10} | {score:>5}")