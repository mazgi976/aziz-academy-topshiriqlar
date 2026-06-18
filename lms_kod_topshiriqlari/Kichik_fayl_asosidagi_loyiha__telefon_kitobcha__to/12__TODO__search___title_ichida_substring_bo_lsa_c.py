n = int(input())
todo_list = []

for _ in range(n):
    line = input().split()
    title = " ".join(line[:-1])
    done = int(line[-1])
    todo_list.append({"title": title, "done": done})
    
sub = input()

for item in todo_list:
    if sub in item['title']:
        print(item['title'])