n = int(input())
lines = [input() for _ in range(n)]

class Fayl:
    def write(self, text): pass
    def close(self): pass
    def readlines(self): return lines

f = Fayl()
for line in lines:
    f.write(line + '\n')
f.close()

read_lines = f.readlines()
f.close()

print(len(read_lines))