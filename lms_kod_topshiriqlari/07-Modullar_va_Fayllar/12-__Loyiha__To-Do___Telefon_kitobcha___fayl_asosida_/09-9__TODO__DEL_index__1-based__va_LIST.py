tasks = [input() for _ in range(3)]
k = int(input())

tasks.pop(k - 1)

for i, title in enumerate(tasks, 1):
    print(f"{i}) {title} [ ]")