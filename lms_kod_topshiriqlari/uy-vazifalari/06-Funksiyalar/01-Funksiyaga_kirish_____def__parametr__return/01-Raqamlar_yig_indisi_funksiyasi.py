def raqamlar_yigindisi(n):
    yindi = 0
    while n > 0:
        yindi += n % 10
        n //= 10
    return yindi

if __name__ == "__main__":
    n = int(input())
    print(raqamlar_yigindisi(n))