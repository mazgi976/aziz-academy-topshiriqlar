class BaseNotifier:
    def send(self, to, msg):
        raise NotImplementedError("Subclasslar send metodini implementatsiya qilishi kerak")
        
class EmailNotifier(BaseNotifier):
    def send(self, to, msg):
        print(f"EMAIL->{to}: {msg}")
        
class SmsNotifier(BaseNotifier):
    def send(self, to, msg):
        print(f"SMS->{to}: {msg}")
        
try:
    kind = input().strip()
    to = input().strip()
    msg = input().strip()
    
    if not to or not msg:
        print("BAD")
    elif kind == "EMAIL":
        notifier = EmailNotifier()
        notifier.send(to, msg)
    elif kind == "SMS":
        notifier = SmsNotifier()
        notifier.send(to, msg)
    else:
        print("BAD")
except EOFError:
    print("BAD")