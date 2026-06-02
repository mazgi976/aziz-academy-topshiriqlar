def add(a, b):
       return a + b
    
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

ops = {'add': add, 'sub': sub, 'mul': mul}

def main():
    disp = ops
    q = int(input())
    
    for _ in range(q):
        op, a, b = input().split()
        a, b = int(a), int(b)
        print(disp[op](a, b))
        
if __name__ == '__main__':
    main()