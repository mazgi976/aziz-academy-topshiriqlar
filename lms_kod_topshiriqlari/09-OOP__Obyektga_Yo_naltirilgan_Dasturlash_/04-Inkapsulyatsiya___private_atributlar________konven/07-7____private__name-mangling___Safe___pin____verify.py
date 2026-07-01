class Safe:
    def __init__(self, pin):
        if isinstance(pin, str) and len(pin) == 4 and pin.isdigit():
            self.__pin = pin
        else:
            self.__pin = None
            
    def verify(self, try_pin):
        if self.__pin is None or not isinstance(try_pin, str) or len(try_pin) != 4 or not try_pin.isdigit():
            return "BAD"
        
        if try_pin == self.__pin:
            return "OK"
        else:
            return "NO"
        
try:
    pin_input = input()
    try_pin_input = input()
    
    safe = Safe(pin_input)
    print(safe.verify(try_pin_input))
except EOFError:
    pass