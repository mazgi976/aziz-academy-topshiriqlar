sonlar = list(map(int, input().split()))
unikal_sonlar = set(sonlar)
saralangan_sonlar = sorted(unikal_sonlar, reverse=True)
print(*saralangan_sonlar[:3])