score = int(input())

if score < 0 or score > 100:
    print("Notogri ball")
else:
    if score >= 90:
        print("Alo")
    elif score >= 75:
        print("Yaxshi")
    elif score >= 60:
        print("Qoniqarli")
    else:
        print("Yiqildi")