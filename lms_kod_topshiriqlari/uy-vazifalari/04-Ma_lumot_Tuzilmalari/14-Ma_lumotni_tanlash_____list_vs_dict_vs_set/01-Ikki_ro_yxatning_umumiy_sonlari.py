a = set(map(int, input().split()))
b = set(map(int, input().split()))

natija = sorted(a & b)

print(*natija)