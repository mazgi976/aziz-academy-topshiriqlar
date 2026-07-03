gap = input()
bos_joylar_soni = 0

for belgi in gap:
    if belgi == ' ':
        bos_joylar_soni += 1
        
print(bos_joylar_soni + 1)