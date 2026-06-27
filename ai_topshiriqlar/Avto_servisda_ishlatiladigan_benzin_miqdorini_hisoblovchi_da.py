# Avto servisda ishlatiladigan benzin miqdorini hisoblovchi dastur
# Kurs: Dasturlash / IT
# Mavzu: Type casting ⭐ — type(), int(), float(), str(), bool()
# Ball: 100
# Aziz Academy — AI Topshiriq

data = input().split()
h = int(data[0])
i = int(data[1])
t = int(data[2])

res = (i * t) / h * 100

if res == int(res):
    print(int(res))
else:
    print(res)