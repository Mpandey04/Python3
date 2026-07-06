class person:
    name="Manish"
    occupation="Software Engineer"
    networth=10
    def Info(self):
        print(f"{self.name} is a {self.occupation}")
    
p=person()
# p.name="Raaz Pandey"
# p.occupation="AI Automation Engineer"
# print(p.name,p.occupation)


p.name="Mohit"
p.occupation="Accountant"

p2=person()
p2.name="Nidhi"
p2.occupation="Full stack developer"
p2.Info()
p.Info()