class Counter:
    def __init__(self, start):
        self.value = start
        
    def inc(self):
        self.value += 1
        
try:
    start_val = input()
    n_val = input()
    
    if start_val.lstrip('-').isdigit() and n_val.isdigit():
        start = int(start_val)
        n = int(n_val)
        
        if n >= 0:
            c = Counter(start)
            for _ in range(n):
                c.inc()
            print(c.value)
        else:
            print("BAD")
    else:
        print("BAD")
except:
    print("BAD")