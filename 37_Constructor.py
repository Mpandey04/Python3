# class person:
#     name="Manish Pandey"
#     occupation="AI Engineer"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
        
# p1=person()
# p1.info()


class person:
    def __init__(self,name,occ):
        print("Hey i am a person")
        self.name=name
        self.occupation=occ
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
p1=person("Manish","Engineer")
p1.info()

