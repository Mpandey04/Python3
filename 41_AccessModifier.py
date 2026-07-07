# class Employee:
#     def __init__(self):
#         self.__name="Manish"
        
# a=Employee()
# # print(a.__name)#can not be accessed directly
# print(a._Employee__name)


class student:
    def __init__(self):
        self._name="Manish Pandey"
    def _fullName(self):
        return "Manish Kumar PANDEY"
    
class subject(student):
    pass

obj=student()
obj1=subject()

print(obj._name)
print(obj._fullName())

print(obj1._name)
print(obj1._fullName())