nums = []

def push(x):
    nums.append(x)
    
def last():
    if not nums:
        return 'NONE'
    return nums[-1]

q = int(input())

for _ in range(q):
    command = input().split()
    if command[0] == 'push':
        x = int(command[1])
        push(x)
    elif command[0] == 'last':
        print(last())