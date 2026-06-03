s = input()

class Fayl:
    def __init__(self, content=""):
        self.content = content
    def write(self, text):
        self.content = text
    def close(self): pass
    def read(self):
        return self.content
    
f_src = Fayl()
f_src.write(s)
f_src.close()

src_content = f_src.read()
f_src.close()

f_dst = Fayl()
f_dst.write(src_content)
f_dst.close()

dst_content = f_dst.read()
f_dst.close()

print(dst_content)