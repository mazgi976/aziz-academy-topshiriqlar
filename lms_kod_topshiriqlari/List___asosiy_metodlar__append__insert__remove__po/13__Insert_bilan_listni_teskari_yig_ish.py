n = int(input())
elements = list(map(int, input().split()))

lst = []
for x in elements:
    lst.insert(0, x)
    
print(lst)