freq = {}

def add_word(w):
    word = w.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        
n = int(input())

for _ in range(n):
    word = input().strip()
    add_word(word)
    
for word in sorted(freq.keys()):
    print(f"{word} {freq[word]}")