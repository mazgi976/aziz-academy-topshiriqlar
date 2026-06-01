data = input().split()
username = data[0]
age = int(data[1])

if username == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limited")
else:
     print("No access")

