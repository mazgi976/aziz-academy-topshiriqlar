command = input()
try:
    a = int(input())
    b = int(input())
    
    if command == "ADD":
        print(a + b)
    elif command == "DIV":
        if b == 0:
            print("DIV0")
        else:
            print(a // b)
    else:
        print("BAD")
except ValueError:
    print("BAD")