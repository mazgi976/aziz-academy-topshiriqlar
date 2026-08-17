def yigindi(*sonlar):
    return sum(sonlar)

# Foydalanuvchidan ma'lumotni o'qish va ro'yxatga aylantirish
qator = input()
if qator.strip():
    sonlar_royxati = list(map(int, qator.split()))
    natija = yigindi(*sonlar_royxati)
    print(natija)