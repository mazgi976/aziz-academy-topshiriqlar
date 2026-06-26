words = input().split()
unique_words = sorted({word.lower() for word in words})
print(*unique_words)