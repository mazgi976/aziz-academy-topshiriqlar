def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def pow(a: int, b: int) -> int:
    return a ** b


def dispatch(cmd: str, *args) -> int:
    if cmd == "add":
        return add(*args)
    elif cmd == "mul":
        return mul(*args)
    elif cmd == "pow":
        return pow(*args)
    
    
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        parts = input().split()
        cmd = parts[0]
        a, b = int(parts[1]), int(parts[2])
        print(dispatch(cmd, a, b))