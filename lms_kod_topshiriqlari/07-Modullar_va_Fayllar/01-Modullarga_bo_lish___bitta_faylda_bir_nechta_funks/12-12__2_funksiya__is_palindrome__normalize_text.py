def normalize_text(s):
    return "".join(char.lower() for char in s if char.isalpha())

def is_palindrome(s):
    clean_s = normalize_text(s)
    return clean_s == clean_s[::-1]

s = input()
print(is_palindrome(s))