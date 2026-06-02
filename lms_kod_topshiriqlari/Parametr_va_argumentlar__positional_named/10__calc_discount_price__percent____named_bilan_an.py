price, percent = map(int, input().split())

def calc_discount(price, percent):
    return price - price * percent / 100

res1 = calc_discount(price, percent)
res2 = calc_discount(percent=percent, price=price)

print(f"{res1:.2f}")
print(f"{res2:.2f}")