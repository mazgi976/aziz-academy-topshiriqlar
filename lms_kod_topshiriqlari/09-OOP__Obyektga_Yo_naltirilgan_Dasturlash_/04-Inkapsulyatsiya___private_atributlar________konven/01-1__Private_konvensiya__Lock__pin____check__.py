class Lock:
    def __init__(self, pin):
        if isinstance(pin, str) and len(pin) == 4 and pin.isdigit():
            self._pin = pin
        else:
            self._pin = "BAD"
            
    def check(self, try_pin):
        if not isinstance(try_pin, str) or len(try_pin) != 4 or not try_pin.isdigit():
            return "BAD"
        
        if self._pin == "BAD":
            return "BAD"
        
        if try_pin == self._pin:
            return "OK"
        else:
            return "NO"
        
pin = input()
try_pin = input()

lock = Lock(pin)
print(lock.check(try_pin))