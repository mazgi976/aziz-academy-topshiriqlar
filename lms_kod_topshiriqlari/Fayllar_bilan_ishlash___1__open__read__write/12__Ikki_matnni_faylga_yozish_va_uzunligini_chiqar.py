s1 = input()
s2 = input()

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def read(self): return s1 + ' ' + s2

f = Fayl()
f.write(s1 + ' ' + s2)
f.close()

matn = f.read()
f.close()

print(len(matn))