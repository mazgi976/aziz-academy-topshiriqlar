def find_first(s: str, ch: str) -> int:
    return s.find(ch)


def find_last(s: str, ch: str) -> int:
    return s.rfind(ch)


if __name__ == "__main__":
    s = input()
    ch = input()
    
    print(find_first(s, ch))
    print(find_last(s, ch))