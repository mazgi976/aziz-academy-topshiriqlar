import math

def main():
    a, b = map(float, input().split())
    c = math.sqrt(a * a + b * b)
    print(f"{c:.2f}")
    
if __name__ == '__main__':
    main()