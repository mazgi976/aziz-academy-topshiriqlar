sonlar = sorted([int(x) for x in input().split()], reverse=True)
top_sonlar = sonlar[:3]
print(*(top_sonlar))