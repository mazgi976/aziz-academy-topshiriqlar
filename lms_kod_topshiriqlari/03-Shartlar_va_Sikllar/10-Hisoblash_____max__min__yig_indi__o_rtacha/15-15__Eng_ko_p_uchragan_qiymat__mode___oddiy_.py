n = int(input())
a = list(map(int, input().split()))

res = a[0]
max_count = 0

for x in a:
    count = 0
    for y in a:
        if x == y:
            count += 1
            
        if count > max_count:
            max_count = count = count
            res = x
        elif count == max_count:
            if x < res:
                res = x
                
print(res)
    
