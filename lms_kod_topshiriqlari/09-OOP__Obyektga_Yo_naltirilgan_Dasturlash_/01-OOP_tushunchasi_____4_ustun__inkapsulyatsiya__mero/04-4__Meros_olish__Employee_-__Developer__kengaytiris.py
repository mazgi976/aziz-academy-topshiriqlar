class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def total_pay(self):
        return self.salary
    
class Developer(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        
    def total_pay(self):
        return self.salary + self.bonus
    
try:
    kind = input().strip()
    name = input().strip()
    salary = int(input())
    
    if not name or salary < 0:
        print("BAD")
    elif kind == "EMP":
        emp = Employee(name, salary)
        print(emp.total_pay())
    elif kind == "DEV":
        bonus = int(input())
        if bonus < 0:
            print("BAD")
        else:
            dev = Developer(name, salary, bonus)
            print(dev.total_pay())
    else:
        print("BAD")
except ValueError:
    print("BAD")