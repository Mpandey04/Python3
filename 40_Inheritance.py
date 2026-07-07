class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of the empolyee:{self.name} and ID: {self.id}")
        
e1=Employee("Rohan",500)
e1.showDetails()

class Programmer(Employee):
    def showLanguage(self):
        print(f"The Default language is python")
        
e2=Programmer("Manish",600)
e2.showLanguage()
e2.showDetails()
