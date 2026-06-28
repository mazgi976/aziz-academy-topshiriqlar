def safe_div(a, b):
    if b == 0:
        return 'DIV0'
    return float(a / b)

if __name__ == "__main__":
    try:
        a, b = map(int, input().split())
        result = safe_div(a, b)
        if isinstance(result, float):
            print(f"{result:.2f}")
        else:
            print(result)
    except (ValueError, EOFError):
        pass