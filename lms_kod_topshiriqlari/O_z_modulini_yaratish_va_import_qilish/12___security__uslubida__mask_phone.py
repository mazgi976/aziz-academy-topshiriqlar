def mask_phone(s: str) -> str:
    digits = "".join(char for char in s if char.isdigit())
    n = len(digits)
    
    if n == 12 and digits.startswith("998"):
        digits = digits[1:]
        n = len(digits)
        
    if n < 4:
        return "*" * n
    else:
        return "*" * (n - 4) + digits[-4:]
    
    
if __name__ == "__main__":
    s = input()
    print(mask_phone(s))