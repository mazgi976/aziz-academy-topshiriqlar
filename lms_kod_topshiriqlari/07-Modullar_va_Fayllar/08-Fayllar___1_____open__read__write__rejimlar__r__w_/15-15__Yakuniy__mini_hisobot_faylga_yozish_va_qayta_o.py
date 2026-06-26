n = int(input())
malumotlar = [input() for _ in range(n)]

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def readlines(self):
        natija = []
        for qator in malumotlar:
            name, score = qator.split()
            natija.append(f"{name}:{score}\n")
        return natija
    
f = Fayl()
for qator in malumotlar:
    name, score = qator.split()
    f.write(f"{name}:{score}\n")
f.close()

f_qatorlar = f.readlines()
f.close()

ballar = []
for qator in f_qatorlar:
    if qator.strip():
        name, score = qator.strip().split(':')
        ballar.append(int(score))
        
jami_soni = len(ballar)
ortacha_ball = sum(ballar) / jami_soni
eng_yuqori = max(ballar)

print(jami_soni)
print(f"{ortacha_ball:.2f}")
print(eng_yuqori)