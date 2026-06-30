class Rectangle:
    def __init__(self, w, h):
        self.valid = isinstance(w, int) and isinstance(h, int) and w > 0 and h > 0
        self.w, self.h = (w, h) if self.valid else (0, 0)
        
    def area(self):
        return self.w * self.h if self.valid else None
    
    def perimeter(self):
        return 2 * (self.w + self.h) if self.valid else None
    
try:
    w_input = input()
    h_input = input()
    
    if w_input.isdigit() and h_input.isdigit():
        rect = Rectangle(int(w_input), int(h_input))
        if rect.valid:
            print(f"A={rect.area()}")
            print(f"P={rect.perimeter()}")
        else:
            print("BAD")
    else:
        print("BAD")
except:
    print("BAD")