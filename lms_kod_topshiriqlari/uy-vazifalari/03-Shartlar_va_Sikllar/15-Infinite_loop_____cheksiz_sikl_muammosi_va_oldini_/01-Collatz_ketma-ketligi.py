n = int(input())
qadamlar = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    qadamlar += 1
    
print(qadamlar)