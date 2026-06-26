n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})

unique_tags = set()
for user in users:
    for tag in user['tags']:
        unique_tags.add(tag)
        
print(len(unique_tags))