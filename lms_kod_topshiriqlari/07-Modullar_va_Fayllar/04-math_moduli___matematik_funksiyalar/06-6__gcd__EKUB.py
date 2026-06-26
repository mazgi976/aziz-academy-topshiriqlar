import math

def main():
    a, b = map(int, input().split())
    print(math.gcd(a, b))
    
if __name__ == '__main__':
    main()