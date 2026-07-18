nums = list(map(int, input().split()))
target = int(input())

seen = set()
found = False

for x in nums:
    if (target - x) in seen:
        found = True
        break
    seen.add(x)
    
if found:
    print("Ha")
else:
    print("Yoq")