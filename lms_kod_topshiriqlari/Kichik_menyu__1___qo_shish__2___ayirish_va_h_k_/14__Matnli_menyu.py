a, b = map(int, input().split())
amal = input().strip()
    
if amal == "add":
    print(a + b)        
elif amal == "sub":
    print(a - b)
elif amal == "mul":
    print(a * b)
elif amal == "div":
    if b != 0:
        print(a // b)
    else:
        print("0 ga bo'lish mumkin emas")
else:
    print("Noto'g'ri amal")

            
            
              