n = int(input())
data = {}

for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
    
X = int(input())
result = {k: v for k, v in data.items() if v >= X} 
print(result)
    