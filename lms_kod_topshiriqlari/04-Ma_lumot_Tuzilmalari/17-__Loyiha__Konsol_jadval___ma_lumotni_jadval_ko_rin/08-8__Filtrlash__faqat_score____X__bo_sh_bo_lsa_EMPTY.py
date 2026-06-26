n = int(input())

students = []

for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))
    
x = int(input())



found = False

for name, score in students:
    if score >= x:
        print(f"{name}={score}")
        found = True
        
if not found:
    print("EMPTY")
