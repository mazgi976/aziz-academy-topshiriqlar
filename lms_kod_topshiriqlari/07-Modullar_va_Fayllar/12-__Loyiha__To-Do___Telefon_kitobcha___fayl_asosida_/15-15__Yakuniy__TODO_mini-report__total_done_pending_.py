n = int(input())
tasks = []

for _ in range(n):
    line = input().split()
    tasks.append({"title": " ".join(line[:-1]), "done": int(line[-1])})
    
done_count = sum(t['done'] for t in tasks)
pending = n - done_count

print(f"total {n}")
print(f"done {done_count}")
print(f"pending {pending}")