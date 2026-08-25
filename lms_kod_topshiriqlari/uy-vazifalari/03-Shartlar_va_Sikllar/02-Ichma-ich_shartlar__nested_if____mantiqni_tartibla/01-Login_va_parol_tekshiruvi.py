login = input().strip()
password = input().strip()

if login == "admin":
    if password == "1234":
        print("Xush kelibsiz")
    else:
        print("Parol xato")
else:
    print("Login topilmadi")