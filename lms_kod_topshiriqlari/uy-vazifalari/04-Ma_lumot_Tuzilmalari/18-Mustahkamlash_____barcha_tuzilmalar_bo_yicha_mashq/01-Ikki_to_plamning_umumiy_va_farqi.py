# Ikkita qatorni o'qib, to'plamlarga o'tkazamiz
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Kesishma (ikkalasida ham bor) va ayirma (birinchisida bor, ikkinchisida yo'q)
kesishma = sorted(list(set1 & set2))
ayirma = sorted(list(set1 - set2))

# Natijalarni chiqarish
print(*kesishma)
print(*ayirma)