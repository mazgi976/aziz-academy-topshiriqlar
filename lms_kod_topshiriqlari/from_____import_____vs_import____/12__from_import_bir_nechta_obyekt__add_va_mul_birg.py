def add(a, b):
    return a + b

def mul(a, b):
    return a * b

ops = {'add': add, 'mul': mul}

def main():
    a, b = map(int, input().split())
    mode = input().strip()
    
    add_fn = ops['add']
    mul_fn = ops['mul']
    
    if mode == 'add':
        print(add_fn(a, b))
    elif mode == 'mul':
        print(mul_fn(a, b))
        
if __name__ == '__main__':
    main()