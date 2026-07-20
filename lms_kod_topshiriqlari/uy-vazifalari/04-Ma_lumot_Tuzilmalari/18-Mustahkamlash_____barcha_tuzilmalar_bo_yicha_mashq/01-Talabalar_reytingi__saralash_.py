n = int(input())
talabalar = []

for _ in range(n):
    ism, bal = input().split()
    talabalar.append((-int(bal), ism))
    
talabalar.sort()

for bal, ism in talabalar:
    print(f"{ism} {-bal}")