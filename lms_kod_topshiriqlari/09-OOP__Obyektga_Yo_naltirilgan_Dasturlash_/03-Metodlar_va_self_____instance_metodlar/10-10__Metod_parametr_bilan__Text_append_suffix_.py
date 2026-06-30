class Text:
    def __init__(self, base):
        self.base = base
        self.valid = isinstance(base, str) and len(base.strip()) > 0
        
    def append(self, suffix):
        if self.valid and isinstance(suffix, str) and len(suffix.strip()) > 0:
            self.base += suffix
            return True
        return False

try:
    base = input()
    suffix = input()
    
    text_obj = Text(base)
    
    if text_obj.append(suffix):
        print(text_obj.base)
    else:
        print("BAD")
except:
    print("BAD")