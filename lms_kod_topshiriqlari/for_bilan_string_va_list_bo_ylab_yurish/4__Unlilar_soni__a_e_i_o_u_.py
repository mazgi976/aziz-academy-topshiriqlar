s = input()
unlilar = "aeiou"
count = 0

for char in s:
    if char in unlilar:
        count += 1
print(count)
