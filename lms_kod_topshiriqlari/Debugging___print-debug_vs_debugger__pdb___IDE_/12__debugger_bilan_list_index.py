n = int(input())
elements = []

for _ in range(n):
    elements.append(input())
    
idx = int(input())

if 0 <= idx < n:
    print(elements[idx])
else:
    print("OUT")