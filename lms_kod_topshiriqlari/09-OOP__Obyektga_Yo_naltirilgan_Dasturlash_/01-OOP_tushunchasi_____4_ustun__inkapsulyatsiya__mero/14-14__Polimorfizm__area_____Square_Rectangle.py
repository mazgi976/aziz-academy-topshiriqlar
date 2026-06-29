data = input().split()
kind = data[0]

if kind == 'kv':
    a = int(data[1])
    print(a * a)
elif kind == 'rect':
    a = int(data[1])
    b = int(data[2])
    print(a * b)