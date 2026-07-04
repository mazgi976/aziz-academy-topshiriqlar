n = int(input())
yigindi = 0

for i in range(1, n):
    if n % i == 0:
        yigindi += i
if yigindi == n:
    print("MUKAMMAL")
else:
    print("MUKAMMAL EMAS")