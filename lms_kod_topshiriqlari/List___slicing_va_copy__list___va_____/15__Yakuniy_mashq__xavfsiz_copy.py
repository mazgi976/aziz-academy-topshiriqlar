n = int(input())
lst = list(map(int, input().split()))

lst_copy = list(lst)
lst_copy.reverse()

print(lst)
print(lst_copy)