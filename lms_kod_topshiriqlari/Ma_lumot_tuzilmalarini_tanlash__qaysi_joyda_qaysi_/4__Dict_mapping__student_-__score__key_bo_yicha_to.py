n = int(input())
scores_dict = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    score = data[1]
    scores_dict[name] = score
    
q = int(input())

for _ in range(q):
    query_name = input()
    if query_name in scores_dict:
        print(scores_dict[query_name])
    else:
        print("NOT_FOUND")