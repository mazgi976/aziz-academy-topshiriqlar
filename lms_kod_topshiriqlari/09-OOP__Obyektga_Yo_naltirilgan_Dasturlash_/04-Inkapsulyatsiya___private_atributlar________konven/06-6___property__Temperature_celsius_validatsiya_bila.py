class Temperature:
    def __init__(self, c):
        if isinstance(c, int):
            self._c = c
        else:
            self._c = None
                
    @property
    def celsius(self):
        return self._c
    
    @celsius.setter
    def celsius(self, value):
        if isinstance(value, int):
            self._c = value
        else:
            self._c = None
        
try:
    c_input = int(input())
    new_c_input = int(input())
        
    temp = Temperature(c_input)
    temp.celsius = new_c_input
        
    if temp.celsius is not None:
        print(f"C={temp.celsius}")
    else:
        print("BAD")
except ValueError:
    print("BAD")