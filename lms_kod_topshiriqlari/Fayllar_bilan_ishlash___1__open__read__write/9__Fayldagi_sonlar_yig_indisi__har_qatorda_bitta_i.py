n = int(input())
sonlar = [input() for _ in range(n)]

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def readlines(self): return [x + '\n' for x in sonlar]

f = Fayl()
for son in sonlar:
    f.write(son + '\n')
f.close()

qatorlar = f.readlines()
f.close()

yigindi = sum(int(x.strip()) for x in qatorlar)
print(yigindi)