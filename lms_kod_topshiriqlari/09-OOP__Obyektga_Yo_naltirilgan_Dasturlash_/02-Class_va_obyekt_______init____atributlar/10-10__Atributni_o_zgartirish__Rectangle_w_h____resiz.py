class Rectangle:
    def __init__(self, w, h):
        self.w = int(w)
        self.h = int(h)
        
    def resize(self, dw, dh):
        self.w += int(dw)
        self.h += int(dh)
        
try:
    w, h = input(), input()
    dw, dh = input(), input()
    r = Rectangle(w, h)
    r.resize(dw, dh)
    if r.w > 0 and r.h > 0:
        print(f"W={r.w} H={r.h}")
    else:
        print("BAD")
except:
    print("BAD")