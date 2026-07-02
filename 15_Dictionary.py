dic1={
    "Manish":445,
    "Raaz":400,
    "Kamal":390,
    "Rohit":340
}
print(dic1["Raaz"])
print(dic1.keys())
print(dic1.values())


li=[1,2,3,4,5,6,7,8]

FirstItemOfList,*remainingItemOfList,LastItemOfList=li
print(FirstItemOfList)
print(remainingItemOfList)
print(LastItemOfList)


for key in dic1.keys():
    print(f"The value corresponding to the key {key} is {dic1[key]}")

for key,value in dic1.items():
    print(f"The value corresponding to the key {key} is {dic1[key]}")
    