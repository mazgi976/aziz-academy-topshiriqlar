n = int(input())
lst = list(map(int, input().split()))

toq_sonlar = [x for x in lst if x % 2 != 0]

print(toq_sonlar)