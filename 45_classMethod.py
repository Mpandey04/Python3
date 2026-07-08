class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is:{self.company}")
    @classmethod
    def changeCOmpany(cls,newCOmpany):
        cls.company=newCOmpany
        
e1=Employee()
e1.name="Manish"
e1.show()
e1.changeCOmpany("Tesla")
e1.show()