N = int(input())

for _ in range(N):
    nom, narx = input().split()
    print(nom.ljust(10) + narx.rjust(6))