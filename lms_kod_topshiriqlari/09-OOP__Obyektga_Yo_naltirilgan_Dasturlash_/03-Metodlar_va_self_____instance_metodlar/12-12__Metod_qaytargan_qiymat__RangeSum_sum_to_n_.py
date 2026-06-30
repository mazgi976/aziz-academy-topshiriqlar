class RangeSum:
    def __init__(self, base):
        self.base = base
        self.is_valid = isinstance(base, int)
        
    def sum_to(self, n):
        if self.is_valid and isinstance(n, int) and n >= 0:
            return self.base + (n * (n + 1) // 2)
        return None

try:
    base_input = input()
    n_input = input()
    
    if (base_input.lstrip('-').isdigit() or (base_input.startswith('-') and base_input[1:].isdigit())) and n_input.isdigit():
        rs = RangeSum(int(base_input))
        result = rs.sum_to(int(n_input))
        
        if result is not None:
            print(result)
        else:
            print("BAD")
    else:
        print("BAD")
except:
    print("BAD")