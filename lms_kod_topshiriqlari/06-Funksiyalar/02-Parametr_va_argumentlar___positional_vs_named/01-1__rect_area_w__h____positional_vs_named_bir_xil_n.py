w, h = map(int, input().split())

def rect_area(w, h):
    return w * h

res1 = rect_area(w, h)
res2 = rect_area(h=h, w=w)

print(res1)
print(res2)