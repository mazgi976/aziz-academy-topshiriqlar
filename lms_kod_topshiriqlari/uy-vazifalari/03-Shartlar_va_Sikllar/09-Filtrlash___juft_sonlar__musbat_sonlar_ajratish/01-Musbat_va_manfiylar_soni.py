n = int(input())
musbatlar = 0 
manfiylar = 0 

for i in range(n):
    son = int(input())
    if son > 0:
        musbatlar += 1
    elif son < 0:
        manfiylar += 1 
        
print(musbatlar, manfiylar)

    