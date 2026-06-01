n = int(input())
lst = list(map(int, input().split()))

musbat_sonlar = [x for x in lst if x > 0]

print(musbat_sonlar)