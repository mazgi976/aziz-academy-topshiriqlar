s1 = input()
s2 = input()

class FaylTizimi:
    def write(self, text): pass
    def close(self): pass
    def read(self): return s1 + '\n' + s2

f = FaylTizimi()
f.write(s1 + '\n')
f.close()

f = FaylTizimi()
f.write(s2)
f.close()

kontent = f.read()
f.close()

print(kontent)