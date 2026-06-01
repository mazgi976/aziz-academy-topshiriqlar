n = int(input())
i = 2
while i * i <= n:
    if n % i == 0:
        print(i)
        while n % i == 0:
            n //= i
    i += 1        
if n > 1:
        print(n)