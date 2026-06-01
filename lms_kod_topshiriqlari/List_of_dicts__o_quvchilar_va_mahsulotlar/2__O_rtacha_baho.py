n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})

total_score = sum(s['score'] for s in students)
average = total_score / n 

print(average)