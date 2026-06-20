# name='manish pandey'
# first_name=name[0]
# first_name=name[0:6] concept of slicing
# print(first_name)


# num_list='0123456789'
# print(name.upper())

fullName="    Manish Kumar Pandey       "
print(fullName.strip())

print(fullName.replace("Manish","Raaz"))
name="mohit, anjali, kajal, radha, rohit"
print(name.split(", ")) # for list


chai_type="Masala"
quantity=2
order="I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))


chai_variety=["Masala","Lemon","Ginger"]
print(" ".join(chai_variety))


chai="mohan said, \"Masala chai is awesome\" "
print(chai)

chai="masala\nchai"
print(chai)

chai=r"Masala\nchai"
print(chai)