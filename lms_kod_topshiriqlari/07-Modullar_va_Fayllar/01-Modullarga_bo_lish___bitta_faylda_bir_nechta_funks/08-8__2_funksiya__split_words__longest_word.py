def split_words(s):
    return s.split()

def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)

s = input()
words = split_words(s)
print(longest_word(words))