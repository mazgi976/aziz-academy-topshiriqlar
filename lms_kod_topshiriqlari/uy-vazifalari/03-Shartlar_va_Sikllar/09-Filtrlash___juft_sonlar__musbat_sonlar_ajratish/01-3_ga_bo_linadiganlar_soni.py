n = int(input())
sanagich = 0

for oi in range(n):
    son = int(input())
    if son % 3 == 0:
        sanagich += 1
         
print(sanagich)