N = int(input())

print("Mahsulot".ljust(10) + "Soni".rjust(6))
print("-" * 16)

for _ in range(N):
    nom, son = input().split()
    print(nom.ljust(10) + son.rjust(6))