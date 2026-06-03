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

for qator in f_qatorlar:
    if qator.strip() != '':
        print(qator, end='')