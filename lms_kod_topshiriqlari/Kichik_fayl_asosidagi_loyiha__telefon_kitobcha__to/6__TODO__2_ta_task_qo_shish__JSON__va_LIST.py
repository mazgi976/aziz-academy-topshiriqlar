import json

t1 = input()
t2 = input()

data = [{"title": t1, "done": False}, {"title": t2, "done": False}]

for i, task in enumerate(data, 1):
    print(f"{i}) {task['title']} [ ]")