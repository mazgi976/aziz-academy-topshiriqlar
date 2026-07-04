r = int(input())
jami_urinishlar = 0
min_urinish = float('inf')

for i in range(1, r + 1):
    yashirin_son = int(input())
    urinish = 0
    while True:
        taxmin = int(input())
        urinish += 1
        if taxmin == yashirin_son:
            break
            
    print(f"Round {i}: {urinish} urinish")
    jami_urinishlar += urinish
    if urinish < min_urinish:
        min_urinish = urinish
        
print(f"Jami: {jami_urinishlar}")
print(f"Eng yaxshi: {min_urinish}")