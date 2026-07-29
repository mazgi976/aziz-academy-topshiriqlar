n = int(input())
d = {f"k{i}": int(input()) for i in range(n)}
print(sum(d.values()))