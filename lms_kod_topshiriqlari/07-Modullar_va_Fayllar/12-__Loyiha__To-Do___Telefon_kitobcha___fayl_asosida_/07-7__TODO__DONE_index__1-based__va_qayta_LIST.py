import json

t1, t2 = input(), input()
k = int(input())

data = [{"title": t1, "done": False}, {"title": t2, "done": False}]
data[k-1]["done"] = True

for i, task in enumerate(data, 1):
    status = "[x]" if task["done"] else "[ ]"
    print(f"{i}) {task['title']} {status}")