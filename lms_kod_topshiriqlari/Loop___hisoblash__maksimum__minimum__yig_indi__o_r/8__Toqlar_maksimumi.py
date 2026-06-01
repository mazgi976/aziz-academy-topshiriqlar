n = int(input())
toqlar = [int(x) for x in input().split() if int(x) % 2 != 0]
print(max(toqlar) if toqlar else "No")