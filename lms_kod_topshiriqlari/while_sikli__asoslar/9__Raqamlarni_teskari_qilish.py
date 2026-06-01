n = int(input())
teskari_son = 0

while n > 0:
    teskari_son = teskari_son * 10 + n % 10
    n //= 10
    
print(teskari_son)    