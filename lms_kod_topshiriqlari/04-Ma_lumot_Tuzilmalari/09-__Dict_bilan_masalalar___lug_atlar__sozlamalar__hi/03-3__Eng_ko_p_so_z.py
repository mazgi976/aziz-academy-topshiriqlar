n = int(input())
words = [input().strip() for _ in range(n)]
print(max(set(words), key=lambda w: (words.count(w), -words.index(w))))