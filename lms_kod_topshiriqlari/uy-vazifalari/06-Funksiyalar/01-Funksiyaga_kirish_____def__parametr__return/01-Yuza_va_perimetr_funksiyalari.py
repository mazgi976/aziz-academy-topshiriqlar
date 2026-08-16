def yuza(en, boyi):
    return en * boyi

def perimetr(en, boyi):
    return 2 * (en + boyi)

if __name__ == "__main__":
    en = int(input())
    boyi = int(input())
    
    print(yuza(en, boyi))
    print(perimetr(en, boyi))