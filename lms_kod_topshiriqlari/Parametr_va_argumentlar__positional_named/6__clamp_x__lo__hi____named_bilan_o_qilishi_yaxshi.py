x, lo, hi = map(int, input().split())

def clamp(x, lo, hi):
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
    
res1 = clamp(x, lo, hi)
res2 = clamp(lo=lo, hi=hi, x=x)

print(res1)
print(res2)