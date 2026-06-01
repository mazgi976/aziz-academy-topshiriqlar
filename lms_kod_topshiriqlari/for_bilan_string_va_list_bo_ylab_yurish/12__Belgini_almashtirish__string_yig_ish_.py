s = input()
result = ""

for char in s:
    if char == 'a':
        result += "@"
    else:        
        result += char
    
print(result)        
        