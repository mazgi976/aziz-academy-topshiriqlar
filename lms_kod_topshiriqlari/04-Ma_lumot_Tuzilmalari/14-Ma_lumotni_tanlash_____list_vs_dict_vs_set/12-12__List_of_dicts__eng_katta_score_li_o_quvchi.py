n = int(input())
oquvchilar = []

for _ in range(n):
    data = input().split()
    name = data[0]
    score = int(data[1])
    oquvchilar.append({'name': name, 'score': score})
    
eng_yaxshi = max(oquvchilar, key=lambda x: (x['score'], [-ord(c) for c in x['name']]))

print(f"{eng_yaxshi['name']} {eng_yaxshi['score']}")