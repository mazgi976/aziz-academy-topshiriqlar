n = int(input())
malumotlar = [input() for _ in range(n)]

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def read(self):
        natija = ""
        for qator in malumotlar:
            name, score = qator.split()
            natija += f"{name},{score}\n"
        return natija    
                       
f = Fayl()
for qator in malumotlar:
    name, score = qator.split()
    f.write(f"{name},{score}\n")
f.close()

kontent = f.read()
f.close()

print(kontent, end='')