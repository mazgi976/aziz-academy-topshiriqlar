def narx_bilan(narx, soliq=12):
    return narx + narx * soliq // 100


narx = int(input().strip())
soliq = int(input().strip())

print(narx_bilan(narx))
print(narx_bilan(narx, soliq))