class Counter:
    def __init__(self, mode, start=None):
        self.mode = mode
        self.start = start
        self.value = None
        
    def calculate(self):
        if self.mode == "DEF":
            self.value = 0
            return self.value
        elif self.mode == "CUSTOM":
            try:
                self.value = int(self.start)
                return self.value
            except (ValueError, TypeError):
                return "BAD"
        return "BAD"

mode = input()
if mode == "CUSTOM":
    start = input()
    counter = Counter(mode, start)
else:
    counter = Counter(mode)
    
print(counter.calculate())