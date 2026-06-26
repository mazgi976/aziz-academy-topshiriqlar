sonlar = list(map(int, input().split()))
unikal_sonlar = set(sonlar)
saralangan_sonlar = sorted(unikal_sonlar)
print(*saralangan_sonlar)