class Student:
    school = "PDP"
    def __init__(self, name):
        self.name = name
        
    def display(self):
        clean_name = self.name.strip()
        if clean_name:
            return f"{clean_name} @ {self.school}"
        return "BAD"

print(Student(input()).display())