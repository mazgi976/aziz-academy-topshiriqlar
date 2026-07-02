email = input()
parol = input()

shart1 = "@" in email and "." in email
shart2 = 8 <= len(parol) <= 16
shart3 = email == email.lower()

print(shart1 and shart2 and shart3)