def chegirmali_narx(narx, foiz):
    chegirma = narx * foiz // 100
    return narx - chegirma


narx = int(input().strip())
foiz = int(input().strip())

print(chegirmali_narx(narx, foiz))