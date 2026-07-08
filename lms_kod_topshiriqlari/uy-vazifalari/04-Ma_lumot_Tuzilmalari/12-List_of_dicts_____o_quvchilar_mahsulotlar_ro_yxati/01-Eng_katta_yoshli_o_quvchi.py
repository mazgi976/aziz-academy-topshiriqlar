n = int(input())
oquvchilar = []

for _ in range(n):
    ism, yosh = input().split()
    oquvchilar.append({"ism": ism, "yosh": int(yosh)})
    
eng_yoshi_katta = max(oquvchilar, key=lambda x: x["yosh"])

print(eng_yoshi_katta["ism"])