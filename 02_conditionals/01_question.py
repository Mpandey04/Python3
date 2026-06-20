# Question no:1  Age group categorization
#Classify a person's age group:child(<13),Teenager(13-19),Adult(20-59),senior(60+)

age=int(input("Give me age \n"))

if age  < 13 :
    print("child")
elif age >=13 and age <=19 :
    print("Teenager")
elif age>=20 and age <=59:
    print("Adult")
else :
    print("Senior")
    
