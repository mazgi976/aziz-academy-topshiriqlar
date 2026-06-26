counter = 0

def inc():
    global counter
    counter += 1
    return counter

def reset():
    global counter
    counter = 0
    return counter

q = int(input())

for _ in range(q):
    command = input().strip()
    if command == 'inc':
        print(inc())
    elif command == 'reset':
        print(reset())