N = int(input())

eng_katta = None
eng_katta_pozitsiya = 0

for i in range(1, N + 1):
    son = int(input())
    if eng_katta is None or son > eng_katta:
        eng_katta = son
        eng_katta_pozitsiya = i
print(eng_katta_pozitsiya)