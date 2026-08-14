first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
res = sorted(list({x for x in first if x in second}))
print(res)