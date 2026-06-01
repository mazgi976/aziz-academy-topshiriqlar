n = int(input())
a = list(map(int, input().split()))
avg = sum(a) / n
print(len([x for x in a if x > avg]))