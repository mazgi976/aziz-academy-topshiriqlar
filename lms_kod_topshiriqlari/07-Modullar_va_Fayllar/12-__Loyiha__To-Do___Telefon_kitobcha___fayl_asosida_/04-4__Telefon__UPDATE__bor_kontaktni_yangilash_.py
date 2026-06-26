n1, p1 = input().split()
n2, p2 = input().split()
query = input()

pbook = {n1: p1}
pbook[n2] = p2

print(pbook.get(query, "NOTFOUND"))