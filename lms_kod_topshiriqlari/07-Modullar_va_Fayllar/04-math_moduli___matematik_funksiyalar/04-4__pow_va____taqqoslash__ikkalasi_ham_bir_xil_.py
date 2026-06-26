import math

def main():
    a, b = map(int, input().split())
    
    p1 = math.pow(a, b)
    p2 = a ** b
    print(f"{p1:.0f}")
    print(p2)
    
if __name__ == '__main__':
    main()