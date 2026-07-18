katta_kolleksiya = set(input().split())
tekshiriladigan_qator = input().split()

sanoq = 0
for element in tekshiriladigan_qator:
    if element in katta_kolleksiya:
        sanoq += 1
        
print(sanoq)
