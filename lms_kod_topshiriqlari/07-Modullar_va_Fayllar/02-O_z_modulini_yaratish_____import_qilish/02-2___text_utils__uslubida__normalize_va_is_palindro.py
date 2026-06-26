def normalize(s: str) -> str:
    return "".join(char.lower() for char in s if char.isalpha())


def is_palindrome(s: str) -> bool:
    clean_s = normalize(s)
    return clean_s == clean_s[::-1]


if __name__ == "__main__":
    s = input()
    print(is_palindrome(s))