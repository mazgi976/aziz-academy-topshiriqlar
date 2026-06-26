def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b 
    return abs(a)
        
        
def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
    print(lcm(a, b))