a, b = map(int, input().split())
mode = input()

def choose(a, b, mode):
    if mode == 'max':
        return max(a, b)
    elif mode == 'min':
        return min(a, b)
    else:
        return a
    
res1 = choose(a, b, mode)
res2 = choose(mode=mode, a=a, b=b)

print(res1)
print(res2)