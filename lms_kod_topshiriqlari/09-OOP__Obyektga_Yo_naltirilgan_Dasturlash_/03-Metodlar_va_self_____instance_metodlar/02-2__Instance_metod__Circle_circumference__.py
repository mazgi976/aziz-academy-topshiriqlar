class Circle:
    def __init__(self, r):
        self.r = r
    def circumference(self):
        if isinstance(self.r, int) and self.r > 0:
            return int(2 * 3.14 * self.r)
        return "BAD"

try:
    line = input()
    r = int(line) if line.isdigit() else line
    c = Circle(r)
    print(c.circumference())
except:
    print("BAD")