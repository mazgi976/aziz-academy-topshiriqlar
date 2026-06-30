class Score:
    def __init__(self, start):
        self.score = start
        
    def add(self, points):
        if 0 <= self.score + points <= 100:
            self.score += points
            return True
        else:
            print("BAD")
            return False
        
    def grade(self):
        if self.score >= 90:
            print("A")
        elif self.score >= 70:
            print("B")
        elif self.score >= 50:
            print("C")
        else:
            print("D")
            
            
start = int(input())
points = int(input())

s = Score(start)

if s.add(points):
    s.grade()