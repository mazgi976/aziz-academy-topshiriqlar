login = input().strip()
parol = input().strip()

natija = len(login) >= 3 and len(parol) >= 8 and login != parol
print(natija)