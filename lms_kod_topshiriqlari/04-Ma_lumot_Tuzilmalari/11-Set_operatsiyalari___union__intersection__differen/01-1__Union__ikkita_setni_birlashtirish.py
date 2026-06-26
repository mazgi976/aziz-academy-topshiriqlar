a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a | b

print(*sorted(result))