counter = 0

def inc():
    global counter
    counter += 1
    return counter

n = int(input())

for _ in range(n):
    print(inc())