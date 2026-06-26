data = input().split()
role = data[0]
active = int(data[1])

if role == "admin":
    if active == 1:
        print("Admin active")
    else:
        print("Admin inactive")
else:
        print("User")