transport_turi = int(input())
yolovchi_tolfasi = int(input())

if transport_turi == 1 or transport_turi == 2:
    narx = 1700
elif transport_turi == 3:
    narx = 4000
else:
    print("Notogri transport")
    exit()
    
if yolovchi_tolfasi == 1:
    print(narx)
elif yolovchi_tolfasi == 2:
    print(narx // 2)
elif yolovchi_tolfasi == 3:
    print(0)
else:
    print("Notogri tolfa")