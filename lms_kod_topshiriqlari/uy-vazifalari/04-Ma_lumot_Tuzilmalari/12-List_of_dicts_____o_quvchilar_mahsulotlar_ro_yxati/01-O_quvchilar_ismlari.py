n = int(input())
oquvchilar = []

for _ in range(n):
    ism, yosh = input().split()
    oquvchilar.append({"ism": ism, "yosh": int(yosh)})
    
for oquvchi in oquvchilar:
    print(oquvchi["ism"])