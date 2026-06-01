n = int(input())
juftlar = [int(x) for x in input().split() if int(x) % 2 == 0]
print(min(juftlar) if juftlar else "No")