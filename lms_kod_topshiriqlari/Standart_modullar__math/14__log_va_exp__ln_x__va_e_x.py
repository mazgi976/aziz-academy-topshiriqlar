import math

def main():
    x = float(input())
    y = float(input())
    
    ln = math.log(x)
    ex = math.exp(y)
    
    print(f"{ln:.4f}")
    print(f"{ex:.4f}")
    
if __name__ == '__main__':
    main()