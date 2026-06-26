def inc(x):
    return x + 1

def dec(x):
    return x - 1

ops = {'inc': inc, 'dec': dec}

def main():
    x = int(input())
    cmd = input().strip()
    
    res_a = ops[cmd](x)
    
    fn = ops[cmd]
    res_b = fn(x)
    
    print(res_a)
    print(res_b)
    
if __name__ == '__main__':
    main()