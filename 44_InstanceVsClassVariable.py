class Employee:
    company="Apple"
    def __init__(self,name):
        self.name=name
    def showDetail(self):
        print(f"Employee name is:{self.name} and company:{self.company}")
        
emp1=Employee("Manish")
emp1.showDetail()
# Employee.showDetail(emp1)

emp2=Employee("Raaz")
emp2.company="AppleIndia"
emp2.showDetail()