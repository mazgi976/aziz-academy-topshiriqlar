text = input()
digits = set()

for char in text:
    if char.isdigit():
        digits.add(char)
        
if digits:
    print(*(sorted(digits)))
else:
    print("BO'SH")