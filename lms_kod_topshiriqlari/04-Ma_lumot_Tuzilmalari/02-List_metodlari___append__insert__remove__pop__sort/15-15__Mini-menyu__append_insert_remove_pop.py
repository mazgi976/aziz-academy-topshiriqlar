lst = []

while True:
    cmd = input().split()
 
    if cmd[0] == "stop":
        break
        
    elif cmd[0] == "append":
        lst.append(int(cmd[1]))
        
    elif cmd[0] == "insert":
        lst.insert(int(cmd[1]), int(cmd[2]))
        
    elif cmd[0] == "remove":
        x = int(cmd[1])
        if x in lst:
            lst.remove(x)
            
    elif cmd[0] == "pop":
        if len(cmd) > 1:
            lst.pop(int(cmd[1]))
        elif lst: 
            lst.pop()
                
print(lst)
                