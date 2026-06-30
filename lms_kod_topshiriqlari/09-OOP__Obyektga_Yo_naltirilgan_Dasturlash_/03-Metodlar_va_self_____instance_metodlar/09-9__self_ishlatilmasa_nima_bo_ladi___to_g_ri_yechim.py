class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def swap(self):
                self.x, self.y = self.y, self.x
                
try:
    x_input = input()
    y_input = input()
    
    if (x_input.lstrip('-').isdigit() or (x_input.startswith('-') and x_input[1:].isdigit())) and \
       (y_input.lstrip('-').isdigit() or (y_input.startswith('-') and y_input[1:].isdigit())):
            
        x = int(x_input)
        y = int(y_input)
        
        p = Pair(x, y)
        p.swap()
        print(f"X={p.x} Y={p.y}")
    else:
        print("BAD")
except:
    print("BAD")