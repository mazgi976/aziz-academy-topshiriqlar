sonlar = [int(x) for x in input().split()]
evens = [x for x in sonlar if x % 2 == 0]
print(len(evens))
print(len(sonlar) - len(evens))