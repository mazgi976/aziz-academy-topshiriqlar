freq = {'a': 1}

def reset_freq():
    global freq
    freq = {}
    
def add_word(w):
    word = w.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        
word = input().strip()

reset_freq()
add_word(word)

print(freq)