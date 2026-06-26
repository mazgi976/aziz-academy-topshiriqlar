n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(int(input()))
else:
    sonlar = []
    for _ in range(n):
        sonlar.append(int(input()))
    print(max(sonlar) - min(sonlar))