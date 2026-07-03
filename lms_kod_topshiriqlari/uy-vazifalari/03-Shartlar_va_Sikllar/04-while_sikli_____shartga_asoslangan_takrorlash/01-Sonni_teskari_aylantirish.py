n = int(input())
teskari_son = 0

while n > 0:
    raqam = n % 10
    teskari_son = teskari_son * 10 + raqam
    n = n // 10
    
print(teskari_son)