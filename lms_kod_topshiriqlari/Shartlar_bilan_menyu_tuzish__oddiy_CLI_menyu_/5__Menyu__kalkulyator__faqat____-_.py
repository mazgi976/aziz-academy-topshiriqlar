data = input().split()
a = int(data[0])
b = int(data[1])
op = data[2]

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
else:
    print("Invalid")



