class Temperature:
    def __init__(self, value, scale):
        if scale == "C":
            self._celsius = value
        elif scale == "F":
            self._celsius = (value - 32) * 5 / 9
        else:
            raise ValueError
            
    def get_c(self):
        return int(round(self._celsius))
    
    def get_f(self):
        return int(round(self._celsius * 9 / 5 + 32))
    
try:
    scale = input().strip()
    value = int(input())
    
    if scale not in ["C", "F"]:
        print("BAD")
    else:
        temp = Temperature(value, scale)
        print(f"C={temp.get_c()}")
        print(f"F={temp.get_f()}")
except ValueError:
    print("BAD")
except EOFError:
    print("BAD")