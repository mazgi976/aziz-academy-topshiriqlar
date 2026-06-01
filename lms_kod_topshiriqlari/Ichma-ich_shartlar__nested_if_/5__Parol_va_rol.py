password = input()

if password == "1234":
    print("Admin")
else:
    if password == "0000":
        print("Denied")      
    else:
        print("User")

