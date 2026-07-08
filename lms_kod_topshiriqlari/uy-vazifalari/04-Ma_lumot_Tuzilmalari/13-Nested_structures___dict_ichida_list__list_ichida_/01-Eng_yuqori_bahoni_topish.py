n = int(input())

eng_baho = -1
eng_ism = ""

for _ in range(n):
    data = input().split()
    ism = data[0]
    baholar = list(map(int, data[1:]))
    
    for baho in baholar:
        if baho > eng_baho:
            eng_baho = baho 
            eng_ism = ism
            
print(eng_ism, eng_baho)