# class parentClass:
#     def parent_method(self):
#         print("This is parent method")

# class childClass(parentClass):
#     def parent_method(self):
#         print("Manish Pandey")
#     def child_method(self):
#         print("This is child method.")
#         super().parent_method()
        
# child_object=childClass()
# child_object.child_method()

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        
manish=Employee("Mohan",450)
Raaz=Programmer("Raaz paandey",123,"Python")
print(Raaz.name)
