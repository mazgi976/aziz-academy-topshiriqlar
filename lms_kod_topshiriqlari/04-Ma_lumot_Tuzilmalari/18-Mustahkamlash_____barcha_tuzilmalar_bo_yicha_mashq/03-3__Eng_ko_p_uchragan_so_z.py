from collections import Counter

words = input().split()
cnt = Counter(words)
print(max(cnt, key=cnt.get))