import math

def main():
    a, b = map(int, input().split())
    
    if a == 0 or b == 0:
        lcm = 0
    else:
        lcm = abs(a * b) // math.gcd(a, b)
        
    print(lcm)
    
if __name__ == '__main__':
    main()