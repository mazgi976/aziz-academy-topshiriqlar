n = int(input())
oquvchilar = []

for _ in range(n):
    ism, mat, fiz = input().split()
    oquvchilar.append({"ism": ism, "mat": int(mat), "fiz": int(fiz)})
    
for oquvchi in oquvchilar:
    jami = oquvchi["mat"] + oquvchi["fiz"]
    print(f"{oquvchi['ism']} {jami}")