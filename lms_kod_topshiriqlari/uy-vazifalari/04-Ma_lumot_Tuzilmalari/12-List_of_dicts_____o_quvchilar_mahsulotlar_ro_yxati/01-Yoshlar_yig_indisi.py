n = int(input())
oquvchilar = []
yigindi = 0

for _ in range(n):
    ism, yosh = input().split()
    yosh = int(yosh)
    oquvchilar.append({"ism": ism, "yosh": yosh})
    yigindi += yosh
    
print(yigindi)