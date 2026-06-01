n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})

max_course = data['courses'][0]

for course in data['courses']:
    if len(course['students']) > len(max_course['students']):
        max_course = course 
        
print(max_course['name'])
        