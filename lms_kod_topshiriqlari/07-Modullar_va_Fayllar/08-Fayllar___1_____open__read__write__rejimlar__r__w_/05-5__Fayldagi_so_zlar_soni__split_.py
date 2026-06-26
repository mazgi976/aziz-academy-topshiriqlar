s = input()

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def read(self): return s
f = Fayl()
f.write(s)
f.close()

matn = f.read()
f.close()

sozlar = matn.split()
print(len(sozlar))