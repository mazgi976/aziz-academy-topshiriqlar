import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    word = input_data[0]
    vowels = "aeiou"
    count = 0
    
    for ch in word:
       if ch in vowels:
        count += 1

    print(count)
    
    
if __name__ == "__main__":
    solve()