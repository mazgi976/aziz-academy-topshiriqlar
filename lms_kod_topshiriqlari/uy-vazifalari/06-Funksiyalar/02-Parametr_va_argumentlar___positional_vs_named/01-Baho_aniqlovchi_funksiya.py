def baho(a, b, c):
    orta = (a + b + c) / 3
    if orta >= 90:
        return "a'lo"
    elif orta >= 70:
        return "yaxshi"
    elif orta >= 60:
        return "qoniqarli"
    else:
        return "qoniqarsiz"
    
    
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

print(baho(a, b, c))