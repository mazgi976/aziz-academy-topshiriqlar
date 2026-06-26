n = int(input())
phone_book = []

for _ in range(n):
    phone_book.append(input().split())
    
prefix = input()
matches = []

for entry in phone_book:
    if entry[0].startswith(prefix):
        matches.append(entry)
        
matches.sort()

for entry in matches:
    print(f"{entry[0]} {entry[1]}")