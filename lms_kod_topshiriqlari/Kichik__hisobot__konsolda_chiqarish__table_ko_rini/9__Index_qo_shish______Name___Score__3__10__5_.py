n = int(input())

students = []

for _ in range(n):
    name, score = input().split()
    students.append((name, score))
    
for i, (name, score) in enumerate(students, 1):
    print(f"{i}|{name}|{score}")