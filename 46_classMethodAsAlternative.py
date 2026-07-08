class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(self,string):
        return self(string.split('-')[0],string.split('-')[1])
e=Employee("Manish",23000)

string="mohan-16000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)

        