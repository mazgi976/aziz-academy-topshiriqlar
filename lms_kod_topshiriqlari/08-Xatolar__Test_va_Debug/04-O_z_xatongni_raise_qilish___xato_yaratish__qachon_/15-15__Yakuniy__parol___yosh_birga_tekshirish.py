try:
    age = int(input())
    password = input()
    
    if age < 18 or len(password) < 6:
        raise ValueError
        
    print("ACCEPT")
except ValueError:
    print("REJECT")