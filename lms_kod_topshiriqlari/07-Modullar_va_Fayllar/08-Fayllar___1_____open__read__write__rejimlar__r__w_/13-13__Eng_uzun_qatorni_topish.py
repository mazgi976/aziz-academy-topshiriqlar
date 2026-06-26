n = int(input())
qatorlar = [input() for _ in range(n)]

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def readlines(self): return [x + '\n' for x in qatorlar]

f = Fayl()
for qator in qatorlar:
    f.write(qator + '\n')
f.close()

f_qatorlar = f.readlines()
f.close()

eng_uzun = max(f_qatorlar, key=len).rstrip('\n')
print(eng_uzun)