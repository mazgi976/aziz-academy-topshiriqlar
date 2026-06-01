n = int(input().strip())
users = []
for _ in range(n):
    username, active = input().split()
    users.append({'username': username, 'active': active == '1'})

count = 0
for user in users:
    if user['active']:
        count += 1 
        
print(count)
