def fmt_kv(key: str, value: str) -> str:
    return f"{key}={value}"


def fmt_table_row(a: str, b: str, c: str) -> str:
    return f"{a} | {b} | {c}"


if __name__ == "__main__":
    key = input()
    value = input()
    a, b, c = input().split()
    
    print(fmt_kv(key, value))
    print(fmt_table_row(a, b, c))