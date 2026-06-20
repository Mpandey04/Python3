tea_varities=["black","green","Oolong","white"]
print(tea_varities)
print(tea_varities[-1])
print(tea_varities[1:3])
tea_varities[3]='masala'
print(tea_varities)
tea_varities[1:2]=["lemon"] #slicing dicing
print(tea_varities)

tea_varities[1:1]=["test","test"]
print(tea_varities)

tea_varities[1:3]=[]
print(tea_varities)

for list in tea_varities:
    print(list)
    # print(list,end="-")

if "Oolong" in tea_varities:
    print("I have Oolong tea")