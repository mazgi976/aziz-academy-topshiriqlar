def to_int(s: str, default: int = 0) -> int:
    try:
        return int(s)
    except ValueError:
        return default
    
    
def to_float(s: str, default: float = 0.0) -> float:
    try:
        return float(s)
    except ValueError:
        return default
    
    
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    
    print(to_int(s1))
    print(f"{to_float(s2):.2f}")