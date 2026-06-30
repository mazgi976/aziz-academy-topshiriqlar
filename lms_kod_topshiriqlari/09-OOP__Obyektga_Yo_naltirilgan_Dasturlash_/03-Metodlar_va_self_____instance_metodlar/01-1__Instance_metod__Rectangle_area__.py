class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def area(self):
        if isinstance(self.w, int) and isinstance(self.h, int) and self.w > 0 and self.h > 0:
            return self.w * self.h
        return "BAD"

try:
    line1 = input()
    line2 = input()
    
    w = int(line1) if line1.isdigit() else line1
    h = int(line2) if line2.isdigit() else line2
    
    rect = Rectangle(w, h)
    print(rect.area())
except:
    print("BAD")