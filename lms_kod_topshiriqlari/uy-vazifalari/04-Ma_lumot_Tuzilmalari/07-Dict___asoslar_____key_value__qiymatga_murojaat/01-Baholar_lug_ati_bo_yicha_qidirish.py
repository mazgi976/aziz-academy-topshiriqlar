n = int(input())
baholar = {}

for _ in range(n):
    ism, baho = input().split()
    baholar[ism] = baho
    
qidiriladigan_ism = input()
print(baholar[qidiriladigan_ism])

    