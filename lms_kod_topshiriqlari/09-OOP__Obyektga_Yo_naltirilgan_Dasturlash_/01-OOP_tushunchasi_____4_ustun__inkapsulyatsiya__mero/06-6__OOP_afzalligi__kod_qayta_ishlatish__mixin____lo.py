class LoggerMixin:
    def log(self, msg):
        print(f"LOG:{msg}")
        
class Service(LoggerMixin):
    def run(self, action):
        self.log(action)
        print("DONE")
        
try:
    action = input().strip()
    if not action:
        print("BAD")
    else:
        service = Service()
        service.run(action)
except EOFError:
    print("BAD")