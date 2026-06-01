n = int(input())
lst = list(map(int, input().split()))

juft_sonlar = [x for x in lst if x % 2 == 0]
print(juft_sonlar)          