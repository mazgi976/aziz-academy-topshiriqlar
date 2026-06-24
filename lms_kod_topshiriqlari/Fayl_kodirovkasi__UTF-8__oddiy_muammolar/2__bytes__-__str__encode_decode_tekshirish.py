matn = input()
data = matn.encode('utf-8')
if data.decode('utf-8') == matn:
    print("YES")
else:
    print("NO")