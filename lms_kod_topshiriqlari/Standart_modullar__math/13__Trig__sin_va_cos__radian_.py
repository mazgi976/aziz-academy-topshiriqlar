import math

def main():
    x = float(input())
    
    s = math.sin(x)
    c = math.cos(x)
    
    if abs(s) < 1e-9:
        s = 0.0 
    if abs(c) < 1e-9:
        c = 0.0
    print(f"{s:.4f}")
    print(f"{c:.4f}")
    
if __name__ == '__main__':
    main()