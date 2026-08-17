def jadval(son, nechtagacha=5):
    return " ".join(str(son * i) for i in range(1, nechtagacha + 1))


son = int(input().strip())
nechtagacha = int(input().strip())

print(jadval(son))
print(jadval(son, nechtagacha))