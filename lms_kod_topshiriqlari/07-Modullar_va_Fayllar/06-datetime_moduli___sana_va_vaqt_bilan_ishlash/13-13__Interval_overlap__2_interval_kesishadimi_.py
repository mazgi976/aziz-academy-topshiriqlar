from datetime import date

a1_str, a2_str = input().split()
b1_str, b2_str = input().split()

a1 = date.fromisoformat(a1_str)
a2 = date.fromisoformat(a2_str)
b1 = date.fromisoformat(b1_str)
b2 = date.fromisoformat(b2_str)

start = max(a1, b1)
end = min(a2, b2)

if start <= end:
    print("YES")
else:
    print("NO")