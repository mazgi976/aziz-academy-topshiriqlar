a = input()
b = input()
c = input()

class Fayl:
    def write(self, s): pass
    def close(self): pass
    def readlines(self): return [a+'\n', b+'\n', c+'\n']

f = Fayl()
f.write(a+'\n'+b+'\n'+c+'\n')
f.close()

lines = f.readlines()
f.close()

print(len(lines))
for x in lines:
    print(x, end='')