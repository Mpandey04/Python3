#Reverse a string using loop
input_string=input("Give string")
reversed_str=""

for char in input_string:
    reversed_str=char+reversed_str
print(reversed_str)