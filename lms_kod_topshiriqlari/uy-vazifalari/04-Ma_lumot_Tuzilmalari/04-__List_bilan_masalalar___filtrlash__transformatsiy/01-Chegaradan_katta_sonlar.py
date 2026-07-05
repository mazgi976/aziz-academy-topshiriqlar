numbers = list(map(int, input().split()))
t = int(input())
result = [num for num in numbers if num > t]
print(*result)