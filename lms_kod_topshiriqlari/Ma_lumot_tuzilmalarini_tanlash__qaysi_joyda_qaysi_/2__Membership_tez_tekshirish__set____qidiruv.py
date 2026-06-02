n = int(input())
sonlar = set(map(int, input().split()))
q = int(input())

for _ in range(q):
    query = int(input())
    if query in sonlar:
        print("YES")
    else:
        print("NO")