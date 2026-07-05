# Juft va toq
# Kurs: Dasturlash / IT
# Mavzu: Mantiqiy operatorlar — and, or, not
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
a = int(input())
b = int(input())
c = int(input())

nums = [a, b, c]
evens = [x for x in nums if x % 2 == 0]

print(len(evens))

if evens:
    print(max(evens))
else:
    print(-1)