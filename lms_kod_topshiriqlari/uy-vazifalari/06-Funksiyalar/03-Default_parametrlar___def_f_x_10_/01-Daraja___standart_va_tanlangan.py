def daraja(asos, kotarma=2):
    return asos**kotarma


asos = int(input().strip())
kotarma = int(input().strip())

print(daraja(asos))
print(daraja(asos, kotarma))