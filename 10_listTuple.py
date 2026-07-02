# print(type([1,2,3]))

marks=[76,56,87,56,'raaz',False]
# print(marks)
# print(marks[0])
# for i in marks:
#     print(i,end=',')


print(marks[-2]) #raaz
print(marks[1:-1])
print(marks[1:5])


# Tuple
myTuple=(1,2,3,4,5,"manish",True)
print(myTuple[0])
newTuple=list(myTuple)
newTuple.pop()
print(newTuple)
newTuple=tuple(newTuple)
print(myTuple[-1])

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
    
    
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
    
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      # using positive indexes
print(animals[-4:])     # using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     # using positive indexes
print(animals[-7:-2])   # using negative indexes