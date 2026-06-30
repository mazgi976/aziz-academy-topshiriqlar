class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        try:
            x, y = int(self.x), int(self.y)
            return f"X={x} Y={y}"
        except:
            return "BAD"
    
print(Point(input(), input()).display())