d=input().split()
s=sorted(set(map(int,d)))
print("{"+", ".join(map(str,s))+"}")