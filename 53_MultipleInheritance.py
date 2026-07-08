class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is: {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"Dance is :{self.dance}")
        
class DancerEmployee(Dancer,Employee):
    def __init__(self, dance,name):
        self.dance=dance
        self.name=name
        
o=DancerEmployee("Kathak","shivani")
print(o.name)
print(o)
o.show()
print(o.dance)