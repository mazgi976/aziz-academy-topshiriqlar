# Kodingizni shu yerga yozing
n = int(input())
words = [input().strip() for _ in range(n)]
target = input().strip()
print(words.count(target))