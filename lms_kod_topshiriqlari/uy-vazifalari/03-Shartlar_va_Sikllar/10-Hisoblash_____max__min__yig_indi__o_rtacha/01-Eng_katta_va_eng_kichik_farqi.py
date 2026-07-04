n = int(input())
birinchi_son = int(input())

eng_katta = birinchi_son
eng_kichik = birinchi_son

for i in range(n - 1):
    son = int(input())
    if son > eng_katta:
        eng_katta = son
    if son < eng_kichik:
        eng_kichik = son
        
print(eng_katta - eng_kichik)