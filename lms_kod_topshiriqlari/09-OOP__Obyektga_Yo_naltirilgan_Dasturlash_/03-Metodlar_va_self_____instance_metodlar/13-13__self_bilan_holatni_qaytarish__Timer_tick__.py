class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.is_valid = isinstance(seconds, int) and seconds >= 0
        
    def tick(self):
        if self.is_valid and self.seconds > 0:
            self.seconds -= 1
        return self.seconds
    
try:
    seconds_input = input()
    k_input = input()
    
    if seconds_input.isdigit() and k_input.isdigit():
        seconds = int(seconds_input)
        k = int(k_input)
        
        timer = Timer(seconds)
        for _ in range(k):
            timer.tick()
            
        print(timer.seconds)
    else:
        print("BAD")
except:
    print("BAD")