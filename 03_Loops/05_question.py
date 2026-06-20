#find the first non-repeated character
#Given a string,find the first non-repeated character.

input_str=input("Give any string\n")

for char in input_str:
    if input_str.count(char)==1:
        print("char is:",char)
        break
