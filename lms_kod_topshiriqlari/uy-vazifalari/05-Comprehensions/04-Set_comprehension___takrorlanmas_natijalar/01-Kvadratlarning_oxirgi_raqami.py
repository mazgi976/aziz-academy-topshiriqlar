res = sorted(list({(int(x) * int(x)) % 10 for x in input().split()}))
print(res)