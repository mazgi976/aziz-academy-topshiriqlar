def hisobla(a, b):
    return a + b, a * b

n1, n2 = map(int, input().split())
yigindi, kopaytma = hisobla(n1, n2)

print(yigindi)
print(kopaytma)