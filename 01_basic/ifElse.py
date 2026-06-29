age=int(input("enter your age\n"))

print("Your age is:",age)

#conditional Operators
# >,<,>=,<=.==,!=
# print(age>18)
# print(age<18)
# print(age<=18)
# print(age>=18)
# print(age!=18)
if (age>18):
    print("You can drive")
else:
    print("You can not drive")
    
budget=int(input("enter your budget\n"))

if (budget>500):
    print("You can buy mangoose")
elif (budget<=500 and budget>300):
    print("You can buy banana")
else:
    print("You can not buy mangoo or banana34 ")