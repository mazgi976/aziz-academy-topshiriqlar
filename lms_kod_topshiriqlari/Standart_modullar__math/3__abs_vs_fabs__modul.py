import math

def main():
    x = float(input())
    
    res_abs = abs(x)
    res_fabs = math.fabs(x)
    
    print(f"{res_abs:.2f}")
    print(f"{res_fabs:.2f}")
    
if __name__ == '__main__':
    main()